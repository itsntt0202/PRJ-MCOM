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
| **MCOM-03** | GATE-3 | Digital Modem Transceiver, FEC & Synchronization (`rf_qpsk_link.grc/.py`) | `[IN PROGRESS]` (~80% — FEC Remaining) |
| **MCOM-04** | GATE-3 | Automated Headless BER Sweep Testbed (`ber_sweep.py`, `awgn_ber_qpsk.*`) | `[IN PROGRESS]` (~50% — GNU Radio + FEC Sweep Remaining) |

---

## MCOM-02: Baseband Audio Framing (GATE-2) `[PASS]`

- [x] `pcm_framing.py`: `PCMPacketizerBlock` (48 samples @ 48 kHz -> 104-byte packet with `0xAC62AC62` preamble) & `PCMDepacketizerBlock`.
- [x] `baseband_audio_link.grc` / `.py`: Headless loopback flowgraph.
- [x] `smoke_test_baseband.py`: Verified 100.00% sample recovery, correlation = `1.000000`, SNR = `84.85 dB`, framing delay = `1.000 ms`.

---

## MCOM-03: Digital Modem Transceiver & Synchronization (GATE-3)

### Completed `[PASS]`
- [x] **Deliverable Naming & Compilation**: Created `rf_qpsk_link.grc` and compiled `rf_qpsk_link.py` cleanly via `C:\ProgramData\radioconda\Scripts\grcc.exe` (GNU Radio 3.10.12.0).
- [x] **Core Modem & Sync Blocks**: `digital.constellation_qpsk()`, RRC filters (`sps=4`, `alpha=0.35`, `ntaps=45`), `digital.symbol_sync_cc` (`TED_GARDNER`, `IR_MMSE_8TAP`), `digital.costas_loop_cc` (order 4), and `diff_encoder_bb` / `diff_decoder_bb` (for 90-degree phase ambiguity resolution).
- [x] **GATE-2 Framing Integration (Tx & Rx)**:
  - Removed standalone `multiply_const(127)` / `float_to_char` (8-bit, 16 kHz) path and wired `wavfile_source` (`48000 Hz`) -> `epy_block_packetizer` (104 bytes/packet) -> `packed_to_unpacked_bb(2)` -> QPSK -> `unpacked_to_packed_bb(2)` -> `epy_block_depacketizer` -> `blocks.wavfile_sink` (`48000 Hz`, `FORMAT_PCM_16`).
  - Upgraded `rf_qpsk_link_epy_block_depacketizer.py` with automatic 0..7 bit-shift preamble alignment (`0xAC62AC62`) so no hardcoded `Delay` block is needed.
- [x] **AWGN Baseline & Audio Verification**:
  - Bypassed/separated `selective_fading_model` (GATE-4) and `linear_equalizer` CMA (GATE-5) from the GATE-3 AWGN baseline.
  - Verified `rx_rf_qpsk_48k.wav` (`287,852 bytes`, `48000 Hz`, 16-bit PCM): `99.93%` sample recovery (`143,904 / 144,000`), correlation = `0.999937`, SNR = `38.97 dB`.

### Required Fixes `[TODO]`
- [ ] **Forward Error Correction (FEC)**:
  - Add `fec.cc_encoder_make` (Tx) and `fec.cc_decoder_make` (Rx) with `K=7`, `rate=2` (`R=1/2`), polynomials `[0o171, 0o133]`.
  - Update `sym_rate` to `832000` (`samp_rate = 3328000`) to account for the `R=1/2` code rate and re-verify `rx_rf_qpsk_48k.wav` recovery.
  - *(Note: `digital.symbol_sync_cc` hides the constellation field in GRC when `TED_GARDNER` is selected because Gardner is non-data-aided; no change needed there.)*

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
