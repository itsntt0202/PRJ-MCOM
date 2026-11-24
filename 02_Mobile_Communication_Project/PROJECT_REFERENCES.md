# TOÀN TẬP TÀI LIỆU THAM KHẢO & MA TRẬN ÁNH XẠ KỸ THUẬT (MASTER REFERENCES & TECHNICAL SUPPORT MATRIX)

> **Dự án**: **Design and Simulation of an Ultra-Low Latency Digital Wireless In-Ear Monitor (IEM) Transceiver with Diversity Reception and Adaptive Equalization over Multipath Fading Channels in GNU Radio**  
> **Môn học**: 61ECE314 — Mobile Communications (Winter Semester 2026/2027)  
> **Cơ sở đào tạo**: Trường Đại học Việt Đức (VGU)  
> **Sinh viên chủ trì**: Nguyễn Huỳnh Vân Phương  
> **Thư mục Tệp PDF Gốc**: [`Projects/Reference Papers/`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers) & [`Lecture files/Reference Papers/`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Lecture%20files/Reference%20Papers)

---

## BẢNG ÁNH XẠ TỆP TIN PDF TOÀN VĂN SẴN CÓ TRÊN Ổ ĐĨA (LOCAL PDF MAPPING)

Dưới đây là bảng tra cứu trực tiếp toàn bộ các tệp tin **PDF toàn văn (Full-text Papers)** đã được tải về lưu trữ tại thư mục dự án `Projects/Reference Papers/` và `Lecture files/Reference Papers/`, được phân loại theo từng chủ đề AES và mô-đun chức năng hỗ trợ:

