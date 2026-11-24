# MASTER PROJECT PLAN: ULTRA-LOW LATENCY DIGITAL WIRELESS IEM TRANSCEIVER

> **Course**: 61ECE314 — Mobile Communications (Winter Semester 2026/2027)  
> **Institution**: Vietnamese-German University (VGU)  
> **Instructor**: Dr. Nguyễn Tuấn Khanh  
> **Student / Project Lead**: Nguyễn Huỳnh Vân Phương  
> **Project Title**: **Design and Simulation of an Ultra-Low Latency Digital Wireless In-Ear Monitor (IEM) Transceiver with Diversity Reception and Adaptive Equalization over Multipath Fading Channels in GNU Radio**  
> **Core Toolchain**: GNU Radio Companion **3.10.12.0** (`radioconda` @ `C:\ProgramData\radioconda`), **Python 3.12** (bundled), NumPy/SciPy, PyQt5, XeLaTeX  
> **Environment Verified**: 2026-11-14 — GRC + PyQt5 import OK; headless chain measured at ~1.03 Mbit/s. **Always call `C:\ProgramData\radioconda\python.exe`** (system `python` is 3.15.2 without GNU Radio).  
---

## 1. TỔNG QUAN CHIẾN LƯỢC & PHÂN TẦNG ĐỀ TÀI (STRATEGIC ARCHITECTURE)

Đề tài được thiết kế theo đúng định hướng của Thầy Khanh (sử dụng GNU Radio để mô phỏng truyền thông vô tuyến thực tế) và kế thừa nền tảng từ hai bài báo tham khảo trọng tâm:
1. **Networked Audio & Latency Constraints** (*Borgianni et al. - IEEE TNSM 2025*): Bài toán truyền phát âm thanh trực tiếp độ trễ thấp ($< 5\text{ ms}$).
2. **Spatial Diversity & Fading Mitigation** (*Alamouti - IEEE JSAC 1998*): Phân tập thu kết hợp tỉ số cực đại (**Maximal Ratio Combining - MRC**) chống Fading đa đường Rayleigh/Rician.

### Phân Tầng Trọng Tâm Thực Hiện:
* **Tầng Cốt Lõi (Core Telecom — Bắt buộc, 85% nỗ lực)**:
  - Xây dựng Flowgraph GNU Radio hoàn chỉnh từ Audio Source $\rightarrow$ Framing $\rightarrow$ FEC Convolutional $\rightarrow$ QPSK $\rightarrow$ Kênh truyền đa đường (Rayleigh/Rician, Doppler, AWGN) $\rightarrow$ MRC Combiner $\rightarrow$ Đồng bộ Costas/Polyphase $\rightarrow$ LMS Equalizer $\rightarrow$ Viterbi Decoder $\rightarrow$ Audio Sink.
  - Đo đạc định lượng chuẩn viễn thông: Chòm sao Constellation, đường cong $BER$ vs $SNR$, độ trễ End-to-End ($< 5\text{ ms}$).
* **Tầng Mở Rộng (Optional Extensions — Tự chọn, 15% nỗ lực)**:
  - Tích hợp bộ lọc âm học Harman IEM Target Curve hoặc bộ giới hạn biên độ Brickwall Safety Limiter (thực hiện sau khi hệ thống cốt lõi đã chạy ổn định).

---

### 1.1 Scope Lock (chốt 14/11/2026)

Để đảm bảo 30% điểm môn học với 33 ngày còn lại, scope được **đóng băng** như sau:

