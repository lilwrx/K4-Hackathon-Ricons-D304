# Worksheet JTBD đầy đủ
# Worksheet B1 — Chân dung user & Jobs To Be Done

**Nhóm:** VLearn AI Tutor · **Hướng:** [x] A — VLearn [ ] B — Trợ lý Học viên [ ] C — Làn mở

## 1. Chọn job executor 

**Job executor của nhóm:** Học viên đang học trên nền tảng VLearn, đọc slide/bài giảng và dùng AI tutor khi chọn đoạn khó.

**Vì sao là người này:** Dữ liệu chatlog gốc ghi nhận 1.261 lượt học viên/tutor trong lớp, 99.3% tin nhắn học viên bắt đầu với đoạn được chọn trên slide `(Trang X, đoạn được chọn...)`, cho thấy trải nghiệm cốt lõi là học viên trong buổi đang cần giải thích tức thì.

## 2. Vẽ workflow thật

| Chặng | Họ đang cố làm gì? | Hôm nay họ dùng gì? | Kẹt ở đâu? | Mức đau |
|---|---|---|---|---|
| Trước buổi | Chuẩn bị nội dung trước, xem slide/bài, cố gắng hiểu thuật ngữ và điểm chính. | Tua video, đọc slide, ghi chú cũ. | Không biết chỗ nào cần giải thích; nếu gặp chỗ khó phải quay lại toàn bộ nội dung. | M |
| Trong buổi | Đọc slide, chọn đoạn chưa hiểu và hỏi AI tutor để giải thích ngay. | AI tutor tích hợp trên VLearn, đôi khi cũng hỏi bạn/bạn cùng lớp. | AI trả lời chung chung, không dẫn trang/trích dẫn; dễ mất nhịp học. | H |
| Ngay sau buổi | Kiểm tra lại phần chưa hiểu, so sánh với bài giảng và tìm thêm ví dụ. | Xem lại slide/video, hỏi AI tutor hoặc search ngoài. | Phải tua lại nhiều, không biết chỗ chính xác trong tài liệu. | M/H |
| Khi ôn lại | Ôn lại kiến thức từng phần, kiểm tra hiểu bằng quiz hoặc đọc lại slide. | Tua video, ChatGPT/Google, note cũ. | Nếu không có lời giải ngay, mất thời gian xác định đoạn cần ôn. | M |

**Hai chỗ đau nhất trong workflow:** #1 Trong buổi: cần làm rõ ngay đoạn slide khó mà không rời giao diện học. #2 Ngay sau buổi/ôn lại: AI thiếu grounding/trích dẫn, làm giảm tin tưởng và phải tự dò lại.

**Bằng chứng ban đầu cho 2 chỗ này** (từ chatlog/Discord/tự quan sát — sẽ đào sâu ở Bước 2):
- Chatlog 22/07–29/07/2026 có 1.261 turns, 46.2% tutor trả lời không có citations
- Sample tutor response: "Học máy có thể tự học từ dữ liệu." khi học viên hỏi "Học máy khác gì với AI?" và không có trang dẫn.

## 3. Viết core JTBD 

- Chưa tốt: `hỏi AI tutor về bài học`
- Tốt hơn: `làm rõ ngay chỗ vừa đọc không hiểu mà không phải rời trang tài liệu`
- Chưa tốt: `dùng AI ôn tập`
- Tốt hơn: `tìm lại đúng đoạn giảng viên giải thích một khái niệm trong vài phút thay vì tua cả buổi`

**Core JTBD bản nháp:** làm rõ ngay đoạn slide/bài giảng đang đọc khi không hiểu, mà không phải rời khỏi trang học.

**Từ solution lỡ nhét vào (gạch bỏ):** AI tutor / bôi đen và hỏi.

**Core JTBD bản chốt:** làm rõ ngay đoạn slide/bài giảng đang đọc khi không hiểu, mà không phải rời khỏi trang học.

## 4. Ba job stories 

