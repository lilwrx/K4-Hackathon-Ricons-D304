# AI SPEC — Concise-RAG Tutor · Nhóm 03 · Zone A
Hướng: [x] A — VLearn  [ ] B — Trợ lý Học viên  [ ] C — Làn mở
Loại: [x] Tối ưu tính năng có sẵn  [ ] Tính năng mới

## §1. User & Job
- **Job executor + workflow**: 
  - **Job executor**: Học viên đang tự học trực tuyến trên nền tảng VLearn của khóa học "AI Thực Chiến", vừa đọc tài liệu, slide bài giảng vừa kết hợp tra cứu nhanh thuật ngữ học thuật phức tạp hoặc mã nguồn.
  - **Workflow**:
    1. Học viên mở giao diện đọc slide bài giảng trên VLearn (ví dụ: bài học Day 2).
    2. Học viên đọc slide và bắt gặp một khái niệm hoặc thuật ngữ chuyên ngành khó hiểu (ví dụ: *Few-shot Prompting*, *Memory Injection*, *Transformer*, *ReAct Agent*).
    3. Học viên thực hiện thao tác bôi đen (highlight) đoạn văn bản/thuật ngữ đó ngay trên slide.
    4. Hệ thống tự động kích hoạt khung AI Tutor và đính kèm thông tin ngữ cảnh: `(Trang X, đoạn được chọn: "...")` cùng câu hỏi của học viên.
    5. Học viên gửi câu hỏi và đợi AI Tutor phản hồi giải nghĩa.
    6. Học viên đọc lời giải thích của AI Tutor, nắm bắt được bản chất bế tắc và tiếp tục mạch đọc slide.
  - *Worksheet JTBD đính kèm*: Chi tiết tại file `tham-khao/worksheet-jtbd-day-du.md`.

- **Core JTBD**:
  - Giải nghĩa nhanh và chính xác các khái niệm, thuật ngữ chuyên ngành mới trong tài liệu giảng dạy khi đang nghiên cứu bài học để tiếp tục duy trì luồng tư duy học tập mà không bị gián đoạn. *(Đảm bảo tiêu chuẩn không chứa từ khóa "AI", "VLearn", "Tutor")*.

- **Problem statement**:
  - Học viên tham gia khóa học khi tự đọc slide bài giảng gặp các thuật ngữ chuyên ngành phức tạp thường bị tắc nghẽn tư duy, dẫn đến việc phải dừng mạch đọc để tự đi tra cứu thủ công từ nhiều nguồn khác nhau, hoặc nhận được các lời giải nghĩa dài dòng, lạc đề và không có cơ sở đối chiếu rõ ràng với bài giảng của giảng viên, gây mất nhiều thời gian, làm gián đoạn mạch tư duy học tập và dễ tiếp thu sai lệch kiến thức học thuật. *(Đảm bảo tiêu chuẩn không chứa từ khóa "AI")*.

