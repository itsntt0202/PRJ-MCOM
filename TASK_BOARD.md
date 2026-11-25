# PRJ-MCOM: Shared Task & Fix Board

> **Repository**: `PRJ-MCOM` (Code-only root structure, separated from Google Drive docs)  
> **Runtime**: `C:\ProgramData\radioconda\python.exe` (GNU Radio 3.10.12.0, Python 3.12)  
> **Workflow**: Pull latest `main` -> complete assigned task checkboxes below -> verify locally -> commit & push.

---

## Status Overview

| Task ID | Milestone | Scope | Current Status |
| :--- | :---: | :--- | :--- |
| **MCOM-01** | GATE-1 | Project Registration & Specification | `[PASS]` Completed |
| **MCOM-02** | GATE-2 | Baseband Audio Framing & Smoke Test (`pcm_framing.py`, `baseband_audio_link.grc`) | `[PASS]` Completed |
| **MCOM-03** | GATE-3 | Digital Modem Transceiver, FEC & Synchronization (`rf_qpsk_link.grc/.py`) | `[TODO]` Fixes Required |
| **MCOM-04** | GATE-3 | Automated Headless BER Sweep Testbed (`ber_sweep.py`, `awgn_ber_qpsk.*`) | `[TODO]` Fixes Required |

---

## MCOM-02: Baseband Audio Framing (GATE-2) `[PASS]`

- [x] `pcm_framing.py`: `PCMPacketizerBlock` (48 samples @ 48 kHz -> 104-byte packet with `0xAC62AC62` preamble) & `PCMDepacketizerBlock`.
- [x] `baseband_audio_link.grc` / `.py`: Headless loopback flowgraph.
- [x] `smoke_test_baseband.py`: Verified 100.00% sample recovery, correlation = `1.000000`, SNR = `84.85 dB`, framing delay = `1.000 ms`.

---

## MCOM-03: Digital Modem Transceiver & Synchronization (GATE-3)

### Completed `[PASS]`
- [x] `QPSK.grc` compiles cleanly via `C:\ProgramData\radioconda\Scripts\grcc.exe` (GNU Radio 3.10.12.0).
- [x] Core modulation and sync blocks present: `digital.constellation_qpsk()`, RRC filters (`sps=4`, `alpha=0.35`, `ntaps=45`), `digital.symbol_sync_cc` (`TED_GARDNER`, `IR_MMSE_8TAP`), `digital.costas_loop_cc` (order 4).
- [x] Channel ordering fixed in `QPSK.grc` (`RRC Tx -> Fading -> AWGN -> AGC`).

### Required Fixes `[TODO]`
- [ ] **Deliverable Naming**: Save `QPSK.grc` as `rf_qpsk_link.grc` and compile to `rf_qpsk_link.py` via `grcc.exe`.
- [ ] **GATE-2 Framing Integration (Tx & Rx)**:
  - Remove standalone `multiply_const(127)` -> `float_to_char` (8-bit, `audio_rate = 16000`) and `diff_encoder_bb` / `diff_decoder_bb`.
  - Connect Tx: `wavfile_source` (`48000 Hz`) -> `epy_block_packetizer` (GATE-2, 104 bytes/packet) -> bit unpacking -> FEC / QPSK.
  - Connect Rx: FEC / QPSK -> bit packing -> `epy_block_depacketizer` (GATE-2) -> `blocks.wavfile_sink` (`48000 Hz`, `FORMAT_PCM_16`).
- [ ] **Forward Error Correction (FEC)**:
  - Add `fec.cc_encoder_make` (Tx) and `fec.cc_decoder_make` (Rx) with `K=7`, `rate=2` (`R=1/2`), polynomials `[0o171, 0o133]`.
- [ ] **Block Configuration & Scope Alignment**:
  - Fix `digital.symbol_sync_cc` constellation parameter from `digital.constellation_bpsk().base()` to `qpsk_const`.
  - Add `blocks.wavfile_sink` (`48000 Hz`, `FORMAT_PCM_16`) as primary audio output (avoid relying solely on `audio.sink`, which fails on Windows with `open_waveout_device() failed`).
  - Defer/bypass `channels.selective_fading_model` (GATE-4) and `digital.linear_equalizer` with CMA (GATE-5 requires LMS) from the GATE-3 AWGN baseline so timing & phase lock can be verified cleanly on AWGN first (`Eb/N0 >= 8 dB`).

---

## MCOM-04: Automated Headless BER Sweep Testbed (GATE-3)

### Completed `[PASS]`
- [x] `ber_sweep.py` runs headless via `C:\ProgramData\radioconda\python.exe` (500,000 bits/point).
- [x] Uncoded QPSK empirical BER over AWGN matches closed-form theory $P_b = Q(\sqrt{2 E_b / N_0})$ within 0.5 dB across `0–8 dB`.
- [x] Output graphics `awgn_ber_qpsk.png` and `awgn_ber_qpsk.pdf` generated with semi-log axes.

### Required Fixes `[TODO]`
- [ ] **GNU Radio Pipeline Integration**: Replace or supplement the pure-NumPy symbol-level simulation with headless execution of the GNU Radio transceiver chain (`rf_qpsk_link.py` or equivalent headless `gr.top_block` including RRC, Symbol Sync, and Costas Loop).
- [ ] **FEC Coding Gain Measurement**: Add a Convolutional FEC (`K=7, R=1/2`, Viterbi decoding) BER curve alongside the uncoded QPSK curve.
- [ ] **Extended SNR Sweep & Statistical Depth**: Sweep `Eb/N0` from `0` to `12 dB` with at least `100,000` bits (or `>= 100` bit errors) per SNR point to verify coding gain `>= 2.0 dB` at `BER = 1e-4`.
- [ ] **Regenerate Deliverables**: Update `awgn_ber_qpsk.png` and `awgn_ber_qpsk.pdf` to show `Theory`, `Uncoded QPSK (GNU Radio)`, and `Coded QPSK FEC (K=7, R=1/2)`.
