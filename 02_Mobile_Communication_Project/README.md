# PRJ-MCOM: Ultra-Low Latency Digital Wireless IEM Transceiver

> [!info] Project Context
> - **Course**: `61ECE314` — Mobile Communications (Winter Semester 2026/2027)
> - **Institution**: Vietnamese-German University (VGU)
> - **Instructor**: Dr. Nguyen Tuan Khanh
> - **Team Trio**: Nguyễn Huỳnh Vân Phương, Quang Thiện, Thùy Tiên
> - **Current Progress**: GATE-1 & GATE-2 Completed (25% across 10 work packages). GATE-3 in progress.

---

## 1. Quickstart for Team Members and AI Agents

If you are using an AI coding assistant (DeepSeek, Claude Code, Cursor, Copilot, ChatGPT, Antigravity) to work on this repository:

1. **Read First**: Open [`AGENT_ONBOARDING_GUIDE.md`](AGENT_ONBOARDING_GUIDE.md) — it contains ready-to-use, task-specific prompts for each project milestone (GATE-3 through GATE-6).
2. **Environment Mandate**: The default terminal `python` on Windows does not contain GNU Radio. **All Python scripts and flowgraphs must run via Radioconda**:
   ```powershell
   & "C:\ProgramData\radioconda\python.exe" <script_name.py>
   ```
3. **Smoke Test Execution**: Verify that the baseband pipeline is working by running:
   ```powershell
   & "C:\ProgramData\radioconda\python.exe" smoke_test_baseband.py
   ```

---

## 2. Repository Structure

```
02_Mobile_Communication_Project/
|-- README.md                                 # This file (Project overview & quickstart)
|-- AGENT_ONBOARDING_GUIDE.md                 # Specialized AI prompts by GATE milestone & guidelines
|-- GEMINI.md                                 # Agent rules, technical scope & sync directives
|-- PROJECT_PLAN_MOBILE_COMM.md               # Course abstract, roadmap gates & team breakdown
|-- WIRELESS_IEM_TRANSCEIVER_MASTER_PLAN.md   # Deep architectural plan, GNU Radio 3.10 block mappings & math
|-- PROJECT_REFERENCES.md                     # Comprehensive AES & IEEE literature matrix
|-- MCOM_Project_Progress_Tracker.xlsx        # Excel progress tracker across all 10 work packages
|-- Reference Papers/                         # 15 local full-text academic papers (AES & IEEE)
|-- generate_test_audio.py                    # Script generating 48 kHz multi-tone test audio
|-- test_audio_48k.wav                        # Generated 3-second reference audio
|-- rx_audio_48k.wav                          # Received audio output from baseband loopback
|-- pcm_framing.py                            # Custom blocks: PCMPacketizerBlock & PCMDepacketizerBlock
|-- baseband_audio_link.grc                   # GNU Radio Companion baseband flowgraph
|-- baseband_audio_link.py                    # Compiled Python flowgraph from GRC
|-- baseband_audio_link_epy_block_*.py        # Generated embedded block definitions
`-- smoke_test_baseband.py                    # Headless test runner (SNR, correlation, sample recovery)
```

---

## 3. Active Technical Gates

| Milestone | Target Date | Technical Focus | Lead Owners | Status |
| :--- | :---: | :--- | :---: | :---: |
| **GATE-1** | 23/09/2026 | Topic Registration & Approval | Vân Phương | Completed |
| **GATE-2** | 18/11/2026 | Baseband Framing + Headless Smoke Flowgraph ($T_{\text{framing}} = 1.0\text{ ms}$) | Vân Phương | Completed |
| **GATE-3** | 24/11/2026 | QPSK Modem, RRC, Symbol Sync (`TED_GARDNER`), Costas, Viterbi FEC + `ber_sweep.py` | Quang Thiện & Thùy Tiên | In Progress |
| **GATE-4** | 30/11/2026 | 2-Branch Rayleigh Fading (`fDTs`), Doppler, Custom Python MRC Block + Multi-Doppler Sweeps | Vân Phương & Thùy Tiên | Upcoming |
| **GATE-5** | 05/12/2026 | LMS Adaptive Equalizer (ISI mitigation), Latency Budget ($T_{\text{alg}} \le 5\text{ ms}$) + QT GUI | Vân Phương & Thùy Tiên | Upcoming |
| **GATE-6** | 08/12/2026 | IEEE XeLaTeX Report, Presentation Slides (20 min), Video Demo, Integration | All 3 Members | Upcoming |
| **DEFENSE** | 09/12/2026 | Official Presentation Slot 1 (Lecture 11 per Dr. Khanh's slide) | All 3 Members | Milestone |

---

## 4. Documentation and Markdown Conventions

All documentation files follow strict Obsidian-compatible clean markdown standards:
- Zero icons and emojis.
- Standard Markdown headings (`#`, `##`, `###`).
- Obsidian callout blocks (`> [!info]`, `> [!note]`, `> [!warning]`).
- Strict LaTeX mathematical notation (`$ ... $` and `$$ ... $$`).