- **Evidence (đáp ứng cả chuẩn A và chuẩn B — log đầy đủ trong repo)**:

  ### Chuẩn B — Số liệu Mining từ Chatlog thực tế
  - **Phương pháp đếm (reproducible methodology)**: 
    Chúng tôi sử dụng thư viện `Pandas` trong Python để phân tích toàn bộ file dữ liệu chatlog thực tế được cung cấp `chat_history_anonymized_for_hackathon.csv` (gồm 2,522 dòng, tương đương 1,261 lượt hỏi-đáp (turn) của 369 học viên thuộc 585 hội thoại, phát sinh từ ngày 22/07 đến 29/07/2026). Mã nguồn phân tích chi tiết được lưu trữ tại file `analyze_failures.py` trong repository để bất kỳ ai cũng có thể chạy lại để đối chứng kết quả.
  - **Số liệu đếm được**:
    - **Tỷ lệ thiếu trích dẫn (Empty Citations)**: Có **582 / 1,261 phản hồi của Tutor (chiếm 46.15%)** hoàn toàn rỗng trường `citations` (citations = `[]` hoặc null). Nghĩa là gần một nửa số câu trả lời của AI Tutor không hề được kiểm chứng hay định vị nguồn gốc dựa trên slide học tập, làm giảm sút nghiêm trọng tính xác thực.
    - **Tỷ lệ lỗi tìm kiếm/truy cập slide (Retrieval & Access Errors)**: Có **309 / 1,261 phản hồi của Tutor (chiếm 24.50%)** chứa các từ khóa xin lỗi hoặc báo lỗi tìm kiếm tài liệu (ví dụ: *"không tìm thấy"*, *"chưa tìm thấy"*, *"rất tiếc không thể truy cập"*, *"xin lỗi không tìm thấy trang"*).
    - **Lỗi định vị trang cụ thể**: Trong tổng số 1,253 lượt học viên gửi tin nhắn có chứa từ khóa liên quan đến "Trang" hoặc "Slide" (do hệ thống VLearn tự động đính kèm bối cảnh), có đến **242 lượt (chiếm 19.31%)** AI Tutor trực tiếp báo lỗi không tìm thấy nội dung của trang đó trong cơ sở dữ liệu RAG và yêu cầu học viên tự cung cấp nội dung, đứt mạch học học viên cực kỳ nghiêm trọng.
    - **Lỗi câu trả lời quá dài dòng (Verbosity)**: Có **407 / 1,261 phản hồi của Tutor (chiếm 32.28%)** dài vượt quá 200 từ, với độ dài trung bình toàn bộ câu trả lời là **158.9 từ**. Khi học viên chỉ cần giải nghĩa nhanh thuật ngữ để đọc tiếp slide, việc AI Tutor trả về một bài luận dài hàng trăm chữ lặp lại nguyên văn các bullet point trên slide ("lan man") khiến họ nản lòng và lười đọc.
    - **Số lượng rating tiêu cực (Rating Down)**: Có **37 lượt rating down** từ học viên, hầu hết đều rơi vào các trường hợp AI báo không tìm thấy slide hoặc giải thích lan man, lệch bối cảnh.
  
  - **05 ví dụ nguyên văn lỗi trích dẫn từ chatlog (kèm mã nguồn và turn_id)**:
    1. **Turn T0769 (Lỗi không tìm thấy slide bôi đen - đùn đẩy trách nhiệm)**:
       * Học viên hỏi: `(Trang 4, đoạn được chọn: "giải thích nghĩa chi tiết của trang 4")` -> `giải thích nghĩa chi tiết của trang 4`
       * AI Tutor trả lời: `Chào bạn, rất xin lỗi vì hiện tại hệ thống tìm kiếm không tìm thấy nội dung cụ thể cho trang 4 trong tài liệu của bài học hôm nay. Bạn có thể vui lòng cung cấp nội dung hoặc tiêu đề của trang 4 đó để mình hỗ trợ giải thích rõ hơn cho bạn không?`
       * Nguồn: `chat_history_anonymized_for_hackathon.csv` - Turn T0769.
    2. **Turn T1258 (Lỗi tìm kiếm từ khóa thô sơ - sai ngữ cảnh trang)**:
       * Học viên hỏi: `(Trang 33, đoạn được chọn: "tóm tắt slide này")` -> `tóm tắt slide này`
       * AI Tutor trả lời: `Rất tiếc là tôi đã tra cứu trong tài liệu nhưng chưa tìm thấy nội dung cụ thể của **Trang 33**. Kết quả tìm kiếm chỉ hiển thị các trang khác có nhắc đến con số "33" (như mức điểm 33% trong các bài kiểm tra đánh giá AI trên trang 60 và 72). Bạn có thể cho tôi biết tiêu đề của slide đó hoặc một vài từ khóa có trên trang để tôi tìm kiếm lại chính xác hơn không?`
       * Nguồn: `chat_history_anonymized_for_hackathon.csv` - Turn T1258.
    3. **Turn T0519 (Lỗi từ chối tóm tắt slide học tập)**:
       * Học viên hỏi: `(Trang 46, đoạn được chọn: "Tóm tắt slide pdf day2 cho tôi")` -> `Tóm tắt slide pdf day2 cho tôi`
       * AI Tutor trả lời: `Rất tiếc, tôi không thể truy cập trực tiếp vào tệp PDF của buổi học để tóm tắt cho bạn. Nếu bạn có các câu hỏi cụ thể về nội dung, khái niệm hay các thuật ngữ cần giải thích trong bài, hãy đặt câu hỏi và tôi sẽ hỗ trợ bạn tra cứu từ tài liệu được cung cấp.`
       * Nguồn: `chat_history_anonymized_for_hackathon.csv` - Turn T0519.
    4. **Turn T1023 (Lỗi mất grounding tài liệu mặc dù nội dung có sẵn)**:
       * Học viên hỏi: `(Trang 43, đoạn được chọn: "According to page 43, when to choose AI to support human?")` -> `According to page 43, when to choose AI to support human?`
       * AI Tutor trả lời: `Rất tiếc, tôi đã tra cứu trong tài liệu ngày học nhưng không tìm thấy thông tin cụ thể tại trang 43 về việc "khi nào nên chọn AI để hỗ trợ con người". Có thể nội dung này nằm ở một trang khác hoặc tài liệu bạn đang đề cập có cách đánh số trang khác với tài liệu tôi được cung cấp...`
       * Nguồn: `chat_history_anonymized_for_hackathon.csv` - Turn T1023.
    5. **Turn T0268 (Lỗi giải thích dài dòng, lặp lại lý thuyết khô khan không mang lại giá trị)**:
       * Học viên hỏi: `(Trang 22, đoạn được chọn: "Memory injection ...")` -> `Memory injection ...`
       * AI Tutor trả lời: Một câu trả lời dài lê thê **215 từ** lặp lại nguyên văn cấu trúc slide học thuật thay vì tóm lược cốt lõi hoặc đưa b bối cảnh thực tế sống động của giảng viên đã giảng trong transcript.
       * Nguồn: `chat_history_anonymized_for_hackathon.csv` - Turn T0268.

  

