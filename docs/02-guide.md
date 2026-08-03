# Guide xuyên suốt — 5 giai đoạn, bám 6 mốc

> **Cách dùng:** Một file duy nhất, đọc theo thứ tự giai đoạn. Mỗi giai đoạn mở đầu bằng **các câu hỏi nhóm phải tự suy luận và trả lời** — đó là phần quan trọng nhất; scaffold (khung output) chỉ là phần nhẹ để chốt lại. Worksheet và bảng mẫu chỉ dùng để chốt lại kết quả — phần quan trọng là nhóm tự trả lời được các câu hỏi.

| Giai đoạn | Mốc tương ứng | Mục |
|---|---|---|
| 1 · Khám phá | Phát đề → CP1 Canvas | §1 |
| 2 · Thiết kế & Spec | CP1 → CP4 + spec.md 23:59 N1 | §2 |
| 3 · Build | CP2 → CP3 | §3 |
| 4 · Đo & Validate | CP3 → CP5 | §4 |
| 5 · Demo & Nộp | CP5 → CP6 | §5 |

---

# §1 · KHÁM PHÁ *(phát đề → CP1, ~1 giờ)*

## 1.1 Năm câu hỏi phải tự trả lời — theo đúng thứ tự

1. **Ai** là người trực tiếp làm việc này? Một vai cụ thể (học viên đang-trong-buổi-học · học viên ôn trước quiz · học viên nghỉ buổi · học viên hỏi bài trên Discord · giảng viên soạn quiz · TA trả lời câu hỏi lặp) — không phải "học viên nói chung".
2. Họ đang cố **hoàn thành việc gì**? Viết thành một câu `verb + object + bối cảnh`, không có tên sản phẩm/AI trong câu. Tự kiểm: bỏ AI đi, việc đó còn tồn tại không? Không còn = bạn đang tìm chỗ nhét AI, chọn lại.
3. Hôm nay họ đang giải quyết bằng gì (tua video · hỏi bạn · hỏi tutor · ChatGPT riêng · bỏ qua)? **Nó fail ở đâu, và vì sao họ chưa bỏ nó?**
4. **Bằng chứng nào** cho thấy họ đau thật — số đếm được từ data, hay lời nguyên văn của họ? Cảm nhận cá nhân chưa phải là bằng chứng.
5. Nhóm thấy **≥3 hướng khả dĩ** — vì sao chọn hướng này? Trả lời bằng số: bao nhiêu người gặp × tần suất × mỗi lần tốn gì (phút / điểm số / niềm tin), và có build nổi trong sự kiện không.

## 1.2 Cách làm nhanh JTBD *(15-20')*

- Chọn job executor (câu 1) → viết job statement (câu 2) → liệt kê alternatives và chỗ fail (câu 3).
- Nghĩ thêm 2-3 **job story**: `When [tình huống], I want to [động lực], so I can [kết quả]` — lấy tình huống từ chatlog thật càng tốt.
- Tra Strategyn Playbook (tham-khao/) đúng 2 thứ: cách viết job statement (chương 2) và job map 8 bước (chương 3). Không đọc hết 48 trang. Muốn đào sâu: `tham-khao/worksheet-jtbd-day-du.md`.

## 1.3 Cách mining data & thu bằng chứng

1. **Đọc 30-50 mẫu trước, đếm sau** — đọc chatlog VLearn / tin nhắn thật trong Discord khoá để biết *loại* pattern tồn tại (tin cụt "hii/hả"? tutor trả template dài? câu hỏi logistics? cite sai trang? câu hỏi lặp?), rồi mới định nghĩa tiêu chí đếm.
2. **Đếm được mới là bằng chứng**: "41/200 hội thoại mở đầu bằng tin không-phải-câu-hỏi" ✓ · "nhiều bạn nhắn linh tinh" ✗.
3. **Ghi phương pháp đếm** (đếm gì, trên bao nhiêu mẫu, quy tắc xếp loại) — người khác kiểm lại được mới tính. Giữ ≥5 ví dụ nguyên văn.
4. Khảo sát/phỏng vấn: hỏi về **lần gần nhất** ("lần gần nhất bạn muốn xem lại một đoạn bài giảng, bạn làm gì? mất bao lâu?") — tránh hỏi ý kiến kiểu "bạn có cần tính năng X không?" — hầu như ai cũng trả lời có, dữ liệu thu được không dùng được. **Ghi log toàn bộ: câu đã hỏi, từng câu trả lời nguyên văn, và ai trả lời.** Không có log thì không được tính là bằng chứng.

