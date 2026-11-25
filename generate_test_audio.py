"""
Generate synthetic 48 kHz 16-bit PCM test audio for GNU Radio Baseband Streaming.
Project: PRJ-MCOM (Mobile Communications - VGU Sem5)
"""

import numpy as np
import scipy.io.wavfile as wavfile
import os

SAMPLE_RATE = 48000  # 48 kHz
DURATION = 3.0       # 3 seconds
NUM_SAMPLES = int(SAMPLE_RATE * DURATION)

t = np.linspace(0, DURATION, NUM_SAMPLES, endpoint=False)

# Multi-tone acoustic signal: 440 Hz (A4) fundamental + 880 Hz (A5) harmonic
f1, f2 = 440.0, 880.0
signal = 0.7 * np.sin(2 * np.pi * f1 * t) + 0.3 * np.sin(2 * np.pi * f2 * t)

# Apply gentle 50ms smooth Hann envelope to eliminate onset/offset transients
fade_len = int(0.05 * SAMPLE_RATE)
fade_in = np.sin(np.linspace(0, np.pi / 2, fade_len)) ** 2
fade_out = np.sin(np.linspace(np.pi / 2, 0, fade_len)) ** 2
signal[:fade_len] *= fade_in
signal[-fade_len:] *= fade_out

# Normalize and convert to 16-bit signed integer PCM
signal_int16 = np.int16(signal * 32767)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_wav = os.path.join(out_dir, "test_audio_48k.wav")

wavfile.write(out_wav, SAMPLE_RATE, signal_int16)
print(f"Generated test audio: {out_wav}")
print(f"Sample Rate: {SAMPLE_RATE} Hz | Duration: {DURATION}s | Samples: {NUM_SAMPLES} | Shape: {signal_int16.shape}")
