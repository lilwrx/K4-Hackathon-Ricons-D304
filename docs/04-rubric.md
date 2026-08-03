# Rubric — 100 điểm = 25 điểm nộp checkpoint + 75 điểm chấm bài nộp

> **Phạm vi & nguyên tắc:** chấm trên artifact trong repo — mỗi con điểm trỏ về một file, phúc khảo được. Rubric chấm chuỗi quyết định và bằng chứng, không chấm mức độ hoành tráng của sản phẩm. Kết quả đo được ghi nhận trung thực — kể cả khi không đạt quality bar — vẫn được tính đủ điểm mục tương ứng; số liệu bị chỉnh sửa hoặc che giấu sẽ không được tính. Điểm vòng demo, chấm chéo zone và thưởng thêm (nếu có) thuộc thể lệ sự kiện công bố lúc khai mạc — không thuộc file này.

## PHẦN 1 — 25 ĐIỂM NỘP: mỗi checkpoint 5 điểm

| CP1 | CP2 | CP3 | CP4 | CP5 |
|:---:|:---:|:---:|:---:|:---:|
| 5 | 5 | 5 | 5 | 5 |

- **Nộp đúng hạn → 5 điểm · Nộp muộn → 0 điểm cho mốc đó.** Artifact từng mốc: xem bảng Phần 3.
- **Mỗi thành viên nộp riêng, cả nhóm dùng chung một link repo.**

## PHẦN 2 — 75 ĐIỂM CHẤM: trên artifact trong repo

| Khối | Điểm | Chấm trên file nào |
|---|---|---|
| R1 · Bằng chứng & impact | **15** | `spec.md` §1-§2 + log khảo sát/mining |
| R2 · Lát cắt & thiết kế | **15** | `spec.md` §4 |
| R3 · Chỗ khó & kịch bản rủi ro | 11 | `spec.md` §5-§6 |
| R4 · Kiểm thử | **15** | `spec.md` §7 + `eval/` |
| R5 · Prototype chạy được | 8 | `codebase/` + demo |
| R6 · Validation với user | 8 | `validation/` |
| R7 · Quy trình & repo | 3 | cấu trúc repo |

### R1 · Bằng chứng & impact — 15

| Điều kiện | Điểm |
|---|---|
| Evidence đạt chuẩn **A** (khảo sát ≥20 người ngoài nhóm, ≥50% xác nhận, log đủ câu hỏi + từng câu trả lời nguyên văn) và/hoặc **B** (số mining đếm được + ≥5 ví dụ nguyên văn + phương pháp đếm kiểm lại được) | 6 |
| Pain cụ thể: ai — đang làm gì — vướng đâu — hậu quả gì | 3 |
| Bảng impact ≥3 ứng viên có con số (bao nhiêu người × tần suất × tốn gì mỗi lần) | 3 |
| Ứng viên bị loại được giữ lại + lý do chọn bằng số | 3 |

### R2 · Lát cắt & thiết kế — 15

| Điều kiện | Điểm |
|---|---|
| Lát cắt đúng format MỘT CÂU (1 user · 1 việc · 1 quyết định AI · 1 kết quả), khớp bản build | 3 |
| ≥3 non-goals, bản build không vi phạm | 2 |
| Automation chọn rõ + lý do theo cost-of-error | 4 |
| ≥4 nguyên tắc HAX/PAIR, **mỗi nguyên tắc trỏ được vào chỗ cụ thể trong prototype** | 6 |

### R3 · Chỗ khó & kịch bản — 11

| Điều kiện | Điểm |
|---|---|
| 4 lớp chỗ khó cụ thể hoá đúng taxonomy (①②③④), không chung chung | 4 |
| ≥8 kịch bản có hành vi mong muốn, phủ đủ 4 lớp | 4 |
| 4 đường đi trải nghiệm (happy / low-confidence / failure / correction) đủ trong spec và thể hiện trong prototype | 3 |

### R4 · Kiểm thử — 15

| Điều kiện | Điểm |
|---|---|
| Golden set ≥20 case nhóm tự xây: ≥2 case/lớp chỗ khó + 8-10 case thường + 2-4 case hiếm; ≥10 case từ chatlog thật | 4 |
| Mỗi chiều chất lượng có định nghĩa kiểm chứng được (người ngoài nhóm chấm ra cùng kết quả) | 4 |
| Quality bar bằng con số, nằm trong spec.md commit trước 23:59 ngày 1, giữ nguyên sau đó | 3 |
| Bảng kết quả chạy trọn bộ ≥1 lượt, đủ mọi case kể cả case chưa đạt, có %, đối chiếu quality bar; chưa đạt thì có phân tích nguyên nhân | 4 |