**Chuẩn bằng chứng** (tiêu chí nghiệm thu 2 — hoàn thiện đến 23:59, CP1 chỉ cần mầm):
- **Đường A — khảo sát:** ≥20 người ngoài nhóm · ≥50% xác nhận · log đầy đủ.
- **Đường B — mining:** số đếm được + ≥5 ví dụ nguyên văn + phương pháp đếm.
- Khuyến khích cả hai: B chứng minh pain *tồn tại*, A chứng minh user *muốn nó được giải*.

## 1.4 Chọn bài toán bằng bảng impact *(scaffold nhẹ)*

Với ≥3 ứng viên, mỗi cái một dòng: `ứng viên | bao nhiêu người gặp (từ evidence) | tần suất | mỗi lần tốn gì | build nổi không | chọn?`. Hai ứng viên sát nhau → chọn ứng viên có **bằng chứng mạnh hơn**. Ứng viên bị loại giữ lại trong spec §2 — người chấm cần thấy nhóm đã cân nhắc gì.

## 1.5 Gặp TA ở CP1 cần show *(scaffold Canvas — 7 dòng)*

Hướng (A/B/C) · job executor · pain một câu (ai-đang làm gì-vướng đâu-hậu quả) · 1-2 bằng chứng đầu tiên · **lát cắt MỘT CÂU** (1 user · 1 việc · 1 quyết định AI · 1 kết quả) · automation dự kiến + 1 dòng lý do · ≥3 willing users dự kiến · phân công có tên.
*Kẹt >30' chưa chọn được hướng? Tự hỏi: "nhóm mình là user thật của cái nào nhiều nhất?" — chọn cái đó.*

---

# §2 · THIẾT KẾ & SPEC *(CP1 → CP4 · spec.md chốt 23:59 N1)*

## 2.1 Các câu hỏi phải tự trả lời

1. Người khác đã giải bài này thế nào — mình học gì, né gì, khác gì?
2. AI nên **tự làm đến đâu** — và nếu nó sai thì ai chịu gì, sửa đắt hay rẻ?
3. Sản phẩm sẽ **hành xử thế nào khi sai / khi không chắc** — cụ thể nói gì, hiện gì, cho user làm gì tiếp?
4. **"Tốt" nghĩa là gì, đo bằng gì** — và bar của nhóm là bao nhiêu %?

## 2.2 Nghiên cứu giải pháp tương tự *(express — chia người, 15'/người)*

Mỗi thành viên dùng thử 1 sản phẩm gần giống (ChatGPT study mode · Khanmigo · NotebookLM · Duolingo · Quizlet AI...) và trả lời đúng 4 câu: ① họ giải job này bằng flow nào? ② một điều đáng học (quan sát cụ thể — "NotebookLM luôn cite nguồn cạnh câu trả lời", không phải "giao diện đẹp")? ③ một điều đáng né? ④ mình sẽ khác gì ở lát cắt này? → gom vào spec §3.

## 2.3 Chọn mức automation theo cost-of-error

| Mức | Khi nào đúng | Ví dụ trong khoá |
|---|---|---|
| **Augment** — AI gợi ý, người quyết | Sai thì đắt (kiến thức sai đến học viên, điểm số) | Quiz AI sinh, giảng viên duyệt từng câu |
| **Conditional** — AI tự làm case chắc, chuyển người case mơ hồ | Đa số case lành, số ít hiểm | Trợ lý trả lời khi có căn cứ trong tài liệu; không có → chuyển TA |
| **Automate** — AI tự làm | Sai thì rẻ, user tự thấy và sửa được | Sinh chapter/timestamp cho video |