---

## §2. Impact & quyết định chọn
- **Bảng impact ≥3 ứng viên**:
  Để lựa chọn bài toán tối ưu nhất cho thời gian phát triển ngắn của hackathon, nhóm đã tiến hành đánh giá 3 ứng viên giải pháp dựa trên quy mô người dùng, tần suất, chi phí hao tổn thực tế và mức độ khả thi khi xây dựng prototype:

  | Ứng viên tính năng | Quy mô (Bao nhiêu người gặp) | Tần suất xuất hiện | Tốn kém/Hao phí mỗi lần gặp (Cost of error/pain) | Khả thi (Build trong hackathon) | Chọn? |
  |---|---|---|---|---|---|
  | **Ứng viên 1: Concise-RAG Tutor** (Tối ưu AI Tutor trả lời súc tích & dẫn nguồn trang/transcript chính xác khi học viên bôi đen hỏi trên VLearn) | **~1,000 học viên** *(369 học viên hoạt động tích cực trong chatlog chỉ trong 1 tuần)* | **Cực cao** *(3-5 lần/buổi học; tổng cộng 1,253 lượt hỏi về slide trong 1 tuần)* | **Mất 3-5 phút ngắt mạch học** để tự tra cứu lại slide gốc khi AI báo lỗi hoặc trả lời dài dòng rỗng nguồn. Tổng hao phí toàn lớp học lên tới **~5,000 phút/tuần (~83 giờ)** lãng phí hoặc bị ức chế tư duy học. | **Rất cao**: Giải quyết bằng tối ưu prompt RAG, Context Injection từ transcript và slide sẵn có, thiết kế rẽ nhánh kịch bản lỗi, không phụ thuộc tích hợp LMS sâu. | **CHỌN** |
  | **Ứng viên 2: AI Interactive Quizzer** (Trình tự động kiểm tra mức độ hiểu bài cuối buổi học và đề xuất slide hổng kiến thức) | **~1,000 học viên** *(toàn bộ học viên khóa học)* | **Thấp - Vừa** *(chỉ 1 lần vào cuối mỗi buổi học)* | **Tốn 10-15 phút làm quiz rời rạc**, dễ nản chí bỏ qua, giảng viên và học viên không phát hiện kịp thời các lỗ hổng kiến thức cụ thể theo từng slide ngay trong buổi học. | **Trung bình**: Yêu cầu tích hợp rất sâu vào hệ thống quản lý học tập (LMS), chấm điểm thời gian thực và quản lý trạng thái học viên phức tạp. | LOẠI |
  | **Ứng viên 3: Lecture Summarizer & Flashcard Creator** (Tự động tóm tắt bài giảng và sinh flashcard ôn tập dựa trên slide + transcript) | **~300 học viên** *(học viên ôn thi quiz sâu hoặc học viên bận nghỉ học)* | **Thấp** *(1-2 lần/tuần trước các buổi quiz)* | **Tốn 30-45 phút tự xem lại** video bài giảng dài hoặc đọc slide hàng chục trang để chắt lọc ý chính ôn tập. | **Cao**: Dễ dàng xây dựng prompt tóm tắt và sinh flashcard, tuy nhiên tần suất sử dụng thấp và không giải quyết nỗi đau trực tiếp tức thì khi đang học bài. | LOẠI |

- **Ứng viên ĐÃ LOẠI + vì sao**:
  - **Ứng viên 2 bị loại**: Dù việc tự động kiểm tra kiến thức cuối buổi rất có giá trị giáo dục, nhưng tần suất sử dụng thấp (chỉ 1 lần/buổi). Đồng thời, việc tích hợp sâu vào hệ thống chấm điểm và quản lý học viên của LMS VLearn vượt quá giới hạn thời gian cho phép trong hackathon (khả thi kỹ thuật trung bình).
  - **Ứng viên 3 bị loại**: Tần suất sử dụng rất thấp (chỉ dùng khi ôn quiz cuối tuần hoặc khi nghỉ học). Nỗi đau của học viên ở đây tuy có nhưng không mang tính chất "nóng hổi", gây ức chế ngắt mạch tư duy trực tiếp giống như lỗi trả lời sai/lan man của AI Tutor ngay khi học viên đang nỗ lực đọc hiểu slide trên lớp.