| Hạng mục | Quyết định |
| :--- | :--- |
| QPSK (Gray-mapped) | Giữ — modulation duy nhất |
| π/4-DQPSK | Cắt — làm 2 modulation sẽ mất cả hai |
| Convolutional FEC K=7, R=1/2 + Viterbi | Giữ — đa thức **171/133** |
| Symbol Sync + Costas Loop | Giữ — phần khó nhất, được ưu tiên thời gian |
| 2-branch Rayleigh + Doppler + MRC | Giữ — core của môn học |
| Linear Equalizer (LMS) | Giữ — nhưng là hạng mục **cắt trước** nếu trễ lịch |
| Harman IEM Target EQ + Brickwall Limiter | Cắt khỏi deliverable chính — chỉ nêu 1 slide "hướng mở rộng" |
| Audio live qua soundcard | Phương án B — `wavfile_sink` + video là bắt buộc, `audio.sink` là tùy chọn |
| RF/SDR thật | Không — kênh mô phỏng thuần túy (cần xác nhận với GVHD) |

---

## 2. KIẾN TRÚC HỆ THỐNG FLOWGRAPH GNU RADIO

```
═════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                   KHỐI PHÁT (WIRELESS IEM TRANSMITTER)
═════════════════════════════════════════════════════════════════════════════════════════════════════════════
   [Audio Source]               [Framing & Sync]              [FEC Encoder]             [Digital Mod]
┌──────────────────┐        ┌──────────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│ WAV File / Micro │ ─────> │ Preamble Sync +      │ ───> │ Convolutional    │ ───> │ QPSK (pi/4 cut)  │
│ 16-bit PCM Audio │        │ Timestamp Header     │      │ Rate 1/2, K=7    │      │ Constellation Map│
└──────────────────┘        └──────────────────────┘      └──────────────────┘      └────────┬─────────┘
                                                                                             │
                                                                                             ▼
                                                                                   [Pulse Shaping Filter]
                                                                                  ┌──────────────────────┐
                                                                                  │ Root Raised Cosine   │
                                                                                  │ Roll-off alpha=0.35  │
                                                                                  └──────────┬───────────┘
                                                                                             │ (Tx Signal)
═════════════════════════════════════════════════════════════════════════════════════════════╪═══════════════
                    MÔ HÌNH KÊNH TRUYỀN VÔ TUYẾN ĐA ĐƯỜNG (MULTIPATH STAGE CHANNEL)          │
═════════════════════════════════════════════════════════════════════════════════════════════╪═══════════════
                                                                                             │
                    ┌────────────────────────────────────────────────────────────────────────┴───────────────────┐
                    ▼ (Nhánh truyền không gian 1 - Rx Ant 1)                                                     ▼ (Nhánh truyền không gian 2 - Rx Ant 2)
┌────────────────────────────────────────────────────────┐               ┌────────────────────────────────────────────────────────┐
│ • Rayleigh / Rician Multipath Fading 1                 │               │ • Rayleigh / Rician Multipath Fading 2                 │
│ • Doppler Shift fd (Nghệ sĩ di chuyển trên sân khấu)   │               │ • Độc lập không gian (Uncorrelated Spatial Path)       │
│ • AWGN Noise Source 1 (Nhiễu nhiệt nền RF)             │               │ • AWGN Noise Source 2 (Nhiễu nhiệt nền RF)             │
└───────────────────────────┬────────────────────────────┘               └───────────────────────────┬────────────────────────────┘
                            │                                                                        │
════════════════════════════╪════════════════════════════════════════════════════════════════════════╪════════
                            │        KHỐI THU PHÂN TẬP & CÂN BẰNG THÍCH NGHI (IEM RECEIVER)          │
════════════════════════════╪════════════════════════════════════════════════════════════════════════╪════════
                            └────────────────────────────────────┬───────────────────────────────────┘
                                                                 ▼
                                                 ┌───────────────────────────────┐
                                                 │    1. MRC (custom PyBlock)    │
                                                 │    (tự viết, không có sẵn)    │
                                                 └───────────────┬───────────────┘
                                                                 │
                                                                 ▼
                                                 ┌───────────────────────────────┐
                                                 │ 2. Matched Filter (Rx RRC)    │
                                                 └───────────────┬───────────────┘
                                                                 │
                                                                 ▼
                                                 ┌───────────────────────────────┐
                                                 │    3. Symbol Sync + Costas    │
                                                 │      TED_GARDNER + Costas     │
                                                 └───────────────┬───────────────┘
                                                                 │
                                                                 ▼
                                                 ┌───────────────────────────────┐
                                                 │       4. Linear EQ (LMS)      │
                                                 │    Triệt tiêu méo trễ ISI     │
                                                 └───────────────┬───────────────┘
                                                                 │
                                                                 ▼
                                                 ┌───────────────────────────────┐
                                                 │    5. FEC cc_decoder (K=7)    │
                                                 └───────────────┬───────────────┘
                                                                 │
                                                                 ▼
                                                 ┌───────────────────────────────┐
                                                 │       6. WAV/Audio Sink       │
                                                 │     + BER & latency probe     │
                                                 └───────────────┬───────────────┘
                                                                 : (Tùy chọn mở rộng)
                                                 ┌ - - - - - - - ┴ - - - - - - - ┐
                                                 │ • Harman Target EQ Filter     │
                                                 │ • Brickwall Safety Limiter     │
                                                 └ - - - - - - - - - - - - - - - ┘
```