Lý do trong spec viết theo cost-of-error: *sai thì ai chịu gì, sửa đắt hay rẻ* — không viết "vì tiện".

## 2.4 Nguyên tắc HAX/PAIR — chọn ≥4, khai trong spec §4b, mỗi cái trỏ vào chỗ cụ thể

*(Tra bản gốc khi cần: microsoft.com/haxtoolkit/ai-guidelines · pair.withgoogle.com/guidebook. Mỗi nguyên tắc khai báo phải chỉ ra được vị trí áp dụng cụ thể trong prototype — TA kiểm tra tại CP4.)*

**Nhóm khởi đầu (chọn ≥1):**
- **G1 — Làm rõ hệ thống làm được gì.** Câu đầu tiên user thấy có nói đúng phạm vi không? (Tutor chào bằng cả đoạn văn — có ai đọc?)
- **G2 — Làm rõ nó làm tốt đến đâu.** User biết khi nào nên tin, khi nào nên kiểm lại? ("Trả lời dựa trên tài liệu buổi 2; ngoài tài liệu mình sẽ nói rõ.")

**Khi không chắc / khi sai (G10 bắt buộc + ≥1 trong G8/G9/G11):**
- **G10 — Thu hẹp phạm vi khi nghi ngờ.** Không chắc → hỏi lại một câu, hoặc trả lời kèm giới hạn — không làm liều.
- **G8 — Gạt bỏ dễ dàng.** User bỏ qua câu trả lời/gợi ý có dễ không, hay bị chặn flow?
- **G9 — Sửa dễ dàng.** User sửa/hỏi lại được ngay trên output không?
- **G11 — Giải thích vì sao.** "Vì đoạn bạn chọn ở trang 6 nói về X" — giải thích gắn với hành động tiếp theo.

**Nhóm nâng cao (tự chọn nếu hợp):** **G5** hợp chuẩn mực xã hội (giọng có hợp học viên VN gõ "cái chi dợ"?) · **G12** nhớ tương tác gần · **G13/G14** học từ hành vi, thay đổi thận trọng · **G15** mời feedback chi tiết (👍👎 kèm "sai chỗ nào?") · **G17** quyền kiểm soát tổng.

**PAIR — tra theo chương:** *Mental Models* (đặt kỳ vọng thấp hơn khả năng một chút, đừng ngược lại) · *Explainability + Trust* (tin đúng mức > tin tối đa — hiển thị căn cứ để user tự kiểm) · *Feedback + Control* (thu feedback ngay trong flow; user luôn bỏ qua AI được) · *Errors + Graceful Failure* (lỗi-do-giới-hạn ≠ lỗi-do-hiểu-nhầm-ngữ-cảnh — mỗi loại một đường lui).

## 2.5 Bốn lớp chỗ khó + kịch bản rủi ro *(≥8 kịch bản — TA soát tại CP4)*

Tự cụ thể hoá 4 lớp cho lát cắt của mình bằng 4 câu hỏi:
- ① **Nguồn sự thật** — chỗ nào AI bịa được? Không có căn cứ thì làm gì?
- ② **Mơ hồ / thiếu thông tin** — input không đủ chắc: hỏi lại, đoán có báo, hay từ chối?
- ③ **Ngoài phạm vi / thẩm quyền** — user sẽ đòi gì mà feature không được phép làm?
- ④ **Đặc thù domain** — sai cái gì thì học viên học sai kiến thức / mất điểm / mất niềm tin ngay?

Chạy **HAX Playbook** (github.com/microsoft/HAXPlaybook — trả lời bộ câu hỏi config → nhận kịch bản lỗi) → chốt ≥8 kịch bản, mỗi kịch bản một dòng: `tình huống cụ thể | lớp | hành vi mong muốn (nói gì, hiện gì, cho user làm gì tiếp) | nguyên tắc áp (G../PAIR)`. Tự kiểm: **kịch bản nào làm nhóm sợ nhất khi demo?** Chưa có cái nào đáng sợ = chưa đủ hiểm. Mỗi lớp phải có ≥2 case tương ứng trong golden set (§2.6).

