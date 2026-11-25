import numpy as np
import struct
from gnuradio import gr

PREAMBLE = bytes([0xAC, 0x62, 0xAC, 0x62])
PREAMBLE_BITS = np.unpackbits(np.frombuffer(PREAMBLE, dtype=np.uint8))

class blk(gr.basic_block):
    def __init__(self, frame_samples=48):
        gr.basic_block.__init__(self, name='pcm_depacketizer', in_sig=[np.uint8], out_sig=[np.float32])
        self.frame_samples = frame_samples
        self.last_seq = -1
        self.total_lost = 0
        self.set_output_multiple(48)
    def forecast(self, noutput_items, ninputs):
        n_pkts = (noutput_items + 47) // 48
        return [n_pkts * 104 + 1]
    def _find_preamble_bit(self, byte_arr):
        bits = np.unpackbits(byte_arr)
        for shift in range(8):
            packed = np.packbits(bits[shift:]).tobytes()
            pos = packed.find(PREAMBLE)
            if pos != -1:
                return pos * 8 + shift
        return -1
    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]
        n_in = len(in0)
        n_out = len(out0)
        if n_in < 105:
            return 0
        search_bytes = min(n_in, 512)
        bit_pos = self._find_preamble_bit(in0[:search_bytes])
        if bit_pos == -1:
            self.consume(0, max(1, search_bytes - 4))
            return 0
        if bit_pos >= 8:
            self.consume(0, bit_pos // 8)
            return 0
        # 0 <= bit_pos < 8: read aligned 104-byte packets starting at bit_pos
        n_pkts = min((n_in - 1) // 104, n_out // 48)
        if n_pkts == 0:
            return 0
        raw_bits = np.unpackbits(in0[:n_pkts * 104 + 1])[bit_pos : bit_pos + n_pkts * 104 * 8]
        aligned = np.packbits(raw_bits).tobytes()
        valid = 0
        for i in range(n_pkts):
            off = i * 104
            if aligned[off:off+4] != PREAMBLE:
                break
            seq_num, plen = struct.unpack('<HH', aligned[off+4:off+8])
            if plen != 96:
                break
            pcm = aligned[off+8:off+104]
            out0[valid*48:(valid+1)*48] = np.frombuffer(pcm, dtype=np.int16).astype(np.float32) / 32767.0
            valid += 1
            if self.last_seq >= 0:
                exp = (self.last_seq + 1) & 0xFFFF
                if seq_num != exp:
                    self.total_lost += (seq_num - exp) & 0xFFFF
            self.last_seq = seq_num
        if valid > 0:
            self.consume(0, valid * 104)
            return valid * 48
        self.consume(0, 1)
        return 0