| STT | Chủ đề AES / Nguồn | Tên Bài báo Khoa học & Tác giả | Mức độ | Tệp tin PDF Toàn văn Nội bộ (Local Clickable Link) | Mô-đun GNU Radio & Vai trò Hỗ trợ |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **1** | **Chủ đề 1: Audio Coding** | **APT-X00 Sub-Band ADPCM Coder** *(Smyth & Smyth, 1989)* | ⭐️⭐️⭐️ | [`APT-X00__A_Low-Delay,_Low_Bit-Rate,_Sub-Band_ADPCM_Audio_Coder_for_Broadcasting.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/APT-X00__A_Low-Delay%2C_Low_Bit-Rate%2C_Sub-Band_ADPCM_Audio_Coder_for_Broadcasting.pdf) | **Khối Nén Audio Tx**: Thuật toán nén ADPCM độ trễ $< 1.5\text{ ms}$, nén 4:1 ($1.536\text{ Mbps} \rightarrow 384\text{ kbps}$). |
| **2** | **Chủ đề 1: Audio Coding** | **AC-2 & AC-3 Transform Coding** *(Fielder & Bosi, 1994)* | ⭐️⭐️ | [`AC-2_and_AC-3__Low-Complexity_Transform-Based_Audio_Coding.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/AC-2_and_AC-3__Low-Complexity_Transform-Based_Audio_Coding.pdf) | **Khối Đối chứng**: Phân tích ngân hàng bộ lọc TDAC và cơ chế phân bổ bit động của chuẩn Dolby. |
| **3** | **Chủ đề 1: Audio Coding** | **New Developments in Low Bit-rate Coding** *(Rumsey, 2005)* | ⭐️⭐️⭐️ | [`New_Developments_In_Low_Bit-rate_Coding.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/New_Developments_In_Low_Bit-rate_Coding.pdf) | **Khối Bù Mất Gói (PLC)**: Thuật toán nội suy dạng sóng để triệt tiêu tiếng nổ khi sóng bị fade sâu. |
| **4** | **Chủ đề 2: Headphones** | **Harman In-Ear Target Curve (Part 1)** *(Olive et al., 2017)* | ⭐️⭐️⭐️ | [`A_Statistical_Model_that_Predicts_Listeners’_Preference_Ratings_of_In-Ear_Headphones__Part_1—Listening_Test_Results_and_Acoustic_Measurements.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/A_Statistical_Model_that_Predicts_Listeners%E2%80%99_Preference_Ratings_of_In-Ear_Headphones__Part_1%E2%80%94Listening_Test_Results_and_Acoustic_Measurements.pdf) | **Khối Lọc Âm học IEM**: Đo đạc thực nghiệm xác lập đường cong mục tiêu tối ưu cho tai nghe In-Ear. |
| **5** | **Chủ đề 2: Headphones** | **Harman In-Ear Target Curve (Part 2)** *(Olive et al., 2017)* | ⭐️⭐️⭐️ | [`A_Statistical_Model_that_Predicts_Listeners’_Preference_Ratings_of_In-Ear_Headphones__Part_2—Development_and_Validation_of_the_Model.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/A_Statistical_Model_that_Predicts_Listeners%E2%80%99_Preference_Ratings_of_In-Ear_Headphones__Part_2%E2%80%94Development_and_Validation_of_the_Model.pdf) | **Khối Lọc Âm học IEM**: Mô hình thống kê dự đoán điểm ưa chuộng âm thanh dùng thiết kế bộ lọc FIR/IIR. |
| **6** | **Chủ đề 2: Headphones** | **Headphone Target Equalization** *(Struck & Temme, 2015)* | ⭐️⭐️⭐️ | [`Headphone_Response__Target_Equalization_Trade-offs_and_Limitations.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Headphone_Response__Target_Equalization_Trade-offs_and_Limitations.pdf) | **Khối Bộ lọc Bù DSP**: Phân tích đánh đổi giữa Free-field, Diffuse-field và buồng kín ống tai. |
| **7** | **Chủ đề 2: Headphones** | **A Self-Calibrating Earphone** *(Backman et al. - Hefio, 2017)* | ⭐️⭐️⭐️ | [`A_Self-Calibrating_Earphone.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/A_Self-Calibrating_Earphone.pdf) | **Khối Cân chỉnh Thích nghi**: Ước lượng hàm truyền âm học cửa tai - màng nhĩ để tự động tạo bộ lọc bù. |
| **8** | **Chủ đề 3: Sound Reinforce** | **Psychoacoustics in Live Sound** *(Ahnert et al., 2007)* | ⭐️⭐️⭐️ | [`Psychoacoustics_in_Sound_Reinforcement_and_PA_Design.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Psychoacoustics_in_Sound_Reinforcement_and_PA_Design.pdf) | **Khối Đặc tả Trễ Hệ thống**: Ràng buộc độ trễ $< 4.5\text{ ms}$ để tránh hiện tượng lọc lược (*comb filtering*). |
| **9** | **Chủ đề 3: Sound Reinforce** | **Live Sound System Optimization** *(Rumsey, 2015)* | ⭐️⭐️⭐️ | [`Live_Sound_System_Optimization.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Live_Sound_System_Optimization.pdf) | **Khối Môi trường Sân khấu**: Tối ưu hóa phân bố trường sóng và kiểm soát can nhiễu đa nguồn. |
| **10** | **Chủ đề 4: Audio Network** | **Flexilink Low Latency Live Audio** *(Wang & Fischer, 2013)* | ⭐️⭐️⭐️ | [`Flexilink__A_Unified_Low_Latency_Network_Architecture_for_Multichannel_Live_Audio.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Flexilink__A_Unified_Low_Latency_Network_Architecture_for_Multichannel_Live_Audio.pdf) | **Khối Đóng gói Micro-Packets**: Cấu trúc khung tin siêu nhỏ loại bỏ độ trễ hàng đợi $< 1\text{ ms}$. |
| **11** | **Chủ đề 4: Audio Network** | **Redundancy Optimization** *(Heinzmann, 2012)* | ⭐️⭐️⭐️ | [`Redundancy_Optimization_for_Networked_Audio_Systems.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Redundancy_Optimization_for_Networked_Audio_Systems.pdf) | **Khối Dự phòng Gói tin**: Truyền trùng lặp gói (*Packet Duplication*) chống mất gói mà không cần ARQ. |
| **12** | **Chủ đề 4: Audio Network** | **Latency Issues in Audio Networking** *(Fonseca, 2005)* | ⭐️⭐️⭐️ | [`Latency_Issues_in_Audio_Networking.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Latency_Issues_in_Audio_Networking.pdf) | **Khối Phân tích Độ trễ**: Phân rã mô hình ngân sách độ trễ (*Latency Budget*) từng phân đoạn. |
| **13** | **Chủ đề 5: Hearing Safety** | **Do In-Ear Monitors Protect Hearing?** *(Nykänen et al., 2017)* | ⭐️⭐️⭐️ | [`Do_In-Ear_Monitors_Protect_Musicians’_Hearing_.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Do_In-Ear_Monitors_Protect_Musicians%E2%80%99_Hearing_.pdf) | **Khối Brickwall Safety Limiter**: Khống chế mức đỉnh áp suất âm $< 0\text{ dBFS}$ chống sốc âm học cho ca sĩ. |
| **14** | **Chủ đề 6: Quality Prediction** | **PEAQ ITU-R BS.1387 Standard** *(Thiede et al., 2000)* | ⭐️⭐️⭐️ | [`PEAQ_-_The_ITU_Standard_for_Objective_Measurement_of_Perceived_Audio_Quality.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/PEAQ_-_The_ITU_Standard_for_Objective_Measurement_of_Perceived_Audio_Quality.pdf) | **Khối Script QA Benchmark**: Tiêu chuẩn đo lường chất lượng âm thanh khách quan tính điểm ODG ($0$ đến $-4$). |
| **15** | **Chủ đề 6: Quality Prediction** | **POLQA ITU-T P.863 Standard** *(Beerends et al., 2013)* | ⭐️⭐️⭐️ | [`Perceptual_Objective_Listening_Quality_Assessment_(POLQA),_The_Third_Generation_ITU-T_Standard_for_End-to-End_Speech_Quality_Measurement_Part_II—Perceptual_Model.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Perceptual_Objective_Listening_Quality_Assessment_%28POLQA%29%2C_The_Third_Generation_ITU-T_Standard_for_End-to-End_Speech_Quality_Measurement_Part_II%E2%80%94Perceptual_Model.pdf) | **Khối Đánh giá Kênh Jitter**: Chuẩn đo lường chất lượng âm thanh thế hệ 3 bù trễ thời gian động (*Time Warping*). |
| **16** | **Lecture Reference 1** | **A Simple Transmit Diversity (Alamouti)** *(S. Alamouti, 1998)* | ⭐️⭐️⭐️ | [`reference paper 1 A Simple Transmit Diversity Technique for Wireless Communications IEEE 1998.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Lecture%20files/Reference%20Papers/reference%20paper%201%20A%20Simple%20Transmit%20Diversity%20Technique%20for%20Wireless%20Communications%20IEEE%201998.pdf) | **Khối Phân tập Phát STBC**: Kỹ thuật phân tập phát 2 Tx kinh điển trong bài giảng Thầy Khanh. |
| **17** | **Lecture Reference 2** | **Networked Music Performance (Starlink)** *(2023)* | ⭐️⭐️ | [`A_Comprehensive_Evaluation_of_Networked_Music_Performance_Using_LEO_Satellite_Internet_The_Starlink_Use_Case.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Lecture%20files/Reference%20Papers/A_Comprehensive_Evaluation_of_Networked_Music_Performance_Using_LEO_Satellite_Internet_The_Starlink_Use_Case.pdf) | **Khối Phân tích Trễ Mạng**: Đánh giá trễ truyền dẫn âm thanh trình diễn nhạc thời gian thực. |

---

## HỆ THỐNG PHÂN LOẠI MỨC ĐỘ QUAN TRỌNG (IMPORTANCE RATING)

* ⭐️⭐️⭐️ **Mức độ 1: Cốt lõi Trọng tâm (High / Core Implementation)**: Tài liệu trực tiếp định hình thuật toán và xây dựng các khối xử lý chính trong Flowgraph GNU Radio (ví dụ: Khối nén ADPCM độ trễ thấp, Khối phân tập 2 ăng-ten MRC, Khối cân bằng thích nghi LMS, Khối nắn âm học Harman IEM, Khối bảo vệ thính lực Peak Limiter, Khối script đo điểm PEAQ).
* ⭐️⭐️ **Mức độ 2: Bổ trợ Kỹ thuật Quan trọng (Medium / Direct Technical Support & Parameterization)**: Cung cấp tham số thực nghiệm, mô hình hóa kênh fading đa đường sân khấu, cơ chế bù mất gói PLC, đóng gói micro-packets, ràng buộc độ trễ thính giác.
* ⭐️ **Mức độ 3: Nền tảng Tham chiếu & Bối cảnh Học thuật (Low / Academic Context & Literature Survey)**: Khảo sát tổng quan, cơ sở lý thuyết rộng và nghiên cứu đối chứng mở rộng trong Báo cáo Kỹ thuật Cuối kỳ.

---

## I. NỀN TẢNG GIÁO TRÌNH HÀN LÂM CHUẨN (TEXTBOOK FOUNDATIONS)

### 1. Fundamentals of Wireless Communication [⭐️⭐️⭐️]
* **Tác giả**: David Tse và Pramod Viswanath (Cambridge University Press, 2005).
* **Mô-đun được hỗ trợ trong dự án**:
  * **Chương 2 (Mô hình hóa Kênh truyền Vô tuyến Đa đường)**: Làm cơ sở toán học thiết lập khối mô phỏng kênh truyền *Rayleigh & Rician Fading*, tính toán độ trải trễ đa đường ($T_d$), băng thông kết hợp ($W_c \approx \frac{1}{2 T_d}$), và độ dịch tần Doppler ($f_d = \frac{v}{\lambda}$) khi ca sĩ di chuyển trên sân khấu.
  * **Chương 3 (Kỹ thuật Phân tập Thu & Phát)**: Cơ sở lý thuyết thiết kế khối phân tập thu 2 ăng-ten **Maximal Ratio Combining (MRC)** với tỉ số tín hiệu trên nhiễu tối ưu $\gamma_{\text{MRC}} = \gamma_1 + \gamma_2$, giảm xác suất lỗi bit từ bậc $\mathcal{O}(1/\gamma)$ xuống bậc $\mathcal{O}(1/\gamma^2)$.

### 2. Digital Communications (5th Edition) [⭐️⭐️⭐️]
* **Tác giả**: John G. Proakis và Masoud Salehi (McGraw-Hill, 2008).
* **Mô-đun được hỗ trợ trong dự án**:
  * **Chương 12 (Điều chế Băng gốc Số & Lọc Định hình Xung)**: Thiết kế bộ điều chế QPSK/$\pi/4$-DQPSK, ánh xạ chòm sao (*Constellation Mapping*) và bộ lọc phối hợp Cosine nâng căn (*Root Raised Cosine - RRC*) với hệ số dốc $\alpha = 0.35$ để triệt tiêu nhiễu ISI.
  * **Chương 13 & 14 (Cân bằng Kênh Thích nghi & Mã hóa Kênh)**: Xây dựng thuật toán cân bằng kênh thích nghi **LMS (Least Mean Squares)** và bộ giải mã **Viterbi (Trellis Decoding)** cho mã xoắn *Convolutional Code (Rate 1/2, K=7)* để khôi phục chuỗi bit bị méo do dội sóng.

### 3. Wireless Communications (1st Edition) [⭐️⭐️]
* **Tác giả**: Andrea Goldsmith (Cambridge University Press, 2005).
* **Mô-đun được hỗ trợ trong dự án**:
  * **Chương 3, 6, 10**: Đánh giá dung lượng kênh và xác suất dừng (*Outage Probability*) trong môi trường fading phẳng và fading chọn lọc tần số.

### 4. Mobile Communication Systems for Private Networks [⭐️⭐️]
* **Tác giả**: Srinivasan Balasubramanian và Michael D. Thelander (Artech House, 2023).
* **Mô-đun được hỗ trợ trong dự án**:
  * **Chương 4, 5**: Thiết kế mạng vô tuyến chuyên dụng (Private Wireless Networks), quản lý băng tần và tối ưu hóa chất lượng dịch vụ QoS cho các ứng dụng âm thanh thời gian thực.

---

## II. CHỦ ĐỀ AES 1: MÃ HÓA ÂM THANH (AUDIO CODING)
> Nguồn chính thức: [https://aes.org/audio-topics/audio-coding/](https://aes.org/audio-topics/audio-coding/)

### 1. Danh mục Toàn bộ 18 Bài báo Khoa học & Bài báo Chuyên đề

1. **APT-X00: A Low-Delay, Low Bit-Rate, Sub-Band ADPCM Audio Coder for Broadcasting** [⭐️⭐️⭐️]
   * **Tác giả**: Mike Smyth, Stephen Smyth (AES Convention 86, 1989) — [elib=5400](https://aes.org/publications/elibrary-page/?id=5400).
   * **Tệp PDF Toàn văn Nội bộ**: [`APT-X00__A_Low-Delay,_Low_Bit-Rate,_Sub-Band_ADPCM_Audio_Coder_for_Broadcasting.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/APT-X00__A_Low-Delay%2C_Low_Bit-Rate%2C_Sub-Band_ADPCM_Audio_Coder_for_Broadcasting.pdf)
   * **Phân tích kỹ thuật**: Nén âm thanh 4 băng con phi biến đổi (*non-transform sub-band coding*) kết hợp lượng tử hóa vi sai thích nghi (ADPCM). Xử lý theo từng mẫu đơn lẻ mà không cần tích lũy khung MDCT lớn.
   * **Mô-đun hỗ trợ**: **Khối Nén Âm thanh Thời gian thực (Tx Audio Codec)**. Đạt độ trễ thuật toán siêu thấp **$< 1.5\text{ ms}$**, giảm bitrate từ $1.536\text{ Mbps}$ xuống $384\text{ kbps}$ để truyền qua kênh vô tuyến.