## 2.6 Định nghĩa "tốt" + golden set + quality bar *(phải xong lượt đo đầu tại CP3)*

1. **Bắt đầu từ output thật, không từ tiêu chí trừu tượng.** Chạy tay 10-20 input qua prototype (hoặc ChatGPT/Claude với prompt nháp), đọc từng output, ghi thô: dùng được / sửa được / không chấp nhận được. Tiêu chí tốt được *chưng cất từ lỗi đã thấy*. *(Hamel Husain — "Your AI Product Needs Evals": "look at your data" là bước một; Anthropic docs — "Create strong empirical evaluations".)*
2. **Đặt tên cho lỗi.** Gom output tệ thành nhóm lỗi có tên (bịa nguồn / lạc trình độ / cite sai trang / đoán khi thiếu thông tin / vượt thẩm quyền...), đối chiếu 4 lớp để không sót. Mỗi lỗi: trigger → biểu hiện → hậu quả. *(HAX Playbook; Aman Khan — "Beyond vibe checks", Lenny's Newsletter.)*
3. **Biến mỗi chiều chất lượng thành định nghĩa kiểm chứng được.** "Trả lời tốt" không đo được. Tách chiều (đúng-có-căn-cứ / đúng cỡ-đúng giọng / an toàn), mỗi chiều: pass/fail ("mọi thông tin trace được về transcript") hoặc thang có mô tả mức (1 = sai kiến thức; 3 = đúng nhưng dài gấp đôi cần; 5 = đúng, đúng cỡ, có trích dẫn). *(HAX G2.)*
4. **Test độ rõ bằng người thứ hai.** Hai thành viên chấm độc lập cùng 5 output → so. Lệch = định nghĩa mơ hồ → viết lại. Trong nhóm còn chấm khác nhau thì không dùng chấm được ai.
5. **Golden set ≥20 case nhóm tự xây**: ≥2 case cho mỗi lớp chỗ khó + 8-10 case thường + 2-4 case hiếm; trong đó **≥10 case lấy hoặc phát triển từ chatlog thật** (nhóm dùng promptfoo nên mở rộng lên 30+). Lưu file trong `eval/` và **chốt quality bar trước khi đo**: "Đạt khi ≥ __% qua bộ, và [điều kiện cứng]" — chốt tại spec.md 23:59 và giữ nguyên sau đó. Không đạt quality bar nhưng phân tích được nguyên nhân vẫn được tính đủ điểm; số liệu bị chỉnh sửa sẽ không được tính. *(Bài giảng Ship/Limited/Hold.)*

## 2.7 Trước CP4 tự soát

Spec đủ §1-§9 theo `03-template-ai-spec.md` · evidence đạt chuẩn A/B có log · bảng impact ≥3 ứng viên + ứng viên loại · ≥4 nguyên tắc có "áp vào đâu" · 4 lớp + ≥8 kịch bản · quality bar bằng % · kế hoạch sáng N2 (ai validate, ai dry run). **Commit spec.md trước 23:59 — quality bar chốt từ thời điểm này.**

---

# §3 · BUILD *(CP2 → CP3)*

## 3.1 Câu hỏi định hướng + nguyên tắc xương sống

*"Demo 5 phút thì bấm vào đâu, gõ gì, ra gì?"* — build đúng đường đó trước, mọi thứ khác sau. **CP2:** flow chính bấm đi hết được (Sketch/Mock, data giả, chưa cần AI — đừng dựng UI đẹp trước khi flow thông). **CP3:** ≥1 lời gọi AI thật vào quyết định trung tâm, log/trace giữ trong repo; mock phần còn lại, ghi rõ trong spec §4. Sau CP4 không thêm feature mới.

## 3.2 Ba mức prototype — chọn theo sức nhóm

| Mức | Là gì | Đủ để |
|---|---|---|
| Sketch | Màn hình dựng nhanh + 1 AI call chạy demo được | Chứng minh concept + hành vi khi sai |
| Mock | Flow bấm được, data giả, AI thật ở lõi | Demo trọn 4 đường đi trải nghiệm |
| Working | Chạy end-to-end với data pack thật | Đưa cho user thật dùng thử |

**Mức nào cũng bắt buộc có ≥1 lời gọi AI chạy thật.** Một bản Sketch làm kỹ được đánh giá cao hơn một bản Working làm vội — rubric chấm chuỗi quyết định, không chấm mức độ hoành tráng.

## 3.3 Multi-prototype *(khuyến khích — giữa CP2 và CP3 nếu kịp)*

Trước khi build sâu, dựng nhanh **≥2 phương án khác nhau ở MỘT quyết định thiết kế có tên** — mức automation (hỏi trước vs làm luôn) / kiểu tương tác (chủ động vs chờ gọi) / dạng output (nháp sửa được vs 3 lựa chọn vs kết quả chốt). **Khác trục, không phải khác màu nút.** Thử → chọn → giữ bằng chứng cả phương án bị loại + lý do chọn (spec §8).

## 3.4 Tool menu + luật an toàn

- **Builder:** v0.dev (UI đẹp nhanh) · Lovable/Bolt.new (nhóm không dev — đăng ký free tier TRƯỚC) · Figma Make (nhóm mạnh design) · Claude Code/Cursor (nhóm kỹ thuật).
- **AI call:** Google AI Studio (Gemini free tier ~1.500 req/ngày — free tier có thể dùng data để train → **chỉ đưa data giả/data pack**) · API key khoá học nếu ban tổ chức cấp.
- **Luật an toàn:** ① không commit API key/.env — key để biến môi trường; ② chỉ dùng data giả hoặc data pack — không data thật của người thật; ③ repo public: trước khi push soát không key, không thông tin cá nhân, không đổ nguyên data pack lên (trích ngắn minh hoạ được).
- **Kẹt kỹ thuật quá 20 phút: gọi TA** — CP2 chính là mốc hỗ trợ kỹ thuật. Ghi lại lỗi và cách xử lý vào notes để dùng cho reflection.

## 3.5 Phân công song song *(nhóm 4-5 người, tham khảo)*

1 người evidence tiếp tục đến chuẩn A/B · 1-2 người build flow · 1 người prompt + golden set · 1 người spec + chuẩn bị validation. Ai cũng phải giải thích được phần có tên mình — CP5 kiểm ngẫu nhiên.

---

# §4 · ĐO & VALIDATE *(CP3 → CP5)*

## 4.1 Đo bằng máy — chạy golden set

**Hai đường tuỳ sức:** *(tay — mọi nhóm)* bảng 4 cột `case | input | output | đạt? theo định nghĩa từng chiều`, hai người chấm độc lập case khó rồi so; *(code)* `npx promptfoo@latest init` — golden set thành test tự động, có red-team mode sinh thêm case hiểm.

**Nhịp lặp:** `chạy trọn bộ → bảng % → chọn MỘT failure đau nhất → sửa → chạy lại trọn bộ`. Sửa xong phải chạy **trọn bộ** (sửa chỗ này vỡ chỗ kia là chuyện thường của prompt). Mỗi lượt một bản ghi trong `eval/`, đủ mọi case kể cả fail.

**Lỗi thường gặp:** golden set chỉ toàn case dễ (TA sẽ kiểm tra độ phủ 4 lớp chỗ khó) · chấm "đạt" theo cảm tính giữa chừng (quay lại định nghĩa trong spec; nếu định nghĩa chưa ổn thì sửa định nghĩa và ghi changelog) · đổi quality bar khi thấy kết quả thấp (bar đã chốt — phân tích khoảng cách chính là nội dung của slide 4).

## 4.2 Đo bằng người — vòng validation *(CP5, trước dry run)*

**Ai:** ≥5 người ngoài nhóm — ưu tiên 3 willing users đã khai ở CP1 + thành viên zone khác (đổi chéo giữa các nhóm là nhanh nhất, và ai cũng là user thật của khoá).

**Một phiên 10 phút/người:** ① giao task thật ("hãy dùng cái này để [job]") → **im lặng quan sát** — không thuyết minh, không gợi ý, ghi lại họ bấm gì, kẹt đâu; ② hỏi đúng 3 câu: *"Điều gì khó hiểu hoặc khó chịu nhất?"* · *"Kết quả này bạn có tin không — vì sao?"* · *"Bạn có dùng thật không — vì sao / vì sao chưa?"*; ③ log nguyên văn.

**Scaffold log** (bảng trong `validation/`, mỗi người thử một dòng): `người thử (tên/vai — willing user?) | task | quan sát | quote nguyên văn | mức nghiêm trọng`. Kèm 4 dòng tổng hợp: chủ đề lặp nhiều nhất · 1-2 thay đổi làm trước demo (→ Changelog spec §9) · giữ nguyên có lý do · đưa vào backlog (slide 6).

Nếu mọi phản hồi đều là lời khen, phiên test chưa đạt — giao lại task khó hơn hoặc đổi người thử.

## 4.3 Gặp TA ở CP5 cần show

Feedback log ≥5 mẩu có tên người thử · changelog có thay đổi từ feedback (hoặc lý do giữ) · slide final + demo script · dry run xong có bấm giờ · **mọi thành viên sẵn sàng bị hỏi ngẫu nhiên "phần này hoạt động thế nào?"** (vibe-coding rule).

---

# §5 · DEMO & NỘP *(CP5 → CP6)*

## 5.1 Slide 6 trang — luật "không có bằng chứng thì không có slide"

*(Luật: mỗi slide phải có ≥1 con số / quote có nguồn / kết quả đo — người nghe kiểm chứng được.)*

1. **User & Job** *(45")* — job executor + core JTBD một câu + con số pain ("41/200 hội thoại...", "17/25 người khảo sát..."). Tránh: persona chung chung.
2. **Vì sao chọn tính năng này** *(45")* — bảng impact rút gọn 3 ứng viên + ứng viên loại một dòng lý do. Tránh: trình bày như chỉ có đúng một ý tưởng từ đầu.
3. **Giải pháp & demo live** *(2')* — lát cắt 1 câu + automation 1 dòng cost-of-error + **demo trực tiếp: 1 case chuẩn + 1 case chỗ khó** (case lỗi được xử lý là phần được đánh giá cao — không nên giấu). Tránh: 3 case đều happy path; video thay live khi live vẫn chạy được.
4. **Kết quả đo** *(45")* — % qua golden set đối chiếu **quality bar đã chốt từ 23:59 N1** + 1 failure đáng kể nhất; chưa đạt thì phân tích nguyên nhân. Tránh: chỉ trình bày số đẹp mà không nêu quality bar đã cam kết.
5. **User thật nói gì** *(45")* — ≥2 quote nguyên văn từ validation (tên/vai) + thay đổi đã làm. Tránh: chỉ toàn lời khen chung chung.
6. **Nếu có thêm 1 tuần** *(30")* — 2-3 việc ưu tiên trỏ về feedback/failure chưa xử + một dòng bài học lớn nhất. Tránh: roadmap 10 mục.

Demo round: 5' trình bày + 5' Q&A — **thẻ giám khảo** (chạy 1 case lạ tại chỗ) + **mỗi thành viên nói ≥1 phần**.

## 5.2 Checklist nộp cuối *(trước CP6)*

- [ ] Repo đủ: README (thành viên + phân công có tên) · spec.md · demo-slides.pdf · codebase/ · eval/ (golden set + các lượt chạy) · validation/ (feedback log) · reflection/ (mỗi người 1 file)
- [ ] Backup demo (screenshot/video ngắn) phòng live hỏng
- [ ] Cả nhóm trả lời được: "Augment hay automate — vì sao?" · "Failure nguy hiểm nhất?" · "Phần bạn làm là gì?"