---

### 2.1 Block Mapping — Verified trên GNU Radio 3.10.12.0 (2026-11-14)

> [!warning] Sơ đồ ASCII ở §2 chỉ là minh họa khái niệm.** Tên block triển khai thực tế **phải** lấy theo bảng dưới đây. Bảng này được xác minh bằng `dir()` trên bản cài thật **và** bằng một flowgraph chạy thật trên máy — không phải suy đoán.

| Tầng chức năng | Tên trong plan cũ | Block thực tế trong GR 3.10.12.0 | Tham số chốt |
| :--- | :--- | :--- | :--- |
| Điều chế | `QPSK / π/4-DQPSK` | `digital.constellation_qpsk()` + `digital.chunks_to_symbols_bc` | Gray-mapped QPSK; **π/4-DQPSK đã cắt** |
| Lọc phát / thu | RRC α = 0.35 | `filter.firdes.root_raised_cosine` + `filter.interp_fir_filter_ccf` (Tx) / `filter.fir_filter_ccf` (Rx) | `sps = 4`, `taps = 11*sps` |
| Kênh fading | *(plan không nêu block)* | `channels.fading_model(N=8, fDTs=..., LOS=False, K=..., seed=i)` × **2 instance, seed khác nhau** | Map Doppler: xem §4.1 |
| Cộng nhiễu AWGN | `AWGN Noise Source` | `channels.channel_model(noise_voltage, 0, 1.0, [1.0], seed, False)` nối sau mỗi nhánh | `noise_voltage` quét theo SNR |
| **MRC combiner** | "Maximal Ratio Combiner block" | **KHÔNG có block sẵn** → tự viết **Python Block** (`gr.sync_block`) | Genie-aided: `y = conj(h1)*r1 + conj(h2)*r2`, ~20 dòng |
| Đồng bộ timing | **Polyphase Clock Sync** (Không tồn tại) | `digital.symbol_sync_cc(digital.TED_GARDNER, sps, loop_bw, damping, ted_gain, max_dev, osps, cons, digital.IR_MMSE_8TAP, 8)` | `polyphase_clock_sync_cc` và `filter.pfb_clock_sync_ccf` **đều không tồn tại** |
| Đồng bộ pha | Costas Loop | `digital.costas_loop_cc(loop_bw, order=4, use_snr=False)` | Đặt **sau** Symbol Sync |
| Cân bằng thích nghi | **LMS DD Equalizer** (Không tồn tại) | `digital.linear_equalizer(15, 2, True, digital.adaptive_algorithm_lms(cons, mu), False)` | `lms_dd_equalizer_cc` **không tồn tại**; truyền **object** algorithm, **không** `.as_float()` |
| FEC encoder | Convolutional K=7, R=1/2 | `fec.cc_encoder_make(frame_size>0, 7, 2, [0o171, 0o133])` | Đa thức **171/133** — bản cũ **không ghi** |
| FEC decoder | **Viterbi Decoder** | `fec.cc_decoder_make(frame_size>0, 7, 2, [0o171, 0o133])` | `decode_ccsds_27_bb` **không tồn tại** (chỉ có bản encode) |
| Đo BER / chòm sao | QT GUI | `qtgui.const_sink_c` + `qtgui.ber_sink_b` | Có sẵn, dùng trực tiếp |
| Audio ra | Audio Sink | `blocks.wavfile_sink` (**phương án A**) / `audio.sink` (**phương án B**) | `audio.sink` **đã fail** trên máy này: `open_waveout_device() failed` |

