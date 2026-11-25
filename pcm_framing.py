"""
PCM Packet Framing and Deframing Module for GNU Radio 3.10
Project: PRJ-MCOM (Mobile Communications - VGU Sem5)
Author: Nguyen Huynh Van Phuong (Lead) / Antigravity AI

Specifications:
- Sample Rate: 48 kHz
- Audio Format: 16-bit signed PCM mono
- Frame Size: 48 samples (1.0 ms duration)
- Packet Structure:
  [0..3]   Preamble: 0xAC 0x62 0xAC 0x62 (32-bit sync word)
  [4..5]   Sequence Counter: uint16 (Logical timestamp, 0..65535)
  [6..7]   Payload Length: uint16 (96 bytes = 48 samples * 2 bytes)
  [8..103] Audio Payload: 48 int16 samples (96 bytes)
  Total Packet Length = 104 bytes
"""

import numpy as np
import struct
from gnuradio import gr

PREAMBLE = bytes([0xAC, 0x62, 0xAC, 0x62])
PREAMBLE_LEN = len(PREAMBLE)
HEADER_LEN = PREAMBLE_LEN + 4  # 4 + 2 (seq) + 2 (len) = 8 bytes
FRAME_SAMPLES = 48
PAYLOAD_BYTES = FRAME_SAMPLES * 2  # 96 bytes
PACKET_TOTAL_LEN = HEADER_LEN + PAYLOAD_BYTES  # 104 bytes


class PCMPacketizerBlock(gr.basic_block):
    """
    GNU Radio Block: Audio Samples (float32) -> Framed Packet Byte Stream (uint8)
    """
    def __init__(self, frame_samples=FRAME_SAMPLES):
        gr.basic_block.__init__(
            self,
            name="pcm_packetizer",
            in_sig=[np.float32],
            out_sig=[np.uint8]
        )
        self.frame_samples = frame_samples
        self.seq_num = 0
        self.set_output_multiple(PACKET_TOTAL_LEN)

    def forecast(self, noutput_items, ninputs):
        # To produce noutput_items (multiple of 104), we need corresponding frames
        n_pkts = (noutput_items + PACKET_TOTAL_LEN - 1) // PACKET_TOTAL_LEN
        return [n_pkts * self.frame_samples]

    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]

        n_in = len(in0)
        n_out = len(out0)

        n_pkts = min(n_in // self.frame_samples, n_out // PACKET_TOTAL_LEN)
        if n_pkts == 0:
            return 0

        for i in range(n_pkts):
            offset_in = i * self.frame_samples
            offset_out = i * PACKET_TOTAL_LEN

            # Convert 48 float32 samples to int16 PCM bytes
            frame_float = in0[offset_in:offset_in + self.frame_samples]
            frame_int16 = np.clip(frame_float * 32767.0, -32768, 32767).astype(np.int16)
            pcm_bytes = frame_int16.tobytes()

            # Pack header: Preamble (4B) + SeqNum (2B) + Length (2B)
            header = PREAMBLE + struct.pack("<HH", self.seq_num & 0xFFFF, len(pcm_bytes))
            packet_bytes = header + pcm_bytes

            out0[offset_out:offset_out + PACKET_TOTAL_LEN] = np.frombuffer(packet_bytes, dtype=np.uint8)
            self.seq_num = (self.seq_num + 1) & 0xFFFF

        self.consume(0, n_pkts * self.frame_samples)
        return n_pkts * PACKET_TOTAL_LEN


class PCMDepacketizerBlock(gr.basic_block):
    """
    GNU Radio Block: Framed Packet Byte Stream (uint8) -> Audio Samples (float32)
    With Preamble Synchronization and Packet Loss Detection via Sequence Counter.
    """
    def __init__(self, frame_samples=FRAME_SAMPLES):
        gr.basic_block.__init__(
            self,
            name="pcm_depacketizer",
            in_sig=[np.uint8],
            out_sig=[np.float32]
        )
        self.frame_samples = frame_samples
        self.last_seq = -1
        self.total_packets_received = 0
        self.total_packets_lost = 0
        self.set_output_multiple(self.frame_samples)

    def forecast(self, noutput_items, ninputs):
        n_pkts = (noutput_items + self.frame_samples - 1) // self.frame_samples
        return [n_pkts * PACKET_TOTAL_LEN]

    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]

        n_in = len(in0)
        n_out = len(out0)

        if n_in < PACKET_TOTAL_LEN:
            return 0

        # Search for preamble synchronization
        search_window = min(n_in, 2048)
        pos = bytes(in0[:search_window]).find(PREAMBLE)

        if pos == -1:
            # Drop unaligned bytes leaving enough for potential preamble overlap
            discard = max(1, search_window - PREAMBLE_LEN + 1)
            self.consume(0, discard)
            return 0

        if pos > 0:
            # Advance stream to align preamble at index 0
            self.consume(0, pos)
            return 0

        # Now stream is aligned to PREAMBLE
        n_pkts = min(n_in // PACKET_TOTAL_LEN, n_out // self.frame_samples)
        if n_pkts == 0:
            return 0

        valid_pkts = 0
        for i in range(n_pkts):
            offset_in = i * PACKET_TOTAL_LEN
            offset_out = valid_pkts * self.frame_samples

            # Check if this packet still starts with PREAMBLE
            pkt_preamble = bytes(in0[offset_in:offset_in + PREAMBLE_LEN])
            if pkt_preamble != PREAMBLE:
                # Synchronization lost midway, break to realign in next work call
                break

            # Parse header
            header_bytes = bytes(in0[offset_in + PREAMBLE_LEN:offset_in + HEADER_LEN])
            seq_num, payload_len = struct.unpack("<HH", header_bytes)

            if payload_len != PAYLOAD_BYTES:
                # Corrupted packet header
                break

            # Extract PCM payload
            pcm_bytes = in0[offset_in + HEADER_LEN:offset_in + PACKET_TOTAL_LEN].tobytes()
            int16_samples = np.frombuffer(pcm_bytes, dtype=np.int16)
            float_samples = int16_samples.astype(np.float32) / 32767.0

            out0[offset_out:offset_out + self.frame_samples] = float_samples
            valid_pkts += 1

            # Sequence Continuity Tracking
            if self.last_seq >= 0:
                expected_seq = (self.last_seq + 1) & 0xFFFF
                if seq_num != expected_seq:
                    lost = (seq_num - expected_seq) & 0xFFFF
                    self.total_packets_lost += lost
            self.last_seq = seq_num
            self.total_packets_received += 1

        if valid_pkts > 0:
            self.consume(0, valid_pkts * PACKET_TOTAL_LEN)
            return valid_pkts * self.frame_samples
        else:
            # Discard 1 byte to restart search
            self.consume(0, 1)
            return 0
