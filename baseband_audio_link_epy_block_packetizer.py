import numpy as np
import struct
from gnuradio import gr

PREAMBLE = bytes([0xAC, 0x62, 0xAC, 0x62])

class blk(gr.basic_block):
    def __init__(self, frame_samples=48):
        gr.basic_block.__init__(self, name='pcm_packetizer', in_sig=[np.float32], out_sig=[np.uint8])
        self.frame_samples = frame_samples
        self.seq_num = 0
        self.set_output_multiple(104)
    def forecast(self, noutput_items, ninputs):
        n_pkts = (noutput_items + 103) // 104
        return [n_pkts * self.frame_samples]
    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]
        n_pkts = min(len(in0) // self.frame_samples, len(out0) // 104)
        if n_pkts == 0:
            return 0
        for i in range(n_pkts):
            s_in = in0[i*48:(i+1)*48]
            s_int16 = np.clip(s_in * 32767.0, -32768, 32767).astype(np.int16)
            pcm_bytes = s_int16.tobytes()
            header = PREAMBLE + struct.pack('<HH', self.seq_num & 0xFFFF, len(pcm_bytes))
            out0[i*104:(i+1)*104] = np.frombuffer(header + pcm_bytes, dtype=np.uint8)
            self.seq_num = (self.seq_num + 1) & 0xFFFF
        self.consume(0, n_pkts * 48)
        return n_pkts * 104