#### Bằng chứng đo được trên máy (14/11/2026)

| Kiểm chứng | Kết quả |
| :--- | :--- |
| GNU Radio | **3.10.12.0** — `C:\ProgramData\radioconda` (Python 3.12) |
| GRC + PyQt5 | Import OK; `Scripts\gnuradio-companion.exe` tồn tại |
| Chain modem QPSK→RRC→AWGN→SymbolSync | Chạy headless: 47.980 bit / 0,05 s ≈ **1,03 Mbit/s** (≈ 20× nhu cầu real-time) |
| Fading 2 nhánh Rayleigh + Doppler | Chạy OK; \|h\| = 0,966 / 0,880; **tương quan 0,008** → 2 nhánh độc lập thật |
| Khóa đồng bộ (lock) | **CHƯA lock** trong probe nhanh (BER ≈ 0,49) → **rủi ro #1**, xem §3.1 |
| `audio.sink` | `open_waveout_device() failed` → phải có phương án `wavfile_sink` |

> [!warning] Bẫy môi trường
> `python` mặc định của máy là **3.15.2 và KHÔNG có GNU Radio**. Mọi script phải chạy bằng `C:\ProgramData\radioconda\python.exe`.

---

## 3. LỘ TRÌNH TRIỂN KHAI (CẬP NHẬT THEO LỊCH SLIDE GV 17/11/2026)

> **Cập nhật 17/11/2026**: Lịch thuyết trình Final Project được đối soát chính xác theo Slide bài giảng của Giáo viên (Lecture 0, Slide 8 & 10):
> - **Buổi 11 (Lecture 11 — 09/12/2026)**: Đợt thuyết trình Final Project 1 (20 phút thuyết trình, 10 phút Q&A).
> - **Buổi 12 (Lecture 12 — 16/12/2026)**: Đợt thuyết trình Final Project 2 (Buổi kết thúc môn học).
> - **Chiến lược an toàn tuyệt đối**: Toàn bộ code GNU Radio, Báo cáo XeLaTeX và Slide thuyết trình phải **Code & Report Freeze vào 08/12/2026** để sẵn sàng báo cáo ngay tại Buổi 11. Nếu nhóm được phân lịch vào Buổi 12 (16/12/2026), khoảng thời gian 09–16/12 sẽ là **Extended Defense Buffer** để tối ưu bài thuyết trình.