2. **New Developments in Low Bit-rate Coding** [⭐️⭐️⭐️]
   * **Tác giả**: Ban Biên tập AES / Francis Rumsey (JAES, 2005) — [elib=13410](https://aes.org/publications/elibrary-page/?id=13410).
   * **Tệp PDF Toàn văn Nội bộ**: [`New_Developments_In_Low_Bit-rate_Coding.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/New_Developments_In_Low_Bit-rate_Coding.pdf)
   * **Phân tích kỹ thuật**: Phân tích sự tiến hóa của các giải pháp nén âm thanh hiện đại và giải pháp bù lỗi gói tin trên kênh vô tuyến.
   * **Mô-đun hỗ trợ**: **Khối Thuật toán Bù Mất Gói (Packet Loss Concealment - PLC)** tại máy thu IEM để nội suy dạng sóng khi sóng bị fade sâu.

3. **Subjective Evaluation of State-of-the-Art Two-Channel Audio Codecs** [⭐️⭐️⭐️]
   * **Tác giả**: Gilbert A. Soulodre, Theodore Grusec et al. (JAES, 2002) — [elib=12159](https://aes.org/publications/elibrary-page/?id=12159).
   * **Phân tích kỹ thuật**: Phương pháp kiểm thử thính giác mù đôi theo chuẩn **MUSHRA (ITU-R BS.1534)** so sánh chất lượng âm thanh của các codec ở nhiều mức bitrate.
   * **Mô-đun hỗ trợ**: **Khối Phương pháp Đo đạc & Kiểm thử Chất lượng Thính giác** sau khi âm thanh đi qua kênh truyền fading.

4. **AC-2 and AC-3: Low-Complexity Transform-Based Audio Coding** [⭐️⭐️]
   * **Tác giả**: Louis D. Fielder, Marina Bosi et al. (AES Convention 97, 1994) — [elib=7132](https://aes.org/publications/elibrary-page/?id=7132).
   * **Tệp PDF Toàn văn Nội bộ**: [`AC-2_and_AC-3__Low-Complexity_Transform-Based_Audio_Coding.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/AC-2_and_AC-3__Low-Complexity_Transform-Based_Audio_Coding.pdf)
   * **Phân tích kỹ thuật**: Ngân hàng bộ lọc TDAC và chuẩn nén Dolby Digital đa kênh 5.1.
   * **Mô-đun hỗ trợ**: **Khối Đối chứng Chuẩn Nén Chuyên nghiệp**.

5. **High Quality Sound Coding at 2.5 Bit/Sample** [⭐️⭐️]
   * **Tác giả**: Karlheinz Brandenburg (AES Convention 84, 1988) — [elib=4824](https://aes.org/publications/elibrary-page/?id=4824).
   * **Phân tích kỹ thuật**: Đặt nền móng cho việc nén âm thanh chất lượng cao dựa trên ngưỡng che lấp thính giác (*Psychoacoustic Masking*).
   * **Mô-đun hỗ trợ**: **Khối Cơ sở Lý thuyết Nén Âm thanh & Biện luận Kiến trúc**.

6. **Bitrate Reduction by Modelling the Ears Masking Thresholds** [⭐️⭐️]
   * **Tác giả**: Detlef Wiese, Gerhard Stoll (AES Convention 86, 1989) — [elib=5723](https://aes.org/publications/elibrary-page/?id=5723).
   * **Phân tích kỹ thuật**: Mô hình toán học tính toán ngưỡng che lấp tần số để giấu nhiễu lượng tử hóa.
   * **Mô-đun hỗ trợ**: **Khối Lượng tử hóa Thích nghi**.

7. **Aspec-Adaptive Spectral Entropy Coding of High Quality Music** [⭐️⭐️]
   * **Tác giả**: Karlheinz Brandenburg, Jürgen Herre et al. (AES Convention 86, 1989) — [elib=5682](https://aes.org/publications/elibrary-page/?id=5682).
   * **Phân tích kỹ thuật**: Tiền thân trực tiếp của chuẩn nén MP3 sử dụng biến đổi MDCT và mã hóa entropy động.
   * **Mô-đun hỗ trợ**: **Khối Đối chứng Hạn chế Độ trễ của Phép biến đổi MDCT**.

8. **ISO-MPEG-1 Audio: Standard for Coding of High-Quality Digital Audio** [⭐️⭐️]
   * **Tác giả**: Karlheinz Brandenburg, Gerhard Stoll (AES Convention 93, 1992) — [elib=6925](https://aes.org/publications/elibrary-page/?id=6925).
   * **Phân tích kỹ thuật**: Tiêu chuẩn hóa quốc tế ISO/IEC 11172-3 (MPEG-1 Layer I/II/III).
   * **Mô-đun hỗ trợ**: **Khối Đối chứng So sánh Hiệu năng Nén vs Độ trễ**.

9. **ISO/IEC MPEG-2 Advanced Audio Coding (AAC)** [⭐️⭐️]
   * **Tác giả**: Marina Bosi, Karlheinz Brandenburg, Schuyler Quackenbush et al. (JAES, 1997) — [elib=10271](https://aes.org/publications/elibrary-page/?id=10271).
   * **Phân tích kỹ thuật**: Chuẩn nén AAC với các công cụ TNS, M/S stereo và phân bổ bit linh hoạt.
   * **Mô-đun hỗ trợ**: **Khối Biện luận Vì sao Không dùng AAC cho IEM Sân khấu (trễ khung $> 20\text{ ms}$)**.

10. **Spectral Band Replication (SBR), a Novel Approach in Audio Coding** [⭐️⭐️]
    * **Tác giả**: Martin Dietz, Lars Liljeryd, Kristofer Kjörling (AES Convention 112, 2002) — [elib=11328](https://aes.org/publications/elibrary-page/?id=11328).
    * **Phân tích kỹ thuật**: Kỹ thuật tái tạo dải tần cao SBR trong HE-AAC.
    * **Mô-đun hỗ trợ**: **Khối Mở rộng Phổ Tần số ở Bitrate Cực thấp**.

11. **MPEG Unified Speech and Audio Coding (USAC)** [⭐️⭐️]
    * **Tác giả**: Schuyler Quackenbush (AES Convention 131, 2011) — [elib=16115](https://aes.org/publications/elibrary-page/?id=16115).
    * **Phân tích kỹ thuật**: Chuẩn nén kết hợp giọng nói (LPC) và âm nhạc (MDCT) trong ISO/IEC 23003-3.
    * **Mô-đun hỗ trợ**: **Khối Nghiên cứu Mở rộng Nén Hỗn hợp**.

12. **MPEG-H Audio — The New Standard for Universal Spatial/3D Coding** [⭐️⭐️]
    * **Tác giả**: Jürgen Herre, Johannes Hilpert, Jan Plogsties et al. (JAES, 2014) — [elib=17556](https://aes.org/publications/elibrary-page/?id=17556).
    * **Phân tích kỹ thuật**: Chuẩn âm thanh 3D đa năng hỗ trợ Channel, Object và Ambisonics (HOA).
    * **Mô-đun hỗ trợ**: **Khối Mở rộng Âm thanh Không gian 3D cho IEM**.

13. **AC-4 The Next Generation Audio Codec** [⭐️⭐️]
    * **Tác giả**: Kristofer Kjörling, Jonas Röden, Martin Wolters et al. (AES Convention 140, 2016) — [elib=18190](https://aes.org/publications/elibrary-page/?id=18190).
    * **Phân tích kỹ thuật**: Chuẩn nén thế hệ mới của Dolby hỗ trợ quản lý âm lượng và cá nhân hóa hội thoại.
    * **Mô-đun hỗ trợ**: **Khối Tham khảo Kiến trúc Quản lý Dynamic Range**.

14. **Production and Live Transmission of 22.2 Multichannel Sound on UHDTV** [⭐️]
    * **Tác giả**: Akio Ando, Kimio Hamasaki et al. (AES Convention 122, 2007) — [elib=14122](https://aes.org/publications/elibrary-page/?id=14122).
    * **Mô-đun hỗ trợ**: **Khối Tham khảo Truyền dẫn IP Trực tiếp của Đài NHK**.

15. **A Perceptual Model Applied to Audio Bit-Rate Reduction** [⭐️]
    * **Tác giả**: Catherine Colomes et al. (AES Convention 95, 1993) — [elib=7952](https://aes.org/publications/elibrary-page/?id=7952).
    * **Mô-đun hỗ trợ**: **Khối Phân tích Băng tần Thính giác Bark**.

16. **Parametric Coding for High Quality Audio** [⭐️]
    * **Tác giả**: Albertus C. den Brinker et al. (AES Convention 112, 2002) — [elib=11305](https://aes.org/publications/elibrary-page/?id=11305).
    * **Mô-đun hỗ trợ**: **Khối Nghiên cứu Nén Âm thanh Tham số**.

17. **A New Surround-Stereo-Surround Coding Technique** [⭐️]
    * **Tác giả**: Warner R. ten Kate et al. (AES Convention 93, 1992) — [elib=7046](https://aes.org/publications/elibrary-page/?id=7046).
    * **Mô-đun hỗ trợ**: **Khối Ma trận hóa Tương thích Ngược**.

18. **An Overview of MPEG Audio: Current and Future Standards** [⭐️]
    * **Tác giả**: Karlheinz Brandenburg, Marina Bosi et al. (JAES, 1997) — [elib=7871](https://aes.org/publications/elibrary-page/?id=7871).
    * **Mô-đun hỗ trợ**: **Khối Bối cảnh Lịch sử Tiêu chuẩn hóa**.

---

## III. CHỦ ĐỀ AES 2: TAI NGHE & IN-EAR MONITORS (HEADPHONES)
> Nguồn chính thức: [https://aes.org/audio-topics/headphones-2/](https://aes.org/audio-topics/headphones-2/)

### 1. Danh mục Toàn bộ 10 Bài báo Khoa học Nghiên cứu

1. **A Statistical Model that Predicts Listeners’ Preference Ratings of In-Ear Headphones: Part 1 & Part 2** [⭐️⭐️⭐️]
   * **Tác giả**: Sean Olive, Todd Welti, Omid Khonsaripour (Harman International, AES Convention 143, 2017) — [elib=19237](https://aes.org/publications/elibrary-page/?id=19237), [elib=19275](https://aes.org/publications/elibrary-page/?id=19275).
   * **Tệp PDF Toàn văn Nội bộ**: Part 1: [`A_Statistical_Model_that_Predicts_Listeners’_Preference_Ratings_of_In-Ear_Headphones__Part_1—Listening_Test_Results_and_Acoustic_Measurements.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/A_Statistical_Model_that_Predicts_Listeners%E2%80%99_Preference_Ratings_of_In-Ear_Headphones__Part_1%E2%80%94Listening_Test_Results_and_Acoustic_Measurements.pdf) | Part 2: [`A_Statistical_Model_that_Predicts_Listeners’_Preference_Ratings_of_In-Ear_Headphones__Part_2—Development_and_Validation_of_the_Model.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/A_Statistical_Model_that_Predicts_Listeners%E2%80%99_Preference_Ratings_of_In-Ear_Headphones__Part_2%E2%80%94Development_and_Validation_of_the_Model.pdf)
   * **Phân tích kỹ thuật**: Công trình kinh điển xác lập đường cong mục tiêu **Harman In-Ear Target Curve**. Đưa ra mô hình hồi quy dự đoán độ ưa thích âm thanh của người nghe dựa trên đáp ứng tần số thực đo.
   * **Mô-đun hỗ trợ**: **Khối Bộ lọc Âm học IEM (Harman Target Equalizer FIR/IIR)** tại đầu ra Audio Sink của máy thu IEM trong GNU Radio.

2. **Headphone Response: Target Equalization Trade-offs and Limitations** [⭐️⭐️⭐️]
   * **Tác giả**: Christopher J. Struck, Steve Temme (CJS Labs / Listen Inc., AES Convention 139, 2015) — [elib=17932](https://aes.org/publications/elibrary-page/?id=17932).
   * **Tệp PDF Toàn văn Nội bộ**: [`Headphone_Response__Target_Equalization_Trade-offs_and_Limitations.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Headphone_Response__Target_Equalization_Trade-offs_and_Limitations.pdf)
   * **Phân tích kỹ thuật**: Khảo sát sự đánh đổi khi cân bằng đáp ứng tần số tai nghe giữa trường tự do (*Free-field*), trường khuếch tán (*Diffuse-field*) và buồng kín ống tai.
   * **Mô-đun hỗ trợ**: **Khối Thiết kế Bộ lọc Bù Tần số DSP** và xác định giới hạn điều chỉnh EQ tránh hiện tượng méo phi tuyến.

3. **A Self-Calibrating Earphone** [⭐️⭐️⭐️]
   * **Tác giả**: Juha Backman, Tom Campbell, Marko Hiipakka (Hefio Oy, AES Convention 142, 2017) — [elib=18722](https://aes.org/publications/elibrary-page/?id=18722).
   * **Tệp PDF Toàn văn Nội bộ**: [`A_Self-Calibrating_Earphone.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/A_Self-Calibrating_Earphone.pdf)
   * **Phân tích kỹ thuật**: Hệ thống tự động đo đáp ứng âm học từ cửa ống tai đến màng nhĩ theo thời gian thực và tự động tạo bộ lọc DSP bù trừ cá nhân hóa.
   * **Mô-đun hỗ trợ**: **Khối Cân chỉnh Thích nghi Âm học Cá nhân hóa cho IEM**.

4. **Principles of Headphone Design—A Tutorial Review** [⭐️⭐️]
   * **Tác giả**: Christopher J. Struck (JAES, 2014) — [elib=17274](https://aes.org/publications/elibrary-page/?id=17274).
   * **Phân tích kỹ thuật**: Hướng dẫn toàn diện về nguyên lý thiết kế cơ điện âm (*Electroacoustics*), cấu tạo driver Dynamic và Balanced Armature trong tai nghe.
   * **Mô-đun hỗ trợ**: **Khối Mô phỏng Mô hình Điện cơ Âm học Đầu ra Tai nghe**.

5. **Refinements in the Electroacoustic Testing of Headphones** [⭐️⭐️]
   * **Tác giả**: Christopher J. Struck, Steve Temme (AES Convention 141, 2016) — [elib=18364](https://aes.org/publications/elibrary-page/?id=18364).
   * **Phân tích kỹ thuật**: Phương pháp đo đạc độ méo THD, đáp ứng xung và trở kháng của tai nghe bằng thiết bị đo mô phỏng đầu và tai giả (HATS).
   * **Mô-đun hỗ trợ**: **Khối Kiểm chuẩn Âm học Đầu ra**.

6. **Perceptual Assessment of Headphone Distortion** [⭐️⭐️]
   * **Tác giả**: Steve Temme, Sean Olive et al. (AES Convention 143, 2017) — [elib=19238](https://aes.org/publications/elibrary-page/?id=19238).
   * **Phân tích kỹ thuật**: Khảo sát ngưỡng nhận biết của tai người đối với hiện tượng méo hài và méo xuyên điều chế trong tai nghe.
   * **Mô-đun hỗ trợ**: **Khối Thiết lập Ngưỡng Méo Biên độ Tối đa cho Bộ Limiter**.

7. **Headphone Technology: Personalization, Perception, Preference** [⭐️⭐️]
   * **Tác giả**: Ban Biên tập AES / Francis Rumsey (JAES, 2016) — [elib=18529](https://aes.org/publications/elibrary-page/?id=18529).
   * **Mô-đun hỗ trợ**: **Khối Khảo sát Trải nghiệm Thính giác Cá nhân hóa**.

8. **A High Resolution Full-Spherical HRTF Database** [⭐️]
   * **Tác giả**: Fabian Brinkmann et al. (AES Convention 143, 2017) — [elib=19357](https://aes.org/publications/elibrary-page/?id=19357).
   * **Mô-đun hỗ trợ**: **Khối Mở rộng Giả lập Không gian Âm thanh 3D Song nhĩ**.

9. **Database Matching of Sparsely Measured HRTFs** [⭐️]
   * **Tác giả**: Gavin Kearney et al. (AES Convention 143, 2017) — [elib=19171](https://aes.org/publications/elibrary-page/?id=19171).
   * **Mô-đun hỗ trợ**: **Khối Khớp nối Dữ liệu HRTF Thưa**.

10. **Sean Olive’s AES Headphone Paper Collection** [⭐️]
    * **Tác giả**: Sean Olive (AES E-Library Collection, 2015) — [docID=5](http://www.aes.org/e-lib/collections/?ID=5).
    * **Mô-đun hỗ trợ**: **Kho Tài liệu Nghiên cứu Tiêu chuẩn Tai nghe Harman**.

---

## IV. CHỦ ĐỀ AES 3: ÂM THANH SÂN KHẤU TRỰC TIẾP (SOUND REINFORCEMENT)
> Nguồn chính thức: [https://aes.org/audio-topics/sound-reinforcement-2/](https://aes.org/audio-topics/sound-reinforcement-2/)

### 1. Danh mục Toàn bộ 16 Bài báo Khoa học & Chuyên đề

1. **Psychoacoustics in Sound Reinforcement and PA Design** [⭐️⭐️⭐️]
   * **Tác giả**: Wolfgang Ahnert et al. (JAES, 2007) — [elib=17284](https://aes.org/publications/elibrary-page/?id=17284).
   * **Tệp PDF Toàn văn Nội bộ**: [`Psychoacoustics_in_Sound_Reinforcement_and_PA_Design.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Psychoacoustics_in_Sound_Reinforcement_and_PA_Design.pdf)
   * **Phân tích kỹ thuật**: Phân tích các hiện tượng tâm thính học trên sân khấu biểu diễn trực tiếp, đặc biệt là hiện tượng trễ âm thanh và méo lọc lược (*comb filtering*) giữa âm thanh phát từ loa kiểm âm ngoài và âm thanh dẫn truyền qua xương sọ ca sĩ.
   * **Mô-đun hỗ trợ**: **Khối Đặc tả Kỹ thuật Độ trễ Tối đa của Hệ thống ($< 4.5\text{ ms}$)**.

2. **Live Sound System Optimization** [⭐️⭐️⭐️]
   * **Tác giả**: Ban Biên tập AES / Francis Rumsey (JAES, 2015) — [elib=17391](https://aes.org/publications/elibrary-page/?id=17391).
   * **Tệp PDF Toàn văn Nội bộ**: [`Live_Sound_System_Optimization.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Live_Sound_System_Optimization.pdf)
   * **Phân tích kỹ thuật**: Phương pháp tối ưu hóa hệ thống âm thanh sân khấu quy mô lớn, kiểm soát độ phủ sóng và triệt tiêu can nhiễu đa nguồn.
   * **Mô-đun hỗ trợ**: **Khối Mô hình Hóa Môi trường Sân khấu Biểu diễn Trực tiếp**.

3. **Object-Based Audio in Large Scale Live Sound Reinforcement** [⭐️⭐️]
   * **Tác giả**: Mario Seideneck, Johannes Bergner et al. (AES Convention 142, 2017) — [elib=18724](https://aes.org/publications/elibrary-page/?id=18724).
   * **Phân tích kỹ thuật**: Ứng dụng âm thanh hướng đối tượng điều khiển bằng hệ thống định vị chuyển động nghệ sĩ thời gian thực (*Motion Tracking*) trên sân khấu.
   * **Mô-đun hỗ trợ**: **Khối Mở rộng Định vị Nguồn Âm theo Vị trí Ca sĩ**.

4. **Live Sound: Things to Get Right** [⭐️⭐️]
   * **Tác giả**: Francis Rumsey (JAES, 2012) — [elib=16159](https://aes.org/publications/elibrary-page/?id=16159).
   * **Phân tích kỹ thuật**: Các nguyên tắc cốt lõi về kiểm soát dải động (*Gain Staging*), tỷ số S/N và đồng pha hệ thống sân khấu.
   * **Mô-đun hỗ trợ**: **Khối Kiểm soát Mức Tín hiệu (Gain Staging) trong GNU Radio**.

5. **Smart Digital Loudspeaker Arrays** [⭐️⭐️]
   * **Tác giả**: Mark Ureda (AES Convention 115, 2003) — [elib=12189](https://aes.org/publications/elibrary-page/?id=12189).
   * **Phân tích kỹ thuật**: Điều khiển búp sóng âm thanh kỹ thuật số (*Digital Beamforming*) và định hình trường âm.
   * **Mô-đun hỗ trợ**: **Khối Phân tích Búp sóng Vô tuyến Tương đương**.

6. **Acoustical Measurements by Time Delay Spectrometry** [⭐️⭐️]
   * **Tác giả**: Richard C. Heyser (JAES, 1967) — [elib=1084](https://aes.org/publications/elibrary-page/?id=1084).
   * **Phân tích kỹ thuật**: Công trình kinh điển của Heyser về phương pháp đo trễ phổ tần (*TDS*) để phân tách âm thanh trực tiếp và âm phản xạ dội tường.
   * **Mô-đun hỗ trợ**: **Khối Phân tách Âm trực tiếp và Âm phản xạ Đa đường**.

7. **Sound Reinforcement Engineering and Technology** [⭐️⭐️]
   * **Tác giả**: Francis Rumsey (JAES, 2016) — [elib=18045](https://aes.org/publications/elibrary-page/?id=18045).
   * **Mô-đun hỗ trợ**: **Khối Tổng quan Công nghệ Âm thanh Trực tiếp**.

8. **Live Sound Subwoofer System Performance Quantification** [⭐️]
   * **Tác giả**: Adam J. Hill (JAES, 2018) — [elib=19442](https://aes.org/publications/elibrary-page/?id=19442).
   * **Mô-đun hỗ trợ**: **Khối Phân tích Đáp ứng Tần số Thấp Sân khấu**.

9. **Historical Perspectives and Technology Overview of Loudspeakers** [⭐️]
   * **Tác giả**: John Eargle, Mark Gander (JAES, 2004) — [elib=13000](https://aes.org/publications/elibrary-page/?id=13000).
   * **Mô-đun hỗ trợ**: **Khối Lịch sử Công nghệ Âm thanh Sân khấu**.

10. **Sound Reinforcing Systems (1950)** [⭐️]
    * **Tác giả**: Arthur W. Schneider (JAES, 1950) — [elib=17807](https://aes.org/publications/elibrary-page/?id=17807).
    * **Mô-đun hỗ trợ**: **Khối Nền tảng Ban đầu của AES**.

11. **Frequency Characteristic of a Sound-Reinforcing System (1955)** [⭐️]
    * **Tác giả**: C. P. Boner (JAES, 1955) — [elib=26](https://aes.org/publications/elibrary-page/?id=26).
    * **Mô-đun hỗ trợ**: **Khối Nghiên cứu Đáp ứng Tần số**.

12. **Gradient Loudspeakers (1973)** [⭐️]
    * **Tác giả**: C. B. Olson (JAES, 1973) — [elib=2006](https://aes.org/publications/elibrary-page/?id=2006).
    * **Mô-đun hỗ trợ**: **Khối Nghiên cứu Gradient Sóng**.

13. **Equivalent Acoustic Distance (1973)** [⭐️]
    * **Tác giả**: V. M. A. Peutz (JAES, 1973) — [elib=1939](https://aes.org/publications/elibrary-page/?id=1939).
    * **Mô-đun hỗ trợ**: **Khối Tính toán Khoảng cách Âm học Tương đương**.

14. **A Microprocessor Based TEF Analyzer (1989)** [⭐️]
    * **Tác giả**: Gerald Stanley (AES Convention 87, 1989) — [elib=11813](https://aes.org/publications/elibrary-page/?id=11813).
    * **Mô-đun hỗ trợ**: **Khối Phân tích TEF**.

15. **Large Arrays: Measured Free-Field Polar Patterns** [⭐️]
    * **Tác giả**: Mark S. Ureda (AES Convention 89, 1990) — [elib=6036](https://aes.org/publications/elibrary-page/?id=6036).
    * **Mô-đun hỗ trợ**: **Khối Phân tích Búp hướng Mảng Nguồn**.

16. **Sound Fields Radiated by Multiple Sound Sources Arrays (1992)** [⭐️]
    * **Tác giả**: Etienne Corteel et al. (JAES, 1992) — [elib=6864](https://aes.org/publications/elibrary-page/?id=6864).
    * **Mô-đun hỗ trợ**: **Khối Mô hình Hóa Trường Âm Đa Nguồn**.

---

## V. CHỦ ĐỀ AES 4: MẠNG ÂM THANH & TRUYỀN DẪN THỜI GIAN THỰC (AUDIO NETWORKING)
> Nguồn chính thức: [https://aes.org/audio-topics/audio-networking-2/](https://aes.org/audio-topics/audio-networking-2/)

### 1. Danh mục Toàn bộ 19 Bài báo Khoa học & Chuyên đề

1. **Flexilink: A Unified Low Latency Network Architecture for Multichannel Live Audio** [⭐️⭐️⭐️]
   * **Tác giả**: Yonghao Wang, John Grant, Axel Fischer (AES Convention 134, 2013) — [elib=16433](https://aes.org/publications/elibrary-page/?id=16433).
   * **Tệp PDF Toàn văn Nội bộ**: [`Flexilink__A_Unified_Low_Latency_Network_Architecture_for_Multichannel_Live_Audio.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Flexilink__A_Unified_Low_Latency_Network_Architecture_for_Multichannel_Live_Audio.pdf)
   * **Phân tích kỹ thuật**: Kiến trúc mạng truyền dẫn âm thanh trực tiếp thống nhất với độ trễ cực thấp (dưới $1\text{ ms}$). Định nghĩa phương pháp đóng gói gói tin kích thước siêu nhỏ (*micro-packets*) để loại bỏ độ trễ hàng đợi (*queuing delay*).
   * **Mô-đun hỗ trợ**: **Khối Đóng gói Micro-Packets & Định dạng Gói tin (Framing & Packetizer)** trong máy phát IEM.

2. **Redundancy Optimization for Networked Audio Systems** [⭐️⭐️⭐️]
   * **Tác giả**: Damian Kowalski, Stefan Heinzmann (AES Convention 133, 2012) — [elib=16246](https://aes.org/publications/elibrary-page/?id=16246).
   * **Tệp PDF Toàn văn Nội bộ**: [`Redundancy_Optimization_for_Networked_Audio_Systems.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Redundancy_Optimization_for_Networked_Audio_Systems.pdf)
   * **Phân tích kỹ thuật**: Tối ưu hóa kỹ thuật truyền dự phòng kép (*Packet Duplication / Redundancy*) để bù đắp việc mất gói trên kênh truyền vô tuyến mà không cần cơ chế truyền lại (*ARQ*) — vốn gây trễ không chấp nhận được trong IEM.
   * **Mô-đun hỗ trợ**: **Khối Cơ chế Dự phòng Chống Mất Gói Tin (Packet Redundancy)**.

3. **Latency Issues in Audio Networking** [⭐️⭐️⭐️]
   * **Tác giả**: Nuno Fonseca, Edmundo Monteiro (AES Convention 118, 2005) — [elib=13190](https://aes.org/publications/elibrary-page/?id=13190).
   * **Tệp PDF Toàn văn Nội bộ**: [`Latency_Issues_in_Audio_Networking.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Latency_Issues_in_Audio_Networking.pdf)
   * **Phân tích kỹ thuật**: Phân tích chi tiết sự phân rã của tổng ngân sách độ trễ (*Latency Budget*) thành: Trễ lấy mẫu $\rightarrow$ Trễ bộ đệm $\rightarrow$ Trễ mã hóa $\rightarrow$ Trễ truyền dẫn $\rightarrow$ Trễ giải điều chế.
   * **Mô-đun hỗ trợ**: **Khối Phân tích & Đo đạc Ngân sách Độ trễ End-to-End ($< 4.5\text{ ms}$)**.

4. **Enhancement of IEEE 802.11 in Handling Multiple Broadcasting Audio Data** [⭐️⭐️]
   * **Tác giả**: Christos Chousidis, Rajagopal Nilavalan, Andreas Floros (AES Convention 134, 2013) — [elib=16702](https://aes.org/publications/elibrary-page/?id=16702).
   * **Phân tích kỹ thuật**: Cải tiến thuật toán MAC vô tuyến cho luồng broadcast âm thanh trực tiếp, giảm thiểu rớt gói (*packet drop*) và xung đột truyền dẫn.
   * **Mô-đun hỗ trợ**: **Khối Thiết lập Cơ chế Quản lý Kênh Vô tuyến Thời gian thực**.

5. **Synchronization Strategies for IP Networked Audio Equipment** [⭐️⭐️]
   * **Tác giả**: Tom Blank, Robert Atkinson (AES Convention 137, 2014) — [elib=17257](https://aes.org/publications/elibrary-page/?id=17257).
   * **Phân tích kỹ thuật**: Chiến lược đồng bộ hóa xung nhịp đồng hồ mạng dựa trên chuẩn IEEE 1588 PTP (Precision Time Protocol) để triệt tiêu hiện tượng rung pha (*Jitter*).
   * **Mô-đun hỗ trợ**: **Khối Đồng bộ Hóa Xung Nhịp (Clock Synchronization & Jitter Buffer)**.

6. **Setting Up and Making an AES67 Network Coexist with Standard Traffic** [⭐️⭐️]
   * **Tác giả**: Mickaël Henry, Luca Rémond (AES Convention 140, 2016) — [elib=18145](https://aes.org/publications/elibrary-page/?id=18145).
   * **Phân tích kỹ thuật**: Cấu hình luồng âm thanh chuẩn **AES67 Audio-over-IP** chạy ổn định với chất lượng dịch vụ QoS được đảm bảo.
   * **Mô-đun hỗ trợ**: **Khối Tương thích Luồng Âm thanh Chuẩn AES67**.

7. **A Multicore Operating System with QoS Guarantees for Network Audio** [⭐️⭐️]
   * **Tác giả**: Juan A. Colmenares, Nils Peters et al. (AES Convention 134, 2013) — [elib=16703](https://aes.org/publications/elibrary-page/?id=16703).
   * **Phân tích kỹ thuật**: Phân bổ luồng xử lý âm thanh đa nhân trên hệ điều hành thời gian thực đảm bảo QoS.
   * **Mô-đun hỗ trợ**: **Khối Tối ưu Hóa Luồng Tính toán Đa nhân trong GNU Radio / Python**.

8. **Rolling out AES67** [⭐️⭐️]
   * **Tác giả**: Francis Rumsey (JAES, 2016) — [elib=18551](https://aes.org/publications/elibrary-page/?id=18551).
   * **Mô-đun hỗ trợ**: **Khối Nghiên cứu Tiêu chuẩn Hóa AES67**.

9. **AES67: How the Net Was Won** [⭐️⭐️]
   * **Tác giả**: Francis Rumsey (JAES, 2014) — [elib=17132](https://aes.org/publications/elibrary-page/?id=17132).
   * **Mô-đun hỗ trợ**: **Khối Tổng quan Chuẩn AoIP**.

10. **Audio Networks: Now We’re Talking!** [⭐️]
    * **Tác giả**: Francis Rumsey (JAES, 2013) — [elib=16675](https://aes.org/publications/elibrary-page/?id=16675).
    * **Mô-đun hỗ trợ**: **Khối Bối cảnh Mạng Âm thanh Số**.

11. **Audio in the Age of Digital Networks** [⭐️]
    * **Tác giả**: Francis Rumsey (JAES, 2011) — [elib=15928](https://aes.org/publications/elibrary-page/?id=15928).
    * **Mô-đun hỗ trợ**: **Khối Lịch sử Chuyển dịch Số**.

12. **Audio Networking for the Pros** [⭐️]
    * **Tác giả**: Francis Rumsey (JAES, 2008) — [elib=14817](https://aes.org/publications/elibrary-page/?id=14817).
    * **Mô-đun hỗ trợ**: **Khối Ứng dụng Chuyên nghiệp**.

13. **Audio Networking: Applications and Requirements** [⭐️]
    * **Tác giả**: Kevin Gross (JAES, 2006) — [elib=13692](https://aes.org/publications/elibrary-page/?id=13692).
    * **Mô-đun hỗ trợ**: **Khối Phân tích Yêu cầu Kỹ thuật**.

14. **The Future of High-Performance Media Networking** [⭐️]
    * **Tác giả**: Kevin Gross (AES Convention 131, 2011) — [elib=16141](https://aes.org/publications/elibrary-page/?id=16141).
    * **Mô-đun hỗ trợ**: **Khối Xu hướng Mạng Truyền thông Hiệu năng Cao**.

15. **An Open-Source Dynamic Networked Audio System** [⭐️]
    * **Tác giả**: Michelle Daniels (AES Convention 136, 2014) — [elib=17219](https://aes.org/publications/elibrary-page/?id=17219).
    * **Mô-đun hỗ trợ**: **Khối Kiến trúc Mã nguồn Mở**.

16. **Feature-Based Analysis of Packet Delay on Musical Interactions** [⭐️]
    * **Tác giả**: Cristina Rottondi, Michele Buccoli et al. (JAES, 2016) — [elib=18047](https://aes.org/publications/elibrary-page/?id=18047).
    * **Mô-đun hỗ trợ**: **Khối Phân tích Tác động của Trễ Gói tin đến Trình diễn Nhạc**.

17. **Challenges of using Networked Music Performance in Education** [⭐️]
    * **Tác giả**: Miriam Iorwerth, Dave Moore (JAES, 2015) — [elib=17857](https://aes.org/publications/elibrary-page/?id=17857).
    * **Mô-đun hỗ trợ**: **Khối Đánh giá Trình diễn Nhạc qua Mạng**.

18. **Dante and AVB Networking** [⭐️]
    * **Tác giả**: AES Standards Committee (2014) — [elib=17313](https://aes.org/publications/elibrary-page/?id=17313).
    * **Mô-đun hỗ trợ**: **Khối So sánh Giao thức Dante và AVB**.

19. **Life after IP** [⭐️]
    * **Tác giả**: John Grant (AES Convention 137, 2014) — [elib=17294](https://aes.org/publications/elibrary-page/?id=17294).
    * **Mô-đun hỗ trợ**: **Khối Nghiên cứu Kiến trúc Mạng Tương lai**.

---

## VI. CHỦ ĐỀ AES 5: BẢO VỆ THÍNH LỰC NGHỆ SĨ (HEARING PROTECTION)
> Nguồn chính thức: [https://aes.org/audio-topics/hearing-and-hearing-loss-prevention-2/](https://aes.org/audio-topics/hearing-and-hearing-loss-prevention-2/)

### 1. Danh mục Toàn bộ 12 Bài báo Khoa học & Chuyên đề

1. **Do In-Ear Monitors Protect Musicians Hearing?** [⭐️⭐️⭐️]
   * **Tác giả**: Arne Nykänen, Magnus Löfdahl, Tomas Johannesson, Jan Berg (Luleå University of Technology, AES Convention 142, 2017) — [elib=18649](https://aes.org/publications/elibrary-page/?id=18649).
   * **Tệp PDF Toàn văn Nội bộ**: [`Do_In-Ear_Monitors_Protect_Musicians’_Hearing_.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Do_In-Ear_Monitors_Protect_Musicians%E2%80%99_Hearing_.pdf)
   * **Phân tích kỹ thuật**: Đo lường thực tế mức áp suất âm thanh tương đương ($L_{\text{eq}}$) tại màng nhĩ ca sĩ ($86\text{ dBA} - 108\text{ dBA}$). Chứng minh rằng nếu không có cơ chế khống chế biên độ đỉnh, hiện tượng mất sóng hoặc lỗi bùng bit trên sóng vô tuyến có thể gây tổn thương thính giác vĩnh viễn.
   * **Mô-đun hỗ trợ**: **Khối Bộ Giới Hạn Đỉnh An Toàn Thính Lực (Brickwall Safety Peak Limiter)** tại đầu ra tai nghe IEM trong GNU Radio.

2. **How the Ear Works and Why Loud Sounds Cause Hearing Loss** [⭐️⭐️]
   * **Tác giả**: Alan Palmer (JAES, 2003) — [elib=12261](https://aes.org/publications/elibrary-page/?id=12261).
   * **Phân tích kỹ thuật**: Cơ chế sinh lý học tai người, tổn thương tế bào lông ốc tai do quá tải áp suất âm thanh liên tục và xung áp suất đột ngột (*acoustic shock*).
   * **Mô-đun hỗ trợ**: **Khối Phân tích Giới hạn An toàn Âm lượng (SPL Safety Thresholds)**.

3. **Why Do My Ears Hurt after a Show (And What Can I Do to Prevent It)** [⭐️⭐️]
   * **Tác giả**: Dennis Rauschmayer (AES Convention 141, 2016) — [elib=17889](https://aes.org/publications/elibrary-page/?id=17889).
   * **Phân tích kỹ thuật**: Phân tích hiện tượng dịch ngưỡng nghe tạm thời (TTS) sau buổi biểu diễn và các biện pháp bảo vệ thính lực chủ động.
   * **Mô-đun hỗ trợ**: **Khối Thiết lập Ngưỡng Phơi nhiễm Âm thanh**.

4. **Preventing Hearing Loss** [⭐️⭐️]
   * **Tác giả**: Ban Biên tập AES / Staff (JAES, 2006) — [elib=13891](https://aes.org/publications/elibrary-page/?id=13891).
   * **Mô-đun hỗ trợ**: **Khối Tiêu chuẩn Bảo vệ Thính lực Nghề nghiệp**.

5. **Music-Induced Hearing Disorders** [⭐️⭐️]
   * **Tác giả**: Francis Rumsey (JAES, 2016) — [elib=17876](https://aes.org/publications/elibrary-page/?id=17876).
   * **Mô-đun hỗ trợ**: **Khối Khảo sát Rối loạn Thính giác do Âm nhạc**.

6. **Hearing Enhancement** [⭐️⭐️]
   * **Tác giả**: Francis Rumsey (JAES, 2008) — [elib=14822](https://aes.org/publications/elibrary-page/?id=14822).
   * **Mô-đun hỗ trợ**: **Khối Tăng cường Thính lực và Độ rõ Nét Âm thanh**.

7. **Effects of Sound-Induced Hearing Loss on Perception of Music** [⭐️]
   * **Tác giả**: Brian C.J. Moore (AES Convention 140, 2016) — [elib=18122](https://aes.org/publications/elibrary-page/?id=18122).
   * **Mô-đun hỗ trợ**: **Khối Phân tích Suy giảm Cảm nhận Âm nhạc**.

8. **Hearing Loss, Earplug Use, and Attitudes Among Musicians** [⭐️]
   * **Tác giả**: Ian O’Brien, Elizabeth Beach et al. (AES Convention 140, 2016) — [elib=18124](https://aes.org/publications/elibrary-page/?id=18124).
   * **Mô-đun hỗ trợ**: **Khối Khảo sát Thói quen Đeo Nút Tai Bảo vệ**.

9. **Listeners with Low Thresholds Do Not Perform Better in Difficult Tasks** [⭐️]
   * **Tác giả**: Piotr Kleczkowski, Magdalena Pluta (JAES, 2012) — [elib=16279](https://aes.org/publications/elibrary-page/?id=16279).
   * **Mô-đun hỗ trợ**: **Khối Đánh giá Ngưỡng Nghe trong Môi trường Nhiễu**.

10. **Workplace Noise Regulations in the Music Industry** [⭐️]
    * **Tác giả**: Robert M. Ghent, Jr. (JAES, 2013) — [elib=16935](https://aes.org/publications/elibrary-page/?id=16935).
    * **Mô-đun hỗ trợ**: **Khối Quy định An toàn Lao động Tiếng ồn**.

11. **Daily Noise-Level Exposures of Professional Recording Engineers** [⭐️]
    * **Tác giả**: Wesley A. Bulla et al. (JAES, 2000) — [elib=8388](https://aes.org/publications/elibrary-page/?id=8388).
    * **Mô-đun hỗ trợ**: **Khối Đo lường Liều lượng Âm thanh Hàng ngày**.

12. **Hearing Loops, The Preferred Assistive Listening Technology** [⭐️]
    * **Tác giả**: Thomas Kaufmann, Juliette Sterkens (JAES, 2015) — [elib=17587](https://aes.org/publications/elibrary-page/?id=17587).
    * **Mô-đun hỗ trợ**: **Khối Công nghệ Vòng Từ Hỗ trợ Nghe**.

---

## VII. CHỦ ĐỀ AES 6: ĐÁNH GIÁ CHẤT LƯỢNG ÂM THANH KHÁCH QUAN (SOUND QUALITY PREDICTION)
> Nguồn chính thức: [https://aes.org/audio-topics/sound-quality-predition-2/](https://aes.org/audio-topics/sound-quality-predition-2/)

### 1. Danh mục Toàn bộ 11 Bài báo Khoa học Nghiên cứu

1. **PEAQ – The ITU Standard for Objective Measurement of Perceived Audio Quality** [⭐️⭐️⭐️]
   * **Tác giả**: Thilo Thiede, William C. Treurniet, Roland Bitto, Thomas Sporer, John G. Beerends et al. (JAES, 2000) — [elib=12078](https://aes.org/publications/elibrary-page/?id=12078). *(Tiêu chuẩn ITU-R BS.1387)*.
   * **Tệp PDF Toàn văn Nội bộ**: [`PEAQ_-_The_ITU_Standard_for_Objective_Measurement_of_Perceived_Audio_Quality.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/PEAQ_-_The_ITU_Standard_for_Objective_Measurement_of_Perceived_Audio_Quality.pdf)
   * **Phân tích kỹ thuật**: Thuật toán quốc tế chuẩn mực kết hợp mô hình màng đáy ốc tai, tính toán ngưỡng che lấp động và lượng tử hóa sai lệch năng lượng để tính ra điểm sai khác chất lượng khách quan **ODG (Objective Difference Grade từ $0.0$ đến $-4.0$)**.
   * **Mô-đun hỗ trợ**: **Khối Script Python Đo Chất Lượng Âm Thanh Khách Quan (PEAQ QA Benchmark)** trong GNU Radio.

2. **Perceptual Objective Listening Quality Assessment (POLQA)** [⭐️⭐️⭐️]
   * **Tác giả**: John G. Beerends, Christian Schmidmer et al. (JAES, 2013) — [elib=16830](https://aes.org/publications/elibrary-page/?id=16830). *(Tiêu chuẩn ITU-T P.863)*.
   * **Tệp PDF Toàn văn Nội bộ**: [`Perceptual_Objective_Listening_Quality_Assessment_(POLQA),_The_Third_Generation_ITU-T_Standard_for_End-to-End_Speech_Quality_Measurement_Part_II—Perceptual_Model.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/Perceptual_Objective_Listening_Quality_Assessment_%28POLQA%29%2C_The_Third_Generation_ITU-T_Standard_for_End-to-End_Speech_Quality_Measurement_Part_II%E2%80%94Perceptual_Model.pdf)
   * **Phân tích kỹ thuật**: Chuẩn đo lường chất lượng âm thanh thế hệ 3 có khả năng bù trừ trễ thời gian động (*Time Warping*), đánh giá chính xác chất lượng âm thanh khi kênh vô tuyến bị trễ biến thiên (*Jitter*) và mất gói.
   * **Mô-đun hỗ trợ**: **Khối Đánh giá Hiệu năng Hệ thống dưới Tác động của Jitter & Mất Gói**.

3. **Spatial Audio Quality Perception (Part 2): A Linear Regression Model** [⭐️⭐️]
   * **Tác giả**: Robert Conetta, Tim Brookes et al. (JAES, 2015) — [elib=17558](https://aes.org/publications/elibrary-page/?id=17558).
   * **Phân tích kỹ thuật**: Mô hình hồi quy tuyến tính dự đoán chất lượng không gian âm thanh dựa trên các tham số vật lý đo đạc.
   * **Mô-đun hỗ trợ**: **Khối Đánh giá Độ Rộng và Độ Ổn định Âm hình Tai nghe**.

4. **Multi-Criteria Subjective and Objective Evaluation of Audio Source Separation** [⭐️⭐️]
   * **Tác giả**: Valentin Emiya, Emmanuel Vincent et al. (JAES, 2011) — [elib=15468](https://aes.org/publications/elibrary-page/?id=15468).
   * **Phân tích kỹ thuật**: Bộ công cụ đánh giá đa tiêu chí (SDR, SIR, SAR) phân tách tín hiệu nguồn và nhiễu.
   * **Mô-đun hỗ trợ**: **Khối Đo lường Tỷ số Tín hiệu trên Méo và Nhiễu (SDR/SIR) sau Cân bằng LMS**.

5. **A Model of Distraction in an Audio-on-Audio Interference Situation** [⭐️⭐️]
   * **Tác giả**: Jon Francombe, Russell Mason et al. (JAES, 2015) — [elib=17567](https://aes.org/publications/elibrary-page/?id=17567).
   * **Phân tích kỹ thuật**: Mô hình hóa mức độ phân tâm thính giác khi có can nhiễu âm thanh nền.
   * **Mô-đun hỗ trợ**: **Khối Phân tích Khả năng Cách ly Tiếng ồn Sân khấu của IEM**.

6. **A Model of Loudness Applicable to Time-Varying Sounds** [⭐️⭐️]
   * **Tác giả**: Brian R. Glasberg, Brian C.J. Moore (JAES, 2002) — [elib=11081](https://aes.org/publications/elibrary-page/?id=11081).
   * **Phân tích kỹ thuật**: Mô hình toán học tính toán độ to cảm nhận (*Loudness in Sones/Phons*) đối với tín hiệu âm thanh biến thiên theo thời gian.
   * **Mô-đun hỗ trợ**: **Khối Cân bằng Âm lượng Tự động (Auto Gain Control - AGC)**.

7. **Comparison of Objective Assessment Methods for Intelligibility and Quality** [⭐️]
   * **Tác giả**: Juan-Pablo Ramirez, Alexander Raake (AES Convention 130, 2011) — [elib=15017](https://aes.org/publications/elibrary-page/?id=15017).
   * **Mô-đun hỗ trợ**: **Khối So sánh Độ rõ Tiếng hát (Intelligibility)**.

8. **Subjective Loudness of 22.2 Multichannel Programs** [⭐️]
   * **Tác giả**: Tomoyasu Komori et al. (AES Convention 139, 2015) — [elib=17643](https://aes.org/publications/elibrary-page/?id=17643).
   * **Mô-đun hỗ trợ**: **Khối Khảo sát Âm lượng Đa kênh**.

9. **Development of an Unintrusive Model for Predicting Envelopment** [⭐️]
   * **Tác giả**: Sunish George, Slawomir Zielinski (JAES, 2010) — [elib=15743](https://aes.org/publications/elibrary-page/?id=15743).
   * **Mô-đun hỗ trợ**: **Khối Dự đoán Cảm giác Bao trùm Không gian**.

10. **Objective Measures of Listener Envelopment in Multichannel Systems** [⭐️]
    * **Tác giả**: Gilbert A. Soulodre et al. (JAES, 2003) — [elib=12205](https://aes.org/publications/elibrary-page/?id=12205).
    * **Mô-đun hỗ trợ**: **Khối Đo lường Tương quan Không gian**.

11. **A Statistical Model that Predicts Listeners’ Preference Ratings (Part 2)** [⭐️⭐️⭐️]
    * **Tác giả**: Sean Olive, Todd Welti, Omid Khonsaripour (AES Convention 143, 2017) — [elib=19275](https://aes.org/publications/elibrary-page/?id=19275).
    * **Tệp PDF Toàn văn Nội bộ**: [`A_Statistical_Model_that_Predicts_Listeners’_Preference_Ratings_of_In-Ear_Headphones__Part_2—Development_and_Validation_of_the_Model.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Projects/Reference%20Papers/A_Statistical_Model_that_Predicts_Listeners%E2%80%99_Preference_Ratings_of_In-Ear_Headphones__Part_2%E2%80%94Development_and_Validation_of_the_Model.pdf)
    * **Mô-đun hỗ trợ**: **Khối Kiểm định Mô hình Dự đoán Độ Ưa thích Tai nghe Harman In-Ear**.

---

## VIII. TIÊU CHUẨN QUỐC TẾ & KHUYẾN NGHỊ KỸ THUẬT (INTERNATIONAL STANDARDS)

1. **AES67-2018**: *AES standard for audio applications of networks – High-performance streaming audio-over-IP interoperability* — [docID=96](http://www.aes.org/publications/standards/search.cfm?docID=96).
2. **ITU-R BS.1387-1**: *Method for objective measurements of perceived audio quality (PEAQ)*.
3. **ITU-T P.863**: *Perceptual objective listening quality assessment (POLQA)*.
4. **ITU-R BS.1534-3**: *Method for the subjective assessment of intermediate quality level of audio systems (MUSHRA)*.
5. **IEC 60268-7**: *Sound system equipment - Part 7: Headphones and earphones*.
6. **IEC 60065 / ANSI/CTA-2051**: *Personal Sound Amplification Performance & Maximum SPL Safety Criteria*.

---

## IX. BÀI BÁO THAM KHẢO TỪ BÀI GIẢNG (LECTURE REFERENCE PAPERS)

1. **A Simple Transmit Diversity Technique for Wireless Communications** [⭐️⭐️⭐️]
   * **Tác giả**: Siavash M. Alamouti (IEEE Journal on Selected Areas in Communications, vol. 16, no. 8, pp. 1451–1458, Oct. 1998).
   * **Tệp PDF Toàn văn Nội bộ**: [`reference paper 1 A Simple Transmit Diversity Technique for Wireless Communications IEEE 1998.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Lecture%20files/Reference%20Papers/reference%20paper%201%20A%20Simple%20Transmit%20Diversity%20Technique%20for%20Wireless%20Communications%20IEEE%201998.pdf)
   * **Phân tích kỹ thuật**: Công trình kinh điển phát minh ra kỹ thuật mã hóa khối không gian - thời gian (**Alamouti Space-Time Block Coding - STBC**), cho phép đạt bậc phân tập phát 2 ($L=2$) mà không cần phản hồi trạng thái kênh về máy phát.
   * **Mô-đun hỗ trợ**: **Khối Phân tập Phát Alamouti STBC & Phân tích Đối chứng với Phân tập Thu MRC**.

2. **A Comprehensive Evaluation of Networked Music Performance Using LEO Satellite Internet: The Starlink Use Case** [⭐️⭐️]
   * **Tác giả**: Nhóm nghiên cứu Networked Music Performance (IEEE Access / AES, 2023).
   * **Tệp PDF Toàn văn Nội bộ**: [`A_Comprehensive_Evaluation_of_Networked_Music_Performance_Using_LEO_Satellite_Internet_The_Starlink_Use_Case.pdf`](file:///G:/My%20Drive/Study/VGU/VGU%20Sem5/Mobile%20Communication/Lecture%20files/Reference%20Papers/A_Comprehensive_Evaluation_of_Networked_Music_Performance_Using_LEO_Satellite_Internet_The_Starlink_Use_Case.pdf)
   * **Phân tích kỹ thuật**: Đánh giá thực nghiệm toàn diện về độ trễ, rung pha (Jitter) và hiện tượng mất gói khi truyền âm thanh biểu diễn nhạc tương tác thời gian thực.
   * **Mô-đun hỗ trợ**: **Khối Đánh giá Độ trễ và Rung pha Mạng trong Trình diễn Âm nhạc Thời gian thực**.

---

## X. BẢNG MA TRẬN ÁNH XẠ TOÀN DIỆN VÀO CÁC KHỐI FLOWGRAPH GNU RADIO

```
                                      SƠ ĐỒ KHỐI HỆ THỐNG TRONG GNU RADIO
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
 [KHỐI CHỨC NĂNG GNU RADIO]                        [TÀI LIỆU KHOA HỌC & TIÊU CHUẨN AES HỖ TRỢ TRỰC TIẾP]
─────────────────────────────────────────────────  ────────────────────────────────────────────────────────────────────
 1. Audio Source (48 kHz / 16-bit PCM)          <─  IEC 60268-7 Sound Equipment Standards
 2. Low-Delay ADPCM Codec (Nén 4:1)             <─  ⭐️ Smyth (APT-X00, elib=5400) [PDF] + Brandenburg (elib=4824)
 3. Micro-Packet Framing & Timestamp            <─  ⭐️ Flexilink (Wang & Fischer, elib=16433) [PDF] + Fonseca (elib=13190) [PDF]
 4. Convolutional FEC (Rate 1/2, K=7)           <─  Proakis Digital Comm (Chương 14 - Channel Coding)
 5. QPSK Modulation & RRC Pulse Shaping         <─  Proakis Digital Comm (Chương 12 - Digital Modulation)
 6. Stage Fading Channel (Rayleigh + Doppler)   <─  ⭐️ David Tse (Chương 2) + Goldsmith (Chương 3)
 7. Maximal Ratio Combining (MRC 2-Antennas)    <─  ⭐️ David Tse (Chương 3 - Receive Diversity MRC) + Alamouti (1998) [PDF]
 8. Carrier & Clock Sync (Costas + Polyphase)   <─  Proakis Digital Comm (Chương 12 - Synchronization)
 9. LMS Adaptive Channel Equalizer (Chống ISI)  <─  ⭐️ Proakis Digital Comm (Chương 13 - Adaptive Equalization)
 10. Viterbi Decoder & Packet Loss Concealer    <─  ⭐️ Rumsey PLC (elib=13410) [PDF] + Heinzmann Redundancy (elib=16246) [PDF]
 11. ADPCM Audio Reconstruction                 <─  Smyth (APT-X00, elib=5400) [PDF]
 12. Harman In-Ear Target Curve Equalizer       <─  ⭐️ Sean Olive (Harman Target, elib=19237, 19275) [PDF] + Struck (elib=17932) [PDF]
 13. Brickwall Safety Peak Limiter (Chống sốc)  <─  ⭐️ Nykänen (IEM Hearing Safety, elib=18649) [PDF] + IEC 60065
 14. Audio Sink (Tai nghe IEM)                  <─  Backman (Self-Calibrating IEM, elib=18722) [PDF]
 15. PEAQ Objective Difference Grade QA Script  <─  ⭐️ Thilo Thiede (PEAQ ITU-R BS.1387, elib=12078) [PDF] + POLQA (elib=16830) [PDF]
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
```

---
*Tài liệu này được tạo tự động và đồng bộ hóa từ kho dữ liệu khoa học chính thức của Audio Engineering Society (AES), hệ thống PDF nội bộ và giáo trình chuẩn VGU Sem5.*