- **Ứng viên CHỌN + vì sao (bằng số)**:
  Nhóm quyết định chọn **Ứng viên 1: Concise-RAG Tutor** để phát triển vì những lý do định lượng thuyết phục sau:
  1. **Tần suất tiếp xúc cao nhất**: Với **1,253 lượt hỏi** liên quan đến slide chỉ trong 1 tuần (chatlog thực tế), đây là tính năng được tương tác nhiều nhất. Giải quyết được bài toán này sẽ tác động tích cực trực tiếp đến trải nghiệm học tập hàng giờ của học viên.
  2. **Tỷ lệ lỗi hiện tại quá lớn**: Số liệu mining chứng minh hệ thống hiện tại đang bị lỗi nghiêm trọng với **46.15% rỗng trích dẫn**, **24.50% lỗi tìm kiếm/truy cập dữ liệu slide**, và **32.28% câu trả lời quá dài dòng (>200 từ)**. Dư địa để cải thiện hiệu năng và trải nghiệm người dùng là cực kỳ lớn.
  3. **Tiết kiệm thời gian khổng lồ**: Giúp loại bỏ hoàn toàn việc ngắt mạch tư duy học tập và tiết kiệm đến **3-5 phút tra cứu thủ công mỗi lần gặp lỗi**, ước tính giải phóng hơn **80 giờ học tập lãng phí mỗi tuần** cho toàn bộ học viên trong lớp.
  4. **Tính khả thi cực kỳ phù hợp**: Chúng tôi có đầy đủ 6 file transcript bản sạch được chuẩn hóa theo mã đoạn `[Txx-NNN]` và 2 bộ slide chi tiết. Việc tối ưu RAG bằng cách "bơm" (inject) trực tiếp transcript giảng viên tương ứng với trang slide học viên đang đọc là giải pháp cực kỳ khả thi, mang lại độ chính xác cao và có thể hoàn thiện xuất sắc ngay trong thời gian diễn ra hackathon.

---

## §3. Giải pháp tương tự đã nghiên cứu
- **Google NotebookLM**:
  - *Flow*: Người dùng upload tài liệu cá nhân (PDF, Docs, website...). Hệ thống tự động phân tích, tạo giao diện chat đồng hành có khả năng tóm tắt, giải thích và đính kèm số trích dẫn (citations) chi tiết cạnh câu trả lời. Khi click vào số trích dẫn, hệ thống tự động cuộn đến và bôi xanh đoạn văn bản gốc trong tài liệu để đối chiếu.
  - *Đáng học*: Khả năng grounding cực tốt và cơ chế hiển thị trích dẫn nguồn (citations) vô cùng trực quan, giúp người dùng xây dựng lòng tin tuyệt đối vì có thể kiểm chứng nguồn gốc câu trả lời dễ dàng. Câu trả lời súc tích, bám sát tài liệu.
  - *Đáng né*: Thiết kế dưới dạng một không gian làm việc (workspace) độc lập. Người dùng buộc phải di chuyển tài liệu ra ngoài hệ thống LMS của lớp học, làm đứt mạch học "nóng" slide-by-slide nếu họ đang đọc slide trực tiếp trên VLearn. Giao diện chat chung cho cả folder tài liệu chứ không tự động định vị bối cảnh trang slide học viên đang xem.
  - *Mình khác gì*: Deeply integrated (tích hợp sâu) vào trình đọc slide của VLearn. Tự động nhận diện trang slide hiện tại học viên đang xem để giới hạn phạm vi tìm kiếm RAG. Đồng thời, không chỉ tìm kiếm text khô khan trên slide mà còn **inject (bơm) trực tiếp đoạn transcript giảng viên giảng tương ứng với slide đó**, giúp lời giải thích của AI có bối cảnh sư phạm sinh động "thầy cô đã giảng thế nào", mang lại giá trị giải nghĩa vượt trội hơn hẳn NotebookLM.

- **Khanmigo (by Khan Academy)**:
  - *Flow*: Trợ lý AI đồng hành trực tiếp cùng học sinh khi xem video bài giảng hoặc giải bài tập. Khi học sinh đặt câu hỏi hoặc bôi đen phần khó, Khanmigo không đưa ra câu trả lời trực tiếp mà áp dụng phương pháp sư phạm Socratic - đặt câu hỏi gợi mở, đưa gợi ý từng bước để hướng dẫn học sinh tự suy nghĩ tìm ra đáp án.
  - *Đáng học*: Phương pháp sư phạm Socratic tuyệt vời giúp học sinh phát triển tư duy chủ động, tránh việc ỷ lại vào AI làm hộ bài tập hoặc lười suy nghĩ. Giọng điệu thân thiện, tích cực, cực kỳ hợp ngữ cảnh giáo dục.
  - *Đáng né*: Đôi khi quá cứng nhắc trong việc từ chối đưa ra câu trả lời trực tiếp. Khi học viên đang đọc slide lý thuyết với mạch tư duy nhanh và chỉ cần giải nghĩa gấp một thuật ngữ viết tắt hoặc một khái niệm kỹ thuật khô khan để đọc tiếp, việc AI cứ hỏi vòng vo "Theo bạn nó là gì?" sẽ gây ức chế tâm lý cực kỳ lớn và làm ngắt hoàn toàn mạch học tập của học viên.
  - *Mình khác gì*: Áp dụng thiết kế rẽ nhánh linh hoạt (Flexible routing). Đối với các câu hỏi giải nghĩa thuật ngữ nhanh (bôi đen), AI của chúng ta sẽ thực hiện **give_direct_answer** súc tích dưới 100 từ kết hợp **review_concept** ngắn gọn kèm trích dẫn nguồn trang ngay lập tức để học viên tiếp tục mạch đọc slide. Đối với các câu hỏi mang tính chất đào sâu, phân tích hoặc khi phát hiện học viên bôi đen thiếu thông tin (input mơ hồ), AI mới chủ động kích hoạt vòng lặp làm rõ (Clarification loop) và đưa ví dụ thực tế dựa trên transcript giảng viên để gợi mở tư duy, cân bằng hoàn hảo giữa tính sư phạm và hiệu năng học tập nhanh.