| Giai đoạn | Thời gian | Nhiệm vụ cốt lõi | Sản phẩm bàn giao | Gate | Trạng thái |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Phase 1: Registration & Spec** | 15/09 – 23/09/2026 | Đăng ký đề tài; viết spec (Vân Phương) | Đề tài được duyệt; Spec v1.0 | GATE-1 | Completed |
| **Phase 2: Baseband & Framing** | 14/11 – 18/11/2026 | Dựng luồng WAV/Mic, packet framing (pcm_framing.py), smoke test headless (Vân Phương) | Flowgraph v1.0 (.grc) + script chạy headless | GATE-2 | Completed |
| **Phase 3: Modulation, Sync & FEC** | 19/11 – **24/11**/2026 | QPSK + RRC; Symbol Sync + Costas; FEC CC 171/133 (Quang Thiện) + **testbed `ber_sweep.py` tự động** (Thùy Tiên) | Flowgraph v2.0 + `ber_sweep.py` + đường BER(AWGN) vs lý thuyết | GATE-3 | In Progress |
| **Phase 4: Fading & Diversity** | 25/11 – **30/11**/2026 | 2 nhánh Rayleigh + Doppler (fDTs); **MRC Python Block** (Vân Phương) + **Doppler sweep & BER curve** (Thùy Tiên) | Flowgraph v3.0 + MRC Python Block + BER curves | GATE-4 | Upcoming |
| **Phase 5: Equalization, Latency & GUI** | **01/12** – 05/12/2026 | Linear Equalizer (LMS); **latency probe** <= 5 ms (Vân Phương) + **QT Dashboard & test audio** (Thùy Tiên) | Flowgraph v4.0 + Bảng latency budget + QT Dashboard | GATE-5 | Upcoming |
| **Report chạy song song** | **25/11** – 05/12/2026 | Viết dần chương lý thuyết + giải thuật vào XeLaTeX IEEE (Vân Phương) | Bản nháp report >= 70% | — | Upcoming |
| **Phase 6: Documentation & Slide** | 06/12 – 08/12/2026 | Ráp hoàn chỉnh report IEEE (Vân Phương); slide 20 phút + video demo A/B (Thùy Tiên); tích hợp demo (Quang Thiện) | PDF report + slide 20' + video demo | GATE-6 | Upcoming |
| **BUFFER & TỔNG DUYỆT** | **08/12/2026** | **Code freeze 08/12.** Tổng duyệt demo 2 lần, kiểm tra âm thanh và máy chiếu trước Buổi 11 | Bản demo & slide sẵn sàng bảo vệ | — | Buffer |
| **DEFENSE SLOT 1 (Lec 11)** | **09/12/2026** | **Thuyết trình Buổi 11 theo Slide GV** (Ca chiều 13:00 - 16:15) | Trình bày 20' + Q&A 10' | — | Milestone |
| **DEFENSE SLOT 2 (Lec 12)** | **16/12/2026** | **Thuyết trình Buổi 12 theo Slide GV** (Ca chiều 13:00 - 16:15) | Trình bày 20' + Q&A 10' | — | Milestone |

### 3.1 Rủi ro & Giảm thiểu

| # | Rủi ro | Xác suất | Sát thương | Giảm thiểu |
| :---: | :--- | :---: | :---: | :--- |
| 1 | **Không lock được Symbol Sync + Costas** trước 24/11 | Cao | Chí mạng | Thêm **preamble correlation** để frame sync trước khi vào TED; nếu vẫn fail → `digital.constellation_receiver_cb` (đơn giản hơn nhiều) |
| 2 | Demo âm thanh live thất bại trước hội đồng | **Đã xảy ra** | Chí mạng | Phương án A bắt buộc: `wavfile_sink` + video quay sẵn; test loa trên **đúng máy thuyết trình** trước 12/12 |
| 3 | MRC không có block sẵn | Cao | Cao | MRC genie-aided ~20 dòng NumPy (dùng trực tiếp h1, h2) — **không** cần ước lượng kênh |
| 4 | Hết thời gian | Trung bình | Cao | Đã cắt π/4-DQPSK; Harman EQ + limiter cắt khỏi deliverable chính |
| 5 | Nhầm `python` 3.15 vs radioconda 3.12 | Chắc chắn | Trung bình | Luôn gọi `C:\ProgramData\radioconda\python.exe` |

**Phân công lại theo trọng tâm kỹ thuật cốt lõi (Cập nhật 18/11/2026):**

