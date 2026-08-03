import pandas as pd
import re

csv_path = r"D:\Python\AiVin\DAY5_6_2A202601780_DAONGOCDUY\data\vlearn-pack\chatlog\chat_history_anonymized_for_hackathon.csv"
df = pd.read_csv(csv_path)

tutor_df = df[df['role'] == 'tutor']

# Keywords indicating retrieval failure or apologies
patterns = [
    r"không tìm thấy",
    r"không thể tìm thấy",
    r"chưa tìm thấy",
    r"rất tiếc",
    r"không thể truy cập",
    r"không truy cập được",
    r"xin lỗi",
    r"không hiển thị"
]

failure_count = 0
failures = []

for idx, row in tutor_df.iterrows():
    content = str(row['content']).lower()
    matched_pats = [pat for pat in patterns if re.search(pat, content)]
    if matched_pats:
        failure_count += 1
        turn_id = row['turn_id']
        student_msg = df[(df['turn_id'] == turn_id) & (df['role'] == 'student')]
        student_content = student_msg['content'].values[0] if len(student_msg) > 0 else "N/A"
        failures.append({
            'turn_id': turn_id,
            'student': student_content,
            'tutor': row['content'],
            'citations': row['citations'],
            'matched_keywords': matched_pats
        })

print(f"Total tutor messages with potential retrieval/access failure keywords: {failure_count} (out of {len(tutor_df)} - {failure_count/len(tutor_df)*100:.2f}%)")

# Let's count specific failures where student selected a page/slide and tutor said "không tìm thấy" or "rất tiếc"
page_in_student = 0
page_failure = 0
for f in failures:
    student_content = str(f['student']).lower()
    if 'trang' in student_content or 'slide' in student_content:
        page_in_student += 1
        # Check if the tutor actually failed
        tutor_content = str(f['tutor']).lower()
        if any(kw in tutor_content for kw in ["không tìm thấy", "chưa tìm thấy", "rất tiếc", "không thể truy cập", "không truy cập được"]):
            page_failure += 1

print(f"Number of turns where student asks about a specific 'Trang' or 'Slide': {sum(1 for idx, r in df[df['role']=='student'].iterrows() if 'trang' in str(r['content']).lower() or 'slide' in str(r['content']).lower())}")
print(f"Number of failures when student asked about a specific 'Trang' or 'Slide': {page_failure}")

# Let's inspect some other issues like "lan man" (long answers). Let's calculate tutor answer length distribution.
tutor_df['length'] = tutor_df['content'].apply(lambda x: len(str(x).split()))
print("\nTutor message length distribution (in words):")
print(tutor_df['length'].describe())

# How many answers are very long (e.g., > 200 words)?
long_answers = tutor_df[tutor_df['length'] > 200]
print(f"Number of tutor answers > 200 words: {len(long_answers)} ({len(long_answers)/len(tutor_df)*100:.2f}%)")

# Let's output some examples of long answers
print("\nSample long answers:")
for idx, row in long_answers.head(3).iterrows():
    turn_id = row['turn_id']
    student_msg = df[(df['turn_id'] == turn_id) & (df['role'] == 'student')]
    student_content = student_msg['content'].values[0] if len(student_msg) > 0 else "N/A"
    print(f"Turn: {turn_id} (Length: {row['length']} words)")
    print(f"Student: {student_content[:150]}...")
    print(f"Tutor: {row['content'][:300]}...")
    print("-" * 50)
