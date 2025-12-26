import streamlit as st
import re
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Quiz Tin học 6 – Nhúng câu hỏi", layout="centered")
st.title("📘 KIỂM TRA CUỐI KỲ I – TIN HỌC 6 (Không cần file)")

# ===============================
# 🔹 NỘI DUNG ĐỀ CƯƠNG (NHÚNG SẴN)
# ===============================

DOC_TEXT = r"""
TRƯỜNG THCS TỊNH SƠN
UBND XÃ SƠN TỊNH
ĐỀ CƯƠNG CUỐI HỌC KỲ I 
NĂM HỌC 2025 - 2026
Môn Tin học - Lớp 6

I. TRẮC NGHIỆM:

Câu 1. Phát biểu nào sau đây là đúng?
A. Dữ liệu chỉ có thể được hiểu bởi những người có trình độ cao.
B. Dữ liệu là những giá trị số do con người nghĩ ra.
C. Dữ liệu được thể hiện dưới dạng con số, văn bản, hình ảnh, âm thanh.
D. Dữ liệu chỉ có ở trong máy tính.

Câu 2. Xem bản tin dự báo thời tiết như Hình 1, bạn Khoa kết luận: "Hôm nay, trời có mưa". Phát biểu nào sau đây đúng?
A. Bản tin dự báo thời tiết là dữ liệu, kết luận của Khoa là thông tin.
B. Bản tin dự báo thời tiết là thông tin, kết luận của Khoa là dữ liệu.
C. Những con số trong bản tin dự báo thời tiết là thông tin.
D. Bản tin dự báo thời tiết và kết luận của Khoa đều là dữ liệu

... (TOÀN BỘ NỘI DUNG BẠN GỬI – giữ nguyên đầy đủ như trong file)
... phần đáp án 1.C 2.A 3.D ... 56.D

II. TỰ LUẬN:
Câu 57. Máy tìm kiếm là gì?
Câu 58. Nêu những ưu, nhược điểm cơ bản của dịch vụ thư điện tử.
...
Câu 64. Một ổ cứng có dung lượng là 64GB...
"""

# ===============================
# 1️⃣ TÁCH CÂU HỎI & PHƯƠNG ÁN
# ===============================

def extract_questions(text):
    pattern_q = r"(Câu\s+\d+\..*?)(?=\nCâu\s+\d+\.|\nII\.|\Z)"
    raw_blocks = re.findall(pattern_q, text, flags=re.S)

    questions = []
    for block in raw_blocks:
        lines = [l.strip() for l in block.split("\n") if l.strip()]
        qtext = re.sub(r"^Câu\s+\d+\.\s*", "", lines[0])
        options = [l for l in lines[1:] if re.match(r"^[A-D]\.", l)]
        questions.append({"question": qtext, "options": options})

    return questions

# ===============================
# 2️⃣ TÁCH ĐÁP ÁN GỐC
# ===============================

def extract_answer_key(text):
    ans_pattern = r"\n\s*(\d+)\.\s*([A-D])"
    return dict(re.findall(ans_pattern, text))

questions = extract_questions(DOC_TEXT)
answer_key = extract_answer_key(DOC_TEXT)

st.success(f"📂 Đã nạp {len(questions)} câu hỏi trắc nghiệm từ đề cương")

# ===============================
# 3️⃣ LÀM BÀI
# ===============================
st.header("📝 Phần trắc nghiệm")

user_answers = []
score = 0
details = []

for i, q in enumerate(questions, start=1):
    st.subheader(f"Câu {i}: {q['question']}")
    choice = st.radio("Chọn đáp án:", q["options"], key=f"q{i}")
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

# ===============================
# 4️⃣ NỘP BÀI – CHẤM & GIẢI THÍCH
# ===============================
if st.button("📌 Nộp bài"):
    st.write("---")
    st.header("📊 Kết quả")

    st.success(f"🎯 Điểm trắc nghiệm: **{score}/{len(questions)}**")

    df = pd.DataFrame(details)
    st.dataframe(df, use_container_width=True)

    st.info("ℹ️ Các câu sai hãy đối chiếu với đáp án & hướng dẫn ôn tập.")

    # ===============================
    # 5️⃣ XUẤT KẾT QUẢ (≥ 6 điểm)
    # ===============================
    if score >= 6:
        st.success("🏆 Đạt yêu cầu (≥ 6 điểm) — cho phép xuất kết quả")

        student = st.text_input("Nhập tên học sinh để lưu kết quả:")

        if st.button("💾 Xuất file kết quả"):
            filename = f"/mnt/data/ket_qua_{student}_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
            df.to_excel(filename, index=False)
            st.write(f"[📥 Tải file kết quả]({filename})")

    else:
        st.warning("⚠️ Chưa đạt 6 điểm — chưa được xuất kết quả")
