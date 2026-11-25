import numpy as np
import struct
from gnuradio import gr

PREAMBLE = bytes([0xAC, 0x62, 0xAC, 0x62])

class blk(gr.basic_block):
    def __init__(self, frame_samples=48):
        gr.basic_block.__init__(self, name='pcm_depacketizer', in_sig=[np.uint8], out_sig=[np.float32])
        self.frame_samples = frame_samples
        self.last_seq = -1
        self.total_lost = 0
        self.set_output_multiple(48)
    def forecast(self, noutput_items, ninputs):
        n_pkts = (noutput_items + 47) // 48
        return [n_pkts * 104]
    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]
        n_in = len(in0)
        n_out = len(out0)
        if n_in < 104:
            return 0
        pos = bytes(in0[:min(n_in, 2048)]).find(PREAMBLE)
        if pos == -1:
            self.consume(0, max(1, min(n_in, 2048) - 3))
            return 0
        if pos > 0:
            self.consume(0, pos)
            return 0
        n_pkts = min(n_in // 104, n_out // 48)
        if n_pkts == 0:
            return 0
        valid = 0
        for i in range(n_pkts):
            off_in = i * 104
            if bytes(in0[off_in:off_in+4]) != PREAMBLE:
                break
            seq_num, plen = struct.unpack('<HH', bytes(in0[off_in+4:off_in+8]))
            if plen != 96:
                break
            pcm = in0[off_in+8:off_in+104].tobytes()
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