### R5 · Prototype — 8

| Điều kiện | Điểm |
|---|---|
| Chạy end-to-end theo lát cắt đã khai, không can thiệp tay giữa chừng | 3 |
| ≥1 lời gọi AI thật ở quyết định trung tâm (log/trace trong repo); phần mock ghi rõ | 3 |
| Mức prototype khai báo (Sketch/Mock/Working) khớp thực tế | 2 |

### R6 · Validation với user — 8

| Điều kiện | Điểm |
|---|---|
| Feedback log ≥5 mẩu từ ≥5 người ngoài nhóm (có ≥2 willing user đã khai từ CP1), quote nguyên văn + tên/vai | 4 |
| ≥1 thay đổi từ feedback ghi trong Changelog, hoặc giữ nguyên có lý do căn cứ | 4 |

### R7 · Quy trình & repo — 3

| Điều kiện | Điểm |
|---|---|
| Repo đủ cấu trúc chuẩn (xem README) | 2 |
| README phân công có tên người cho từng phần | 1 |

### Reflection cá nhân *(chấm riêng)*

Vai trò + phần mình làm + AI hỗ trợ thế nào + một bài học từ case fail của chính nhóm — theo rubric reflection của khoá. **Vibe-coding rule:** bị hỏi tại CP5/CP6 mà không giải thích được phần có tên mình → 0 điểm phần cá nhân liên quan.

## PHẦN 3 — CHECKLIST XÁC MINH 6 MỐC *(TA xác minh theo đúng các ô dưới đây, 2 phút mỗi nhóm; nộp đúng hạn artifact của mốc = điều kiện lấy 5 điểm nộp)*

Checkpoint để giữ nhịp và cứu nhóm kẹt; artifact mỗi mốc là đầu vào của điểm chấm Phần 2.

| Mốc | K3 | K4 | Nhóm cần show | TA tích Có/Không |
|---|---|---|---|---|
| **CP1 · Canvas** | 10:00 N1 | 15:00 N1 | Canvas 7 dòng (guide §1.5): hướng · job executor · pain 1 câu · 1-2 bằng chứng đầu · lát cắt 1 câu · automation + willing users dự kiến · phân công | ☐ lát cắt đúng format 1 câu ☐ có evidence ban đầu ☐ đủ tên phân công |
| **CP2 · Bấm được** *(mốc hỗ trợ kỹ thuật — nhóm kẹt kỹ thuật gọi TA tại đây)* | 12:00 N1 | 17:00 N1 | Prototype Sketch/Mock: flow chính bấm đi hết được + commit đầu | ☐ flow chính bấm hết được ☐ repo có commit |
| **CP3 · AI thật + đo lượt đầu** | 16:00 N1 | 10:30 N2 | Lời gọi AI thật ở quyết định trung tâm + golden set ≥20 + bảng kết quả lượt 1 có % | ☐ lời gọi AI thật, không hardcode ☐ golden set đủ case khó ☐ bảng đủ mọi case (kết quả thấp không ảnh hưởng — cần ghi nhận đầy đủ, trung thực) |
| **CP4 · Chốt tiến độ** | 17:30 N1 | 12:00 N2 | Spec gần cuối + việc còn thiếu. **Hạn cứng: spec.md commit 23:59 N1, quality bar chốt từ thời điểm này** | ☐ evidence chuẩn A/B có log ☐ bảng impact + ứng viên đã loại ☐ 4 lớp cụ thể ☐ ≥4 nguyên tắc có vị trí áp dụng ☐ quality bar bằng số |
| **CP5 · Xác minh + validation + dry run** | 09:00 N2 | 14:00 N2 | Feedback log ≥5 mẩu có tên + changelog + slide final + dry run xong | ☐ log đủ ≥5 có tên ☐ 1 thành viên ngẫu nhiên giải thích được phần có tên mình ☐ dry run xong |
| **CP6 · Demo** | 10:00 N2 | 15:00 N2 | 5' trình bày (slide 6 trang, có case lỗi live + % vs bar) + 5' Q&A: thẻ giám khảo chạy 1 case lạ tại chỗ; mỗi thành viên nói ≥1 phần | — (vòng demo theo thể lệ sự kiện) |