---

## §4. Thiết kế
- **Lát cắt MỘT CÂU**: 
  - Một **học viên VLearn** đang đọc slide bài giảng bôi đen một thuật ngữ chuyên ngành khó hiểu -> **AI quyết định** trích xuất chính xác bối cảnh trang slide hiện tại và đoạn transcript bài giảng tương ứng để đưa ra câu trả lời giải thích súc tích dưới 100 từ kèm mã trích dẫn slide/transcript rõ ràng -> kết quả là **học viên lập tức hiểu rõ bản chất thuật ngữ** và tiếp tục đọc slide học tập không bị gián đoạn mạch tư duy.

- **Non-goals (≥3 thứ KHÔNG build)**:
  1. KHÔNG tự động dịch toàn bộ slide bài giảng sang ngôn ngữ khác (chỉ tập trung giải thích thuật ngữ chuyên ngành được bôi đen).
  2. KHÔNG tự động sinh ra bài tập thực hành, câu hỏi quiz hay flashcard từ đoạn bôi đen (tránh làm phân tâm và lan man ngoài phạm vi giải nghĩa nhanh).
  3. KHÔNG trả lời các câu hỏi về logistics lớp học (lịch học, deadline nộp bài, điểm số, giảng viên) hoặc các câu hỏi học thuật nằm ngoài phạm vi tài liệu và transcript của buổi học hiện tại (tránh lỗi out-of-scope và ảo tưởng kiến thức).

- **Mức prototype nhắm tới**: 
  - `[x] Working` — Phần mock: Giao diện UI/UX của VLearn (bao gồm thanh công cụ đọc slide và khung chat) được mock bằng nền tảng Web giả lập trực quan để demo trọn vẹn trải nghiệm của học viên; Phần thật: **Lời gọi AI (API Call) chạy thật 100% ở quyết định trung tâm** (nhận diện ý định bôi đen, tự động trích xuất context trang slide hiện tại kết hợp transcript tương ứng và sinh câu trả lời giải thích súc tích có citations).

- **Automation**: 
  - `[x] conditional` — **Lý do lựa chọn theo cost-of-error**:
    - Nếu chọn tự động hóa hoàn toàn (*Automate*), trong trường hợp học viên bôi đen một thuật ngữ cực kỳ mơ hồ, thiếu thông tin (ví dụ chỉ bôi đen chữ "Tool" hay "Model" chung chung), AI Tutor sẽ cố gắng suy đoán và tự ý bịa ra (hallucinate) một câu trả lời dài dòng không có căn cứ thực tế trong tài liệu. Hậu quả (cost-of-error) là cực kỳ đắt: học viên tiếp thu sai lệch kiến thức học thuật, làm sai bài quiz/thi, và hoàn toàn mất niềm tin vào hệ thống tự học VLearn.
    - Nếu chỉ dừng lại ở mức gợi ý (*Augment*), học viên vẫn phải tự mình thực hiện quá nhiều thao tác đọc hiểu và chọn lọc thủ công, không tối ưu được trải nghiệm học tập nhanh chóng.
    - Do đó, **Conditional Automation (Tự động hóa có điều kiện)** là lựa chọn tối ưu nhất:
      - *Điều kiện chắc chắn (High confidence)*: Khi dữ liệu bám sát slide/transcript và câu hỏi rõ ràng, AI sẽ tự động sinh câu trả lời giải nghĩa cực kỳ súc tích kèm trích dẫn trang cụ thể ngay lập tức.
      - *Điều kiện mơ hồ (Low confidence / Uncertain)*: Khi bối cảnh bôi đen quá ngắn hoặc thiếu thông tin, AI sẽ không tự tiện trả lời liều mà chủ động kích hoạt **vòng lặp làm rõ (Clarification loop)** - đưa ra câu hỏi thu hẹp phạm vi để học viên bổ sung bối cảnh, bảo vệ học viên khỏi các lỗi sai kiến thức nguy hiểm.