- **Vân Phương** *(Project Lead & Cốt lõi Viễn thông Di động)*: Hoàn thành Baseband (GATE-2), chủ trì triển khai **Kênh Fading 2 nhánh + viết MRC Python Block (GATE-4)**, tích hợp thuật toán **LMS Equalizer triệt ISI (GATE-5)**, đo kiểm **Latency Budget ($T_{\text{alg}} \approx 3.4\text{ ms} \le 5.0\text{ ms}$)**, và chủ trì biên soạn Báo cáo XeLaTeX IEEE.
- **Quang Thiện** *(Modem Thu-Phát số & Giao diện)*: QPSK Gray-mapped + RRC, giải quyết **Symbol Sync (`TED_GARDNER`) + Costas Loop (rủi ro #1 — dồn lực, GATE-3)**, FEC Convolutional + Viterbi `cc_decoder`, **script sweep BER tự động headless**, và thiết kế **QT GUI Dashboard** (GATE-5).
- **Thùy Tiên** *(Đo kiểm thực nghiệm, Media & Trình diễn)*: Chạy sweep thực nghiệm và vẽ toàn bộ **biểu đồ phân tích so sánh BER vs SNR** (1 nhánh vs 2 nhánh MRC; các dải Doppler; có/không FEC), kiểm thử âm thanh `wavfile_sink` / `audio.sink`, **thiết kế Slide thuyết trình 20 phút** và **quay Video Demo chính thức** (GATE-6).

---

## 4. CƠ SỞ TOÁN HỌC & CHỈ SỐ ĐỊNH LƯỢNG (REVISED 14/11/2026)

### 4.1 Mô hình kênh Fading & ánh xạ Doppler sang `fading_model`

Tín hiệu băng gốc tại nhánh thu $i \in \{1,2\}$:

$$
r_i(t) = h_i(t)\,s(t) + n_i(t), \qquad h_i(t) = \sum_{k=1}^{N_p} a_{i,k}\, e^{-j 2\pi f_c \tau_{i,k}}\, e^{j 2\pi f_{d,i,k} t}
$$

với tần số Doppler cực đại do ca sĩ di chuyển vận tốc $v$:

$$
f_{d,\max} = \frac{v}{c}\, f_c
$$

> [!warning] Điểm mà bản plan cũ thiếu
> `channels.fading_model` **không nhận Hz**, nó nhận **`fDTs`** (tần số Doppler đã chuẩn hóa theo chu kỳ ký hiệu). Phải chốt $f_c$ rồi quy đổi:

| Đại lượng | Ký hiệu | Giá trị chốt (kịch bản mặc định) | Cách tính |
| :--- | :---: | :--- | :--- |
| Tần số sóng mang | $f_c$ | **2.4 GHz** (băng ISM) | giả định hệ thống IEM không dây |
| Vận tốc ca sĩ | $v$ | 1.5 m/s (đi lại trên sân khấu) | — |
| Doppler cực đại | $f_{d,\max}$ | **12 Hz** | $v f_c / c$ |
| Tần số lấy mẫu audio | $f_s$ | 48 kHz | — |
| Hệ số nội suy | `sps` | 4 | 48 kHz / 12 ksym/s |
| Chu kỳ ký hiệu | $T_{sym}$ | 83.33 µs | `sps` / $f_s$ |
| **Tham số truyền cho block** | **`fDTs`** | **≈ 1,0 × 10⁻³** | $f_{d,\max} \cdot T_{sym}$ |

**Dải quét Doppler khi đo:** `fDTs` ∈ {1e-4, 1e-3, 1e-2} tương ứng $v$ ≈ 0.15 / 1.5 / 15 m/s.
**Cấu hình block:** `channels.fading_model(N=8, fDTs=fDTs, LOS=False, K=4.0, seed=1)` cho nhánh 1 và `seed=2` cho nhánh 2. Đã kiểm chứng: 2 nhánh cho tương quan biên độ **0.008** (độc lập — điều kiện tiên quyết để MRC có nghĩa).

### 4.2 MRC & BER lý thuyết *(đã sửa hệ số)*

Nhiễu sau kết hợp MRC (genie-aided weights $w_i = h_i^{*}$):

$$
\gamma_{\text{MRC}} = \sum_{i=1}^{2} \gamma_i = \frac{E_s}{N_0}\left(|h_1|^2 + |h_2|^2\right)
$$

BER trung bình của QPSK Gray-mapped qua kênh Rayleigh có MRC $L$ nhánh:

$$
P_b = \mu^{L} \sum_{l=0}^{L-1} \binom{L-1+l}{l}\,(1-\mu)^{l},
\qquad \mu = \sqrt{\frac{\bar{\gamma}}{1+\bar{\gamma}}}
$$

Tại SNR cao, suy ra dạng tiệm cận bậc phân tập $L$:

$$
P_b \;\approx\; \binom{2L-1}{L}\left(\frac{1}{4\bar{\gamma}}\right)^{L}
\quad\Longrightarrow\quad
P_b^{L=2} \;\approx\; \mathbf{3}\left(\frac{1}{4\bar{\gamma}}\right)^{2}
$$

> [!note] Đính chính công thức
> bản cũ ghi $P_b^{\text{MRC}} \approx \left(\frac{1}{4\bar{\gamma}}\right)^2$ — **đúng về bậc suy giảm $L=2$ nhưng thiếu hệ số 3**. Dùng công thức đầy đủ ở trên; đây là công thức sẽ vẽ chồng lên BER mô phỏng.

**Tăng ích kỳ vọng:** array gain $10\log_{10} 2 = 3$ dB **cộng** diversity gain; đo tại $BER = 10^{-3}$ kỳ vọng **> 3 dB** so với 1 nhánh.

> [!note] Ghi chú phạm vi lý thuyết
> hệ thống dùng **receive diversity (MRC)**. Alamouti 1998 là **transmit diversity (STBC)** — *không* được triển khai, chỉ dùng làm bối cảnh "hướng mở rộng". Không trình bày Alamouti như một phần kiến trúc.

### 4.3 Thuật toán cân bằng thích nghi LMS

Sai số và cập nhật trọng số tại mỗi chu kỳ ký hiệu:

$$
e(n) = d(n) - \mathbf{w}^{H}(n)\,\mathbf{x}(n),
\qquad
\mathbf{w}(n+1) = \mathbf{w}(n) + \mu\, e^{*}(n)\,\mathbf{x}(n)
$$

Điều kiện hội tụ: $0 < \mu < \dfrac{2}{N\,\overline{|x|^2}}$ với $N$ = số tap. Trong GNU Radio:

```python
alg = digital.adaptive_algorithm_lms(cons.base(), mu)   # mu = 0.001 .. 0.01
eq  = digital.linear_equalizer(num_taps=15, sps=2, adapt=True, alg=alg, diff=False)
```

> [!note] Lưu ý kỹ thuật
> `digital.lms_dd_equalizer_cc` **không tồn tại** trong 3.10.12 — dùng `linear_equalizer` như trên, và **không** gọi `.as_float()`.

### 4.4 ⏱️ Định nghĩa lại "Độ trễ < 5 ms" *(thay đổi quan trọng)*

> [!warning] Giới hạn đo đạc thực tế
> tuyên bố "$T_{\text{total}} \le 5$ ms end-to-end" là **không thể kiểm chứng** trong mô phỏng và **không thể đạt** trên Windows, vì buffer WASAPI/PortAudio điển hình **10–30 ms** đã vượt ngân sách trước khi tính DSP. Thực tế `audio.sink` **đã fail** trên máy (`open_waveout_device()`).

**Định nghĩa mới — "Simulation-Domain Algorithmic Latency":**

$$
T_{\text{alg}} = T_{\text{framing}} + T_{\text{FEC}} + T_{\text{RRC}} + T_{\text{sync}} + T_{\text{EQ}} + T_{\text{buf}}
\;\;\le\; 5.0\ \text{ms}
\qquad \text{(không tính soundcard I/O)}
$$

**Ngân sách latency (kịch bản: $f_s$ = 48 kHz, `sps` = 4, $T_{sym}$ = 83.33 µs):**

| Thành phần | Công thức | Giá trị |
| :--- | :--- | ---: |
| $T_{\text{framing}}$ | $N_{frame}/f_s$, $N_{frame}=48$ mẫu (1 ms audio) | 1.00 ms |
| $T_{\text{FEC}}$ | bộ nhớ mã $K-1$ ký hiệu | 0.25 ms |
| $T_{\text{RRC}}$ | $2 \cdot (N_{taps}-1)/2 / f_s$, $N_{taps}=44$ | 0.90 ms |
| $T_{\text{sync}}$ | 2 ký hiệu (trạng thái ổn định) | 0.17 ms |
| $T_{\text{EQ}}$ | $(N_{taps}-1)/2 \cdot T_{sym}$, $N_{taps}=15$ | 0.58 ms |
| $T_{\text{buf}}$ | `noutput_items` nội bộ GNU Radio | 0.50 ms |
| **Tổng** | | **≈ 3.4 ms (< 5.0 ms)** |

**Hai cách đo — phải có cả hai trong báo cáo:**

1. **Giải tích:** bảng trên (chứng minh *thiết kế* đạt).
2. **Thực nghiệm trong flowgraph:** chèn **1 mẫu impulse** ở Tx, đo vị trí đỉnh tại Rx → tổng group delay; **và** dùng stream tag (`tag.offset`) tại Tx/Rx, latency $= (n_{out} - n_{in})/f_s$.

> [!tip] Khi bảo vệ
> phải nói rõ *"đây là latency miền mô phỏng, loại trừ soundcard I/O"*. Nếu hội đồng hỏi "5 ms thật hay không" → trả lời trung thực + trình bày bảng budget. Đây là điểm ăn điểm, không phải điểm chết — miễn là định nghĩa trước.

### 4.5 Tiêu chí nghiệm thu (đo được)

| # | Tiêu chí | Ngưỡng | Cách đo |
| :---: | :--- | :--- | :--- |
| **A1** | BER(AWGN) khớp lý thuyết QPSK | lệch **< 1 dB** tại $BER = 10^{-4}$, SNR 0…20 dB | `ber_sweep.py` + công thức §4.2 |
| **A2** | Coding gain của FEC (K=7, R=1/2) | **≥ 2 dB** tại $BER = 10^{-4}$ | So sánh có/không FEC |
| **A3** | Tăng ích MRC (2 nhánh vs 1 nhánh) | **≥ 3 dB** tại $BER = 10^{-3}$ | Quét `fDTs` ∈ {1e-4, 1e-3, 1e-2} |
| **A4** | Triệt ISI của LMS | chòm sao QPSK mở lại rõ khi $\tau_{delay} > 0.5\,T_{sym}$ | Ảnh constellation trước/sau EQ |
| **A5** | Latency thuật toán | **≤ 5.0 ms** theo §4.4 | Bảng budget + impulse/tag |
| **A6** | Demo âm thanh | WAV vào → WAV ra, **nghe được**, có/không MRC | `wavfile_sink` + video |

---

## 5. TÀI LIỆU THAM KHẢO & ÁNH XẠ CHUYÊN ĐỀ (REFERENCES)

1. **Digital Communications (5th Edition)** — John G. Proakis & Masoud Salehi: Chương 13 (Fading Channels), Chương 9 (Carrier & Symbol Synchronization).
2. **Wireless Communications** — Andrea Goldsmith: Chương 3 (Statistical Multipath Channel Models), Chương 6 & 7 (Diversity & Equalization).
3. **Fundamentals of Wireless Communication** — David Tse & Pramod Viswanath: Chương 2 & 3 (Capacity of Wireless Channels, Diversity Techniques).
4. **Reference Paper 1**: S. M. Alamouti, *"A Simple Transmit Diversity Technique for Wireless Communications,"* IEEE JSAC, 1998.
5. **Reference Paper 2**: L. Borgianni et al., *"A Comprehensive Evaluation of Networked Music Performance Using LEO Satellite Internet,"* IEEE TNSM, 2025.
6. **Chi tiết danh mục mở rộng**: Xem tại [`PROJECT_REFERENCES.md`](PROJECT_REFERENCES.md).