import streamlit as st
from docx import Document
import re
import pandas as pd
from datetime import datetime

DOCX_PATH = "/mnt/data/đề cương học kì 1; Tin học 6; năm học 2025-2026.docx"

st.set_page_config(page_title="Quiz Tin học 6 tự động", layout="centered")
st.title("📘 KIỂM TRA CUỐI KỲ I – TIN HỌC 6 (Tự động từ file .docx)")


# ==============================
# 1️⃣ HÀM ĐỌC & TÁCH CÂU HỎI
# ==============================
def load_questions_from_docx(path):
    doc = Document(path)
    text = "\n".join(p.text for p in doc.paragraphs)

    # Tạo danh sách câu hỏi trắc nghiệm
    pattern_q = r"(Câu\s+\d+\..*?)(?=\nCâu\s+\d+\.|\Z)"
    raw_questions = re.findall(pattern_q, text, flags=re.S)

    questions = []
    for block in raw_questions:
        lines = [l.strip() for l in block.split("\n") if l.strip()]
        qline = lines[0]

        # Tách câu hỏi
        qtext = re.sub(r"^Câu\s+\d+\.\s*", "", qline)

        # Tách các phương án A/B/C/D
        options = [l for l in lines[1:] if re.match(r"^[A-D]\.", l)]

        questions.append({
            "question": qtext,
            "options": options
        })

    # Tách đáp án chính thức ở cuối file
    ans_pattern = r"\n\s*(\d+)\.\s*([A-D])"
    answer_key = dict(re.findall(ans_pattern, text))

    return questions, answer_key


questions, answer_key = load_questions_from_docx(DOCX_PATH)

st.success(f"📂 Đã nạp {len(questions)} câu hỏi từ file DOCX")


# ==============================
# 2️⃣ HIỂN THỊ CÂU HỎI + LÀM BÀI
# ==============================
st.header("📝 LÀM BÀI TRẮC NGHIỆM")

user_answers = []
score = 0
details = []

for i, q in enumerate(questions, start=1):
    st.subheader(f"Câu {i}: {q['question']}")
    choice = st.radio("Chọn đáp án:", q["options"], key=f"q_{i}")

    user_answers.append(choice)

    correct = answer_key.get(str(i), "")
    is_correct = choice.startswith(correct)

    if is_correct:
        score += 1

    details.append({
        "Câu": i,
        "Chọn": choice[:1],
        "Đúng": correct,
        "Kết quả": "✓ Đúng" if is_correct else "✗ Sai"
    })


# ==============================
# 3️⃣ NỘP BÀI & GIẢI THÍCH
# ==============================
if st.button("📌 Nộp bài"):
    st.write("---")
    st.header("📊 KẾT QUẢ")

    st.success(f"🎯 Điểm của bạn: **{score}/{len(questions)}**")

    df = pd.DataFrame(details)
    st.dataframe(df, use_container_width=True)

    st.info("ℹ️ Các đáp án sai cần xem lại dựa trên tài liệu ôn tập.")

    # ==============================
    # 4️⃣ XUẤT KẾT QUẢ (≥ 6 điểm)
    # ==============================
    if score >= 6:
        st.success("🏆 Bạn đạt yêu cầu – hệ thống đã xuất kết quả")

        student_name = st.text_input("Nhập tên học sinh để lưu kết quả:")

        if st.button("💾 Lưu & Xuất kết quả"):
            result_file = f"/mnt/data/ket_qua_{student_name}_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
            df.to_excel(result_file, index=False)

            st.write(f"📥 **Tải kết quả tại đây:**")
            st.write(f"[Download file]({result_file})")
    else:
        st.warning("⚠️ Điểm chưa đạt 6 — chưa được xuất kết quả.")