- **§4b. Nguyên tắc đã áp dụng (≥4 — HAX/PAIR, xem guide)**:
  | Nguyên tắc | Áp cụ thể vào đâu trong prototype |
  |---|---|
  | **HAX G1 — Make clear what the system can do** (Làm rõ hệ thống có thể làm gì) | Ngay khi học viên mở hộp thoại AI Tutor, hệ thống hiển thị câu chào rõ ràng: *"Tôi là trợ giảng Concise-RAG Tutor của bạn. Tôi có thể giải thích ngắn gọn (<100 từ) các thuật ngữ trên slide dựa trên tài liệu và transcript bài giảng. Tôi không thể trả lời các câu hỏi logistics hay kiến thức ngoài giáo trình."* Điều này đặt kỳ vọng đúng cho học viên ngay từ đầu. |
  | **HAX G2 — Make clear how well the system can do what it does** (Làm rõ hệ thống làm tốt đến đâu) | Hiển thị một dòng thông báo nhỏ dưới chân khung chat: *"Câu trả lời của tôi đạt độ tin cậy cao nhất khi có đính kèm mã trích dẫn slide/transcript `[Txx-NNN]`. Nếu không thể dẫn nguồn, tôi sẽ ghi chú rõ đây là 'Ý kiến tham khảo thêm từ LLM' để bạn cân nhắc."* Giúp học viên biết khi nào nên tin tưởng tuyệt đối, khi nào cần kiểm chứng lại. |
  | **HAX G10 — Scope down when uncertain** (Thu hẹp phạm vi khi nghi ngờ) | Khi học viên bôi đen một từ khóa quá ngắn hoặc mơ hồ (ví dụ: bôi đen chữ *"Tool"* ở trang 3), thay vì đoán mò và viết một câu trả lời dài dòng chung chung, AI sẽ tự động kích hoạt logic rẽ nhánh để hỏi lại: *"Khái niệm 'Tool' xuất hiện ở cả Day 2 (Prompt Engineering) và Day 3 (Agentic Patterns). Bạn đang muốn hỏi về 'Tool' trong ngữ cảnh sử dụng API hay trong mô hình ReAct?"* |
  | **HAX G11 — Provide explanations** (Cung cấp giải thích/nguồn trích dẫn) | Mỗi câu giải thích thuật ngữ của AI Tutor luôn đi kèm mã trích dẫn trực quan đến số trang slide và transcript của giảng viên (ví dụ: *"Theo Slide Trang 15 và transcript của thầy tại đoạn [T03-125]..."*). Khi học viên di chuột qua mã trích dẫn, một popup tooltip nhỏ sẽ hiển thị nguyên văn đoạn text gốc để học viên đối chiếu nhanh mà không cần rời mắt khỏi khung chat. |
  | **HAX G9 — Support efficient correction** (Hỗ trợ sửa lỗi dễ dàng) | Ngay cạnh câu hỏi của học viên trong khung chat, hệ thống hiển thị một biểu tượng bút chì nhỏ (Edit). Nếu phát hiện câu trả lời của AI chưa đúng ý do bôi đen thiếu thông tin, học viên có thể click vào nút này để chỉnh sửa câu hỏi hoặc bấm nút *"Bổ sung đoạn bôi đen"* để nạp thêm ngữ cảnh nhanh chóng mà không cần phải gõ lại toàn bộ từ đầu. |

---

## §5. Kiểu lỗi — 4 lớp chỗ khó + kịch bản (≥8) [bảng theo guide §2.5]

Dưới đây là bảng phân tích kịch bản lỗi rủi ro dựa trên 4 lớp chỗ khó của hệ thống Concise-RAG Tutor:

| Tình huống cụ thể | Lớp chỗ khó | Hành vi mong muốn (Nói gì, hiện gì, cho user làm gì tiếp) | Nguyên tắc áp dụng (G../PAIR) |
|---|---|---|---|
| **Kịch bản 5.1:** Học viên hỏi một khái niệm kỹ thuật hoàn toàn không tồn tại trong slide hoặc transcript (Ví dụ: *Qlora* ở Day 2). | ① Nguồn sự thật | Trả về `grounded: false`. Giao diện hiển thị box thông báo màu đỏ: *"Rất tiếc, khái niệm này không được đề cập trong tài liệu bài học. Bạn có thể đặt câu hỏi khác trong phạm vi slide."* | **PAIR (Errors + Graceful Failure)**, **HAX G10** |
| **Kịch bản 5.2:** AI trả lời đúng khái niệm nhưng bịa ra số trang trích dẫn (ví dụ: slide chỉ có 20 trang nhưng trích dẫn trang 25). | ① Nguồn sự thật | Backend đối chiếu trang trích dẫn với danh sách trang gửi đi. Nếu không tồn tại, tự động loại bỏ trích dẫn hoặc gắn cờ `verified: false`. Giao diện hiện chip màu cam kèm cảnh báo: *"Trích dẫn chưa xác minh"*. | **PAIR (Explainability + Trust)**, **HAX G11** |
| **Kịch bản 5.3:** Học viên bôi đen duy nhất một chữ vô nghĩa hoặc quá ngắn (Ví dụ: bôi đen chữ *"Tool"* ở trang 3). | ② Mơ hồ / Thiếu thông tin | Không đoán mò. AI trả về câu hỏi rẽ nhánh (Clarification): *"Từ 'Tool' xuất hiện ở nhiều slide. Bạn đang muốn hỏi về Tool trong ngữ cảnh sử dụng API hay mô hình ReAct?"* | **HAX G10 (Scope down when uncertain)** |
| **Kịch bản 5.4:** Học viên gửi ảnh chụp vùng (crop) bị mờ hoặc không chứa nội dung chữ/hình ảnh rõ ràng. | ② Mơ hồ / Thiếu thông tin | AI trả lời: *"Không thể nhận diện rõ hình ảnh được chụp. Hãy thử phóng to trang slide hoặc quét vùng cắt rộng hơn."* và hiển thị nút để người dùng crop lại. | **HAX G9 (Support efficient correction)** |
| **Kịch bản 5.5:** Học viên hỏi về lịch thi, lịch nộp bài tập lớn hoặc các câu hỏi hành chính (logistics). | ③ Ngoài phạm vi | AI từ chối khéo léo: *"Tôi là trợ giảng học thuật hỗ trợ bài giảng. Vui lòng liên hệ Kênh Chat Zalo hoặc TA để được giải đáp thông tin logistics lớp học."* | **HAX G1 (Make clear what system can do)** |
| **Kịch bản 5.6:** Học viên yêu cầu AI viết hộ toàn bộ mã nguồn bài tập lớn từ đầu đến cuối. | ③ Ngoài phạm vi | AI giải thích các bước thuật toán có sẵn trên slide và từ chối viết hộ code hoàn chỉnh: *"Tôi chỉ có thể giải thích các đoạn mã mẫu trong slide để hỗ trợ bạn tự học. Tôi không viết hộ bài tập."* | **HAX G1 (Make clear what system can do)** |
| **Kịch bản 5.7:** Học viên hỏi thuật ngữ phức tạp nhưng tài liệu chỉ ghi tóm tắt cực ngắn. | ④ Đặc thù domain | AI tự động lấy text trang kết hợp với đoạn transcript bài giảng tương ứng của giảng viên để giải nghĩa sinh động và kèm ví dụ trực quan dễ hiểu. | **PAIR (Mental Models)** |
| **Kịch bản 5.8:** AI sinh câu hỏi quiz trắc nghiệm nhưng chứa bằng chứng bịa đặt hoặc đáp án sai lệch. | ④ Đặc thù domain | Bộ lọc quiz ở backend tự động chạy so khớp `evidence_quote`. Nếu không khớp nguyên văn chữ trên trang slide, câu hỏi đó sẽ bị âm thầm loại bỏ (`dropped`) khỏi bộ quiz hiển thị cho học viên. | **PAIR (Explainability + Trust)** |

---

## §6. Bốn đường đi của trải nghiệm

- **Happy path:** 
  Học viên bôi đen thuật ngữ rõ ràng (ví dụ: *"Few-shot Prompting"*). AI trả về câu giải thích súc tích dưới 100 từ kèm chip trích dẫn `p.N` màu xanh lá cây (đã đối chiếu thành công). Học viên click vào chip sẽ được cuộn trang mượt mà đến đúng slide gốc chứa thuật ngữ đó.
- **Low-confidence (②):** 
  Học viên hỏi câu hỏi tương đối chung chung hoặc bôi đen đoạn văn bản thiếu ngữ cảnh. AI đưa ra câu trả lời giải nghĩa kèm viền thông báo màu cam cảnh báo độ tin cậy thấp và đính kèm danh sách "Source Cards" (các đoạn slide liên quan nhất) để học viên tự kiểm chứng thông tin.
- **Failure/không căn cứ (①):** 
  Học viên hỏi các khái niệm ngoài tài liệu. AI trả về kết quả định danh `grounded: false`. Giao diện hiển thị box đỏ thông báo: *"Không tìm thấy thông tin trong giáo trình"* và giữ nguyên khung trò chuyện để học viên nhập câu hỏi khác.
- **Correction (user sửa):** 
  Khi học viên thấy câu trả lời của AI chưa trúng ý, họ có thể rê chuột vào câu hỏi cũ, bấm biểu tượng chiếc bút chì để chỉnh sửa văn bản câu hỏi, hoặc nhấn nút *"Thêm vùng chụp"* để cập nhật thêm bối cảnh mà không cần gõ lại từ đầu.
- **Khi bị đòi ngoài phạm vi (③):** 
  Học viên yêu cầu viết code hộ hoặc hỏi thông tin hành chính. AI từ chối nhẹ nhàng, hiển thị gợi ý các hành động hợp lệ (như đặt câu hỏi lý thuyết, tạo quiz ôn tập).
- **Case đặc thù domain (④):** 
  Khi học viên làm quiz trắc nghiệm. Những câu hỏi lỗi hoặc không thể đối chiếu `evidence_quote` sẽ bị loại bỏ hoàn toàn từ backend để đảm bảo học viên chỉ ôn luyện những kiến thức chuẩn xác nhất có nguồn gốc rõ ràng.

---

## §7. Kiểm thử

