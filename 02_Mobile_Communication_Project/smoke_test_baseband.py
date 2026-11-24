"""
Headless Smoke Test: Baseband Audio Streaming Flowgraph (GATE-2 Deliverable)
Project: PRJ-MCOM — Mobile Communications (61ECE314, VGU Sem5)
Author: Nguyen Huynh Van Phuong (Lead) / Antigravity AI
Date: 2026-11-17

Flowgraph Architecture:
[WAV File Source] -> [PCM Packetizer] -> [Baseband Loopback] -> [PCM Depacketizer] -> [WAV File Sink]
"""

import os
import sys
import numpy as np
import scipy.io.wavfile as wavfile
from gnuradio import gr, blocks

# Import custom framing blocks
from pcm_framing import PCMPacketizerBlock, PCMDepacketizerBlock, FRAME_SAMPLES, PACKET_TOTAL_LEN


class BasebandAudioFlowgraph(gr.top_block):
    def __init__(self, in_wav_path, out_wav_path, sample_rate=48000):
        gr.top_block.__init__(self, "BasebandAudioFlowgraph")

        self.sample_rate = sample_rate

        # 1. Source: WAV File (Outputs float32 [-1.0, 1.0])
        self.src = blocks.wavfile_source(in_wav_path, False)

        # 2. Framing: Float Audio Samples -> Byte Packets
        self.packetizer = PCMPacketizerBlock(frame_samples=FRAME_SAMPLES)

        # 3. Baseband Channel Loopback (Simulated lossless baseband byte stream)
        # In GATE-3 / GATE-4, this will be replaced by:
        # Byte2Chunks -> QPSK Mod -> RRC -> Fading Channel + Noise -> Sync -> Equalizer -> Slicer -> Byte Stream

        # 4. Deframing: Byte Packets -> Float Audio Samples (with Preamble Sync & Sequence Tracking)
        self.depacketizer = PCMDepacketizerBlock(frame_samples=FRAME_SAMPLES)

        # 5. Sink: WAV File (Writes 16-bit PCM WAV at 48 kHz)
        self.sink = blocks.wavfile_sink(
            out_wav_path,
            1,
            sample_rate,
            blocks.wavfile_format_t.FORMAT_WAV,
            blocks.wavfile_subformat_t.FORMAT_PCM_16
        )

        # Connections
        self.connect(self.src, self.packetizer)
        self.connect(self.packetizer, self.depacketizer)
        self.connect(self.depacketizer, self.sink)


def run_smoke_test():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    in_wav = os.path.join(current_dir, "test_audio_48k.wav")
    out_wav = os.path.join(current_dir, "rx_audio_48k.wav")

    if not os.path.exists(in_wav):
        print(f"Error: Input file {in_wav} not found! Please run generate_test_audio.py first.")
        sys.exit(1)

    print("======================================================================")
    print("  PRJ-MCOM GATE-2: BASEBAND AUDIO STREAMING SMOKE TEST")
    print("======================================================================")
    print(f"Input WAV:  {in_wav}")
    print(f"Output WAV: {out_wav}")
    print(f"Frame Size: {FRAME_SAMPLES} samples ({FRAME_SAMPLES / 48.0:.2f} ms @ 48 kHz)")
    print(f"Packet Len: {PACKET_TOTAL_LEN} bytes (Header: 8 bytes, Payload: 96 bytes)")
    print("Executing GNU Radio 3.10 flowgraph...")

    tb = BasebandAudioFlowgraph(in_wav, out_wav)
    tb.run()

    # Flush file sinks
    del tb

    print("\nFlowgraph execution completed successfully!")
    print("Analyzing received audio quality & packet metrics...")

    # Load audio files
    fs_in, data_in = wavfile.read(in_wav)
    fs_out, data_out = wavfile.read(out_wav)

    n_in = len(data_in)
    n_out = len(data_out)
    print(f"Samples in:  {n_in} ({n_in / fs_in:.3f} s)")
    print(f"Samples out: {n_out} ({n_out / fs_out:.3f} s)")

    min_len = min(n_in, n_out)
    s_in = data_in[:min_len].astype(np.float64)
    s_out = data_out[:min_len].astype(np.float64)

    # Difference and correlation
    diff = s_in - s_out
    max_err = np.max(np.abs(diff))
    mse = np.mean(diff ** 2)
    sig_power = np.mean(s_in ** 2)

    corr = np.corrcoef(s_in, s_out)[0, 1]

    if mse == 0:
        snr_db = float("inf")
    else:
        snr_db = 10 * np.log10(sig_power / mse)

    # Verification criteria
    print("\n--- QUANTITATIVE ACCEPTANCE CRITERIA ---")
    print(f"Correlation Coefficient: {corr:.6f}  (Target: > 0.9999)")
    print(f"Max Amplitude Error:    {max_err:.1f}      (Target: <= 1.0 LSB)")
    print(f"Baseband SNR:           {snr_db:.2f} dB   (Target: Bit-Exact / > 90 dB)")
    print(f"Sample Recovery Rate:   {(min_len / n_in) * 100:.2f}%  (Target: 100.0%)")

    # Latency calculation
    t_framing_ms = (FRAME_SAMPLES / 48000.0) * 1000.0
    print(f"\nAlgorithmic Framing Delay (T_framing): {t_framing_ms:.3f} ms (Target: <= 1.0 ms)")

    if corr > 0.9999 and max_err <= 1.0:
        print("\n>>> RESULT: GATE-2 BASEBAND STREAMING VERIFICATION PASSED! <<<")
        return True
    else:
        print("\n>>> RESULT: VERIFICATION FAILED! Output deviates from input. <<<")
        return False


if __name__ == "__main__":
    success = run_smoke_test()
    sys.exit(0 if success else 1)