| # | Khi tôi | Tôi muốn | Để tôi có thể | Story này cho thấy gì |
|---|---|---|---|---|
| JS1 | Đang đọc slide và bôi đen một cụm từ khó hiểu, | Có một lời giải thích ngắn gọn dựa trên nội dung đã chọn, | Tiếp tục học mà không phải rời khỏi trang bài giảng. | Cần giải thích tức thì ngay trên slide. |
| JS2 | Hỏi gia sư về một đoạn đã chọn và câu trả lời có vẻ chung chung, | Câu trả lời có kèm theo nguồn trang hoặc tham chiếu đến slide, | Tin tưởng vào câu trả lời và không lãng phí thời gian xác minh ở nơi khác. | Cần grounding/citation để tin tưởng. |
| JS3 | Ôn lại bài sau giờ học và nhớ ra một khái niệm hóc búa, | AI sử dụng chính xác ngữ cảnh đã được bôi đen từ slide gốc, | Nhanh chóng xác nhận lại kiến thức của mình thay vì phải xem lại toàn bộ video. | Cần giữ liên hệ với nội dung cụ thể đã chọn. |

## 5. Current alternatives

| Alternative | Làm tốt gì? | Fail ở đâu? | Vì sao user chưa bỏ nó? |
|---|---|---|---|
| Hỏi AI tutor hiện tại | Có sẵn trong giao diện VLearn, nhanh, không phải rời trang. | Nhiều trả lời thiếu citation, không bám đúng đoạn highlight. | Đã là luồng chính trong lớp và là cách nhanh nhất để liên hệ với nội dung bài học. |
| Tua video / đọc lại slide | Giúp kiểm tra chính xác nguồn gốc nội dung. | Mất thời gian, phải tua lại dài, không biết chỗ cụ thể. | Vì không có cách nhanh hơn và cần rõ ràng hơn. |
| Hỏi bạn/TA ngoài | Có thể nhận được giải thích bằng ngôn ngữ quen thuộc. | Không phải lúc nào cũng có người trả lời ngay, và câu trả lời có thể khác nguồn tài liệu. | Vì cần tương tác thật, nhưng team/TA không luôn sẵn sàng. |

**Nếu sản phẩm nhóm không ra đời, user sẽ tiếp tục:** dùng AI tutor hiện tại với độ tin cậy thấp, tua lại video, hoặc bỏ qua chỗ hiểu sai.

## 6. AI leverage point

**AI nên vào bước nào của workflow, vai trò gì:** Trong bước "execute" khi học viên đã chọn đoạn slide/bài cần giải thích, AI nên cung cấp câu trả lời gắn với nội dung đó và kèm citation nguồn.

**Vì sao không phải bước khác:** Bước trước (prepare) chưa phải vấn đề chính; user đã ở trong buổi và cần giải quyết ngay. Bước sau (review) tùy chọn, nhưng nếu bước execute đến nơi thì review cũng giảm đau.

**Product hypothesis** (công thức): *Nếu giúp học viên trong buổi học làm rõ ngay đoạn slide/bài giảng đang đọc bằng AI tutor trả lời dựa trên nội dung highlight và kèm citation, họ sẽ chuyển từ dùng tutor hiện tại/tua video/bạn cùng lớp sang giải pháp nhóm, vì họ nhận được câu trả lời tin cậy ngay tại chỗ.*
> Nếu giúp học viên trong buổi làm rõ ngay đoạn slide/bài giảng đang đọc bằng AI tutor trả lời dựa trên nội dung highlight và kèm citation, họ sẽ chuyển từ dùng tutor hiện tại/tua video/bạn cùng lớp sang giải pháp nhóm, vì họ có thể tiếp tục học mà không mất nhịp.

**Assumption nguy hiểm nhất nếu nhóm đang sai** (sẽ kiểm bằng evidence + vòng validation CP5): học viên thực sự cần citation và grounding từ AI ngay trong buổi học, chứ không chỉ một câu trả lời tóm tắt chung chung. Nếu assumption này sai, thì cải tiến citation sẽ không tăng giá trị.  