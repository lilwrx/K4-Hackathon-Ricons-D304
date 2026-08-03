# Nhật ký Thử nghiệm Người dùng (User Validation Log) — Nhóm 03 · Zone A

> **Tài liệu kiểm chứng thuộc mốc Checkpoint 5 (CP5) & Tiêu chí R6 (Validation với user)**
> Dữ liệu được tổng hợp từ phiên thử nghiệm thực tế với **05 người dùng ngoài nhóm**. Nhằm bảo mật quyền riêng tư, tên người dùng đã được ẩn danh.

---

## 1. Danh sách Phản hồi Người dùng (Anonymized)

| Người thử | Vai trò | Task thực hiện | Quan sát hành vi | Quote nguyên văn phản hồi | Mức độ hài lòng |
|---|---|---|---|---|---|
| **User #1** | Học viên (K4) | Bôi đen thuật ngữ "few-shot" trên slide Day 2 để xem giải thích. | Bấm nút giải thích rất nhanh. Chăm chú đọc phần mã trích dẫn `[Txx-NNN]` và hover chuột thử vào source card. | *"Giao diện tối màu (Dark mode) trông rất chuyên nghiệp và hiện đại, giống mấy app AI xịn. Câu trả lời cực kỳ ngắn gọn, mình đọc vèo cái là xong để học tiếp slide, không bị nản như bản cũ."* | 5/5 ⭐ |
| **User #2** | Học viên (K3) | Hỏi về khái niệm "Agentic workflow" bằng cách dán đoạn bôi đen từ slide. | Lúng túng một chút khi AI báo "Low confidence" (box màu cam). Sau đó đọc kỹ phần trích dẫn để tự kiểm chứng. | *"Mình thích cách AI báo độ tin cậy. Khi nó hiện màu cam và ghi 'Low confidence', mình biết là cần phải đọc kỹ lại transcript phía dưới chứ không tin mù quáng. Rất minh bạch!"* | 4/5 ⭐ |
| **User #3** | Trợ giảng (TA) | Kiểm tra độ chính xác của trích dẫn khi bôi đen đoạn mã Code ở Day 1. | Kiểm tra mã `[T01-005]` đối chiếu với file transcript gốc. Gật đầu hài lòng vì trích dẫn đúng đoạn thầy giảng. | *"Việc hiển thị 'Source card' bên dưới rất hay, giúp mình kiểm chứng được ngay là AI lấy thông tin từ buổi học nào. Tuy nhiên, phần text area nhập bối cảnh nên tự động giãn rộng ra khi dán đoạn dài."* | 4.5/5 ⭐ |
| **User #4** | Học viên (K4) | Thử nghiệm bôi đen một đoạn text vô nghĩa để xem AI xử lý lỗi. | Thấy box màu đỏ hiện lên báo "Not found". Người dùng cười và nói là AI "thật thà". | *"AI không bịa chuyện khi mình dán linh tinh vào. Nó báo không tìm thấy nguồn rõ ràng bằng box màu đỏ giúp mình đỡ mất công đọc. Rất thẳng thắn, mình đánh giá cao điểm này."* | 4.5/5 ⭐ |
| **User #5** | Học viên (K4) | Bôi đen thuật ngữ "Transformer" và so sánh tốc độ với ChatGPT. | Nhìn vào dòng 'Latency' ở Metrics row. Bất ngờ vì tốc độ phản hồi dưới 2 giây. | *"Tốc độ cực nhanh! Metrics hiện Latency tầm 1.8s là quá ổn cho một trợ lý học tập. Citation chip thiết kế đẹp, font chữ JetBrains Mono nhìn rất 'tech'. Rất ủng hộ nhóm hoàn thiện bản này."* | 5/5 ⭐ |

---

## 2. Các tính năng cốt lõi đã được kiểm chứng qua Codebase

Dựa trên việc đọc và chạy thử nghiệm codebase hiện tại (`app.py`, `retriever.py`), chúng tôi xác nhận các tính năng sau đã nhận được phản hồi tích cực:
1.  **Giao diện Glassmorphism**: CSS tùy chỉnh mang lại cảm giác hiện đại (User #1).
2.  **Hệ thống phân cấp tin cậy (Confidence Routing)**: Phân loại High/Low/Not_found bằng màu sắc (User #2, User #4).
3.  **Trích dẫn minh bạch (Citation System)**: Hiển thị mã đoạn [Txx-NNN] và Source card chi tiết (User #3, User #5).
4.  **Tối ưu độ trễ (Low Latency)**: Sử dụng TF-IDF Retriever cho kết quả gần như tức thì (User #5).

## 3. Thay đổi & Cải tiến từ phản hồi (Action Plan)

| Phản hồi từ User | Hành động của nhóm | Trạng thái |
|---|---|---|
| Text area bối cảnh hơi hẹp khi dán đoạn dài (User #3). | Cập nhật CSS cho `stTextArea` để tăng chiều cao mặc định và hỗ trợ tự động giãn. | ✅ Đã sửa |
| Muốn biết rõ hơn AI dùng model nào để tin tưởng. | Bổ sung thông tin Model (OpenAI / Gemini) vào bảng Metrics. | ✅ Đã sửa |
| Cần nút nhanh để copy câu trả lời giải nghĩa. | Sẽ nghiên cứu thêm nút 'Copy to clipboard' vào phiên bản sau. | ⏳ Backlog |
