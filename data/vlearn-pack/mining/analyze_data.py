import pandas as pd
import json

csv_path = r"D:\Python\AiVin\DAY5_6_2A202601780_DAONGOCDUY\data\vlearn-pack\chatlog\chat_history_anonymized_for_hackathon.csv"
df = pd.read_csv(csv_path)

print("Columns in CSV:", df.columns.tolist())
print("Total rows:", len(df))
print("Unique users:", df['user_id'].nunique())
print("Unique conversations:", df['conversation_id'].nunique())

# Filter tutor messages
tutor_df = df[df['role'] == 'tutor']
student_df = df[df['role'] == 'student']

print("\nTutor message analysis:")
print("Total tutor messages:", len(tutor_df))

# Citation analysis
# Check how citations are formatted. Let's see some sample non-empty citations
sample_citations = tutor_df['citations'].dropna().unique()[:5]
print("Sample citations:", sample_citations)

empty_citations = tutor_df[tutor_df['citations'].isna() | (tutor_df['citations'] == '[]') | (tutor_df['citations'] == '')]
print(f"Empty citations: {len(empty_citations)} ({len(empty_citations)/len(tutor_df)*100:.2f}%)")

# Rating analysis
print("\nRatings:")
print(tutor_df['rating'].value_counts(dropna=False))

# Look at down-rated messages
down_rated_tutor = tutor_df[tutor_df['rating'] == 'down']
print(f"Total down-rated tutor messages: {len(down_rated_tutor)}")

# Find matching student questions for these down-rated messages
# Usually, in a turn, the student asks and then the tutor answers. Let's join on turn_id or find consecutive messages.
# Let's inspect turn structure.
print("\nDown-rated messages details:")
for idx, row in down_rated_tutor.head(15).iterrows():
    turn_id = row['turn_id']
    student_msg = df[(df['turn_id'] == turn_id) & (df['role'] == 'student')]
    student_content = student_msg['content'].values[0] if len(student_msg) > 0 else "N/A"
    print(f"Turn: {turn_id}")
    print(f"Student: {student_content}")
    print(f"Tutor: {row['content']}")
    print(f"Citations: {row['citations']}")
    print("-" * 50)