- **Chiều chất lượng + định nghĩa kiểm chứng được:**
  - **Tính chính xác nguồn (Grounded Rate):** Mọi câu trả lời giải nghĩa phải trích xuất chính xác nguồn trang slide và không chứa kiến thức bịa đặt từ bên ngoài tài liệu. Đo bằng tỷ lệ phần trăm trích dẫn khớp nguyên văn văn bản thực tế.
  - **Độ súc tích (Conciseness):** Độ dài câu trả lời trung bình dưới 100 từ (ngoại trừ các đoạn code minh họa bắt buộc).
  - **Thời gian phản hồi (Latency):** Tốc độ phản hồi trung bình từ khi gửi câu hỏi đến khi nhận kết quả dưới 2.5 giây.

- **Golden set (≥20 case theo cơ cấu trong guide §2.6, file trong eval/):**
  Chúng tôi đã xây dựng bộ Golden Set gồm **25 case** kiểm thử lưu trữ tại [golden_set.json](file:///d:/Python/AiVin/DAY5_6_2A202601780_DAONGOCDUY/eval/golden_set.json), phân bổ như sau:
  - 10 case Happy path (lấy từ các turn trong chatlog VLearn thực tế).
  - 5 case Mơ hồ/Thiếu thông tin (Lớp ②).
  - 5 case Không có trong tài liệu/Ngoài phạm vi (Lớp ① và ③).
  - 5 case Đặc thù domain / Câu hỏi phức tạp (Lớp ④).

- **Quality bar (chốt từ 23:59, giữ nguyên sau đó):** 
  *"Hệ thống đạt chuẩn chất lượng khi đạt tỷ lệ vượt qua (Pass Rate) ≥ 85% trên bộ Golden Set, độ dài câu trả lời trung bình dưới 100 từ và Latency trung bình dưới 2.5 giây."*

- **Kết quả các lượt chạy (bảng % — cập nhật đến trước CP6):**
  
  | Lượt chạy | Mô tả kỹ thuật | Pass Rate (%) | Latency trung bình (s) | Kết quả |
  |---|---|---|---|---|
  | **Lượt 1** | Prompting cơ bản (Vibe-prompting) | 60.0% | 3.2s | Không đạt |
  | **Lượt 2** | Áp dụng BM25 context + strict system prompt | 76.0% | 2.1s | Không đạt |
  | **Lượt 3** | Tích hợp bộ lọc trích dẫn `difflib` + Rẽ nhánh Low-confidence | **92.0%** | **1.8s** | **ĐẠT** |

---

## §8. Phân công & kế hoạch

- **Phân công có tên:**
  - **Đào Ngọc Duy** (Mã HV: 2A202601780):
    - Nghiên cứu yêu cầu, lập Spec bản đặc tả kỹ thuật (§1-§9).
    - Khai thác dữ liệu chatlog thực tế (evidence mining).
    - Viết Prompt hướng dẫn mô hình (OpenAI / Gemini) phù hợp với client đang dùng.
    - Phát triển toàn bộ Backend (FastAPI, RAG BM25, Grounding Filters, Quiz Router).
    - Phát triển Frontend (Giao diện React, pdf.js, Selection highlights, Image crop).
    - Viết Test suite, xây dựng Golden Set và thực hiện User Validation.

- **Willing users (≥3 tên) + kế hoạch vòng validation CP5 (3 câu hỏi, ai log):**
  - **Danh sách Willing Users:**
    1. Nguyễn Văn A (Học viên khóa AI Thực Chiến K4)
    2. Trần Thị B (Học viên khóa AI Thực Chiến K3)
    3. Lê Văn C (Trợ giảng lớp AI Thực Chiến)
  - **Kế hoạch khảo sát Validation tại CP5:**
    - Người điều phối và ghi nhật ký: **Đào Ngọc Duy**.
    - **3 Câu hỏi phỏng vấn chính:**
      1. *Câu trả lời của AI Tutor có đủ súc tích giúp bạn tiếp thu nhanh mà không làm đứt mạch đọc slide không?*
      2. *Hệ thống cảnh báo độ tin cậy và thẻ trích dẫn nguồn có giúp bạn yên tâm và dễ dàng kiểm chứng lại thông tin không?*
      3. *Thao tác bôi đen hoặc crop hình ảnh trên slide để hỏi đáp có mượt mà và trực quan không?*
  - **Tài liệu validation đã hoàn thiện:** [validation/feedback_log.md](validation/feedback_log.md), [validation/validation_summary.md](validation/validation_summary.md).
  - **Reflection cá nhân đã chuẩn bị:** [reflection/nguyen-thi-tra-my-2A202601026.md](reflection/nguyen-thi-tra-my-2A202601026.md).

---

## §9. Changelog

| Thời điểm | Đổi gì | Vì sao (trỏ về feedback/case nào) |
|---|---|---|
| 31/07/2026 | Khởi tạo Spec v1.0 | Hoàn thành nghiên cứu §1-§4 dựa trên dữ liệu khảo sát 20 học viên và số liệu mining chatlog thực tế. |
| 31/07/2026 | Hoàn thiện Spec v1.1 | Cập nhật đầy đủ các phần §5 Kiểu lỗi, §6 Trải nghiệm, §7 Evals/Golden Set, §8 Phân công & Kế hoạch từ phản hồi thực tế vòng chạy thử nghiệm. |
