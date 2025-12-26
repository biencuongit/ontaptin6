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

Câu 3. Phát biểu nào sau đây đúng về lợi ích của thông tin?
A. Có độ tin cậy cao.đem lại hiểu biết cho con người.
B. Đem lại hiểu biết cho con người, không phụ thuộc vào dữ liệu.
C. Có độ tin cậy cao, không phụ thuộc vào dữ liệu.
D. Đem lại hiểu biết và giúp con người có những lựa chọn tốt.
Câu 4. Các hoạt động xử li thông tin gồm:
A. Đầu vào, đầu ra.
B. Thu nhận, xử lí, lưu trữ, truyền.
C. Nhìn, nghe, suy đoán, kết luận.
D. Mở bài, thân bài, kết luận.
Câu 5. Thao tác ghi nhớ và cất giữ tài liệu của con người được xếp vào hoạt động nào trong quá trình xử li thông tin?
A. Thu nhận.
B. Lưu trữ                           
C. xử lí.                         
D. Truyền.
Câu 6. Các thao tác nói, chia sẻ, thông báo, tuyên truyền, biểu đạt, trò chuyện,... của con người được xếp vào hoạt động nào trong quá trình xử li thông tin?
A. Thu nhận.		B. Lưu trữ.                     C. xử lí.                       D. Truyền.
Câu 7. Bàn phím, chuột, máy quét và webcam là những ví dụ về loại thiết bị nào của máy tính?
A. Thiết bị ra.		B Thiết bị lưu trữ.		C. Thiết bị vào.		D. Bộ nhớ.
Câu 8. Thiết bị nào sau đây không phải là thiết bị ra của máy tính?
A. Micro.		B. Máy in.                 C. Màn hình.             D. Loa.
Câu 9. Đặc điểm nào sau đây không thuộc về máy tính?
A. Thực hiện nhanh và chính xác.		B. Suy nghĩ sáng tạo
C. Lưu trữ lớn					D. Hoạt động bền bỉ
Câu 10. Đơn vị đo dữ liệu nào sau đây là lớn nhất?
A. Gigabyte.  		 B. Megabyte,		C. Kilobyte.     D. Bít.
Câu 11. Hình 5 là thuộc tính của tệp IMG_0041.jpg lưu trữ trong máy tính.
 
Tệp ảnh hà nội có dung lượng bao nhiêu?
A. 103 byte.         B. 103 kilobit			C. 103 kilobyte.    D. 0,846 megabyte.
Câu 12. Dữ liệu được máy tính lưu trữ dưới dạng
A. thông tin.          B. dãy bít.		C. số thập phân.                          D. các kí tự.
Câu 13. Dữ liệu trong máy tính được mã hoá thành dãy bít vì
A. dãy bít đáng tin cậy hơn.
B. dãy bít được xử li dễ dàng hơn.
C. dãy bít chiếm ít dung lượng nhớ hơn.
D. máy tính chỉ làm việc với hai kí hiệu 0 và 1.
Câu 14. Một bít được biểu diễn bằng
A. một chữ cái.                            B. một ki hiệu đặc biệt.
C. kí hiệu 0 hoặc 1.                      D. chữ số bất kì.
Câu 15. Bao nhiêu ‘bit’ tạo thành một ‘byte’?
A. 8.                  B.9.                 C.32.			D. 36
Câu 16. Một thẻ nhớ 4 GB lưu trữ được khoảng bao nhiêu ảnh 512 KB?
A. 2 nghìn ảnh.             B. 4 nghìn ảnh.	C. 8 nghìn ảnh.                D. 8 triệu ảnh
Câu 17. Một ổ cứng di động 2 TB có dung lượng nhớ tương đương bao nhiêu?
A. 2 048 KB.      		B. 1 024 MB.	C. 2 048 MB.                D. 2 048 GB.
Câu 18. Một mạng máy tính gồm
A. Tối thiểu năm máy tính được liên kết với nhau.
B. Một số máy tính bàn.
C. Hai hoặc nhiều máy tính được kết nối với nhau.
D. Tất cả các máy tinh trong một phòng hoặc trong một toà nhà.
Câu 19. Mạng máy tính không cho phép người sử dụng chia sẻ
A. Máy in		B. Bàn phím và chuột		C. Máy quét.		D. Dữ liệu
Câu 20 Trong các nhận định sau, nhận định nào không phải là lợi ích của việc sử dụng mạng máy tính?
A. Giảm chi phí khi dùng chung phần cứng.
B. Người sử dụng có quyền kiểm soát độc quyền đối với dữ liệu và ứng dụng của riêng họ.
C. Giảm chi phi khi dùng chung phần mềm.
D. Cho phép chia sẻ dữ liệu, tăng hiệu quả sử dụng.
Câu 21. Phát biểu nào sau đây không chính xác?
A. Mạng không dây thuận tiện cho những người di chuyển nhiều.
B. Mạng không dây dễ dàng lắp đặt hơn vì không cần khoan đục và lắp đặt đường dây.
C. Mạng không dây thường được sử dụng cho các thiết bị di động như máy tính bảng, điện thoại,...
D. Mạng không dây nhanh và ổn định hơn mạng có dây.
Câu 22. Mạng máy tính gồm các thành phần:
A. Máy tính và thiết bị kết nối.
B. Thiết bị đầu cuối và thiết bị kết nối.
C. Thiết bị đầu cuối, thiết bị kết nối và phần mềm mạng.
D. Máy tinh và phần mềm mạng.
Câu 23. Trong truyện “Cuộc điều tra màu đỏ", sau khi thu thập các chửng cứ, thám tử Sherlock Holmes đã lập luận để chứng minh Jefferson Hope là thủ phạm của vụ án. Hãy ghép mỗi hành động ở cột bên trái của thám tử với một hoạt động xử li thông tin phù hợp ờ cột bên phải.
1) Phán đoán, suy luận để chửng minh tội phạm	a) Thu nhận thông tin
2) Trinh bày lập luận trước toà án	b) Lưu trữ thông tin
3) Thu thập chứng cứ và các dấu vết	c) Xử lí thông tin
4) Ghi lại các sự kiện thu thập được ra giấy	d) Truyền thông tin

A. 1 - c ; 2 – d ;3 – a ; 4 – b 
B. 4 – b; 1 – c ; 2 – d ;3 – a  
C. 1 - c ; 2 – d ; 4 – b ;3 – a  
D. 1 - c ; 4 – b ; 2 – d ;3 – a 
Câu 24. Ghép mỗi ô ở cột bên trái với một ô ở cột bên phải cho phù hợp.

1) Thiết bị vào	a) gồm các bộ phận của máy tính có nhiệm vụ lưu trữ thông tin.
2) Thiết bị ra	b) gồm các bộ phận của máy tính thực hiện tất cả các tính toán và xử lí dữ liệu.
3) Bộ nhớ	c) gồm các bộ phận của máy tính có nhiệm vụ thu nhận thông tin vào máy tính.
4) Bộ xử lí	d) gồm các bộ phận của máy tính có nhiệm vụ giúp người sử dụng tiếp nhận thông tin từ máy tính.

A. 1 - c ; 2 – d ;3 – a ; 4 – b 
B. 4 – b; 1 – c ; 2 – d ;3 – a  
C. 1 - c ; 2 – d ; 4 – b ;3 – a  
D. 1 - c ; 4 – b ; 2 – d ;3 – a 
Câu 25. Thông tin là gì?
A. Các văn bản và số liệu.
B. Những gì đem lại hiểu biết cho con người về thế giới xung quanh và về chính bản thân mình. 
C. Văn bản, Hình ảnh, âm thanh.
D. Hình ảnh, âm thanh, tệp tin.
Câu 26. Thứ tự các hoạt động của quá trình xử lý thông tin bao gồm những gì? 
A. Thu nhận, lưu trữ, xử lý và truyển thông tin.
B. Thu nhận, xử lý,  lưu trữ và truyển thông tin.
C. Thu nhận, xử lý, truyển thông tin và lưu trữ.
D. Xử lý,  thu nhận, lưu trữ và truyển thông tin.
Câu 27. Máy tính gồm có bao nhiêu thành phần thực hiện các hoạt động xử lý thông tin
A. 2			B. 3			C. 4			D. 5
Câu 28. Thông tin khi đưa vào máy tính, chúng đều được biến đổi thành dạng chung đó là
A. dãy bit.		B. văn bản.		C. hình ảnh	.	D. âm thanh.
Câu 29. Kết quả của việc nhìn thấy hoặc nghe thấy ở con người được xếp vào hoạt động nào trong quá trình xử lí thông tin?
A. Thu nhận.	B. Lưu trữ.		 C. xử lí. 		D. Truyền.
Câu 30. Mạng máy tính cho phép người dùng chia sẻ
A. máy in.		B. bàn phím và chuột. 		C. bàn phím. 	  D. chuột.
Câu 31. Mạng máy tính gồm các thành phần nào?
A. Thiết bị đầu cuối, thiết bị kết nối và phần mềm mạng.  B. Máy tính và phần mềm mạng.
C. Máy tính và thiết bị kết nối.			D. Thiết bị đầu cuối và thiết bị kết nối.
Câu 32. Thiết bị nào dưới đây không phải là thiết bị đầu cuối?
A. Bộ định tuyến.		B. Máy tính. 		C. Điện thoại. 	     D. Máy in.
Câu 33. Người sử dụng có thể tìm kiếm, lưu trữ, trao đổi và chia sẻ thông tin một cách thuận lợi, nhanh chóng ở mọi lúc, mọi nơi là đặc điểm nào của Internet?
A. Tính dễ tiếp cận.					B. Tính toàn cầu.	
C. Tính tương tác.					D. Tính không chủ sở hữu.
Câu 34. Phát biểu nào sau đây không nêu đúng lợi ích của việc sử dụng Internet đối với học sinh?
A. Giúp giải trí bằng cách xem mạng xã hội và chơi điện tử suốt ngày.
B. Giúp nâng cao kiến thức bằng cách tham gia khóa học trực tuyến.
C. Giúp tiết kiệm thời gian và cung cấp nhiều tư liệu làm bài tập.
D. Giúp giao lưu kết bạn.
Câu 35. Trong trường hợp nào dưới đây mạng không dây tiện dụng hơn mạng có dây?
A. Mạng không dây ổn định hơn mạng có dây.
B. Các thiết bị có thể linh hoạt thay đổi vị trí mà vẫn duy trì kết nối mạng.
C. Mạng không dây trao đổi thông tin tốc độ cao hơn mạng có dây.
D. Mạng không dây trao đổi thông tin có tính bảo mật cao hơn mạng có dây.
Câu 36. Phát biểu nào sau đây là SAI?
A. Mạng không dây thuận tiện cho những người di chuyển nhiều.
B. Mạng không dây nhanh và ổn định hơn mạng có dây.
C. Mạng không dây thường được sử dụng cho các thiết bị di động như máy tính bảng, điện thoại,...
D. Mạng không dây dễ dàng lắp đặt hơn vì không cần khoan đục, lắp đặt đường dây.
Câu 37. World Wide Web là gì? 
A. Một trò chơi máy tính.		B. Mạng thông tin toàn cầu.
C.	Một phần mềm máy tính. 	D. Tên khác của Internet.
Câu 38. Mỗi website bắt buộc phải có
A. tên cá nhân hoặc tổ chức sở hữu.		B. một địa chỉ truy cập.
C. địa chỉ trụ sở của đơn vị sở hữu.		D. địa chỉ thư điện tử.
Câu 39. Phần mềm giúp người sử dụng truy cập các trang web trên Internet gọi là gì?
A. Website.						B. Địa chỉ web.
C. Trình duyệt web.					D. Công cụ tìm kiếm.
Câu 40. Địa chỉ trang web nào sau đây là hợp lệ?
A. https \\: www. tienphong.vn .			B. www \\ tienphong.vn .
C. https://www.tienphong.vn .			D.  //ww: tienphong.vn .
Câu 41. Khái niệm Internet dùng để chỉ điều gì? 
A. Mạng máy tính toàn cầu, kết nối hàng triệu máy tính và mạng máy tính trên khắp thế giới. 
B. Mạng máy tính chỉ giới hạn trong một thành phố. 
C. Bộ phận của một máy tính dùng để truy cập thông tin. 
D. Phần mềm ứng dụng để đọc báo và xem phim.
Câu 42. Đặc điểm nào sau đây không phải là đặc điểm chính của Internet? 
A. Chỉ có thể dùng để trao đổi thư điện tử.
B. Cung cấp kho thông tin đa dạng, khổng lồ. 
C. Mang tính toàn cầu.
D. Hỗ trợ nhiều dịch vụ (học tập, giao tiếp, giải trí).
Câu 43. Thông tin được cập nhật thường xuyên là đặc điểm nào của Internet?
A. Tính cập nhật.					B. Tính toàn cầu.	
C. Tính tương tác.					D. Tính không chủ sở hữu.
Câu 44. Phát biểu nào sau đây không nêu đúng lợi ích của việc sử dụng Internet đối với học sinh?
A. Giúp giải trí bằng cách chơi trò chơi trực tuyến suốt ngày.
B. Giúp nâng cao kiến thức bằng cách tham gia khóa học trực tuyến.
C. Giúp tiết kiệm thời gian và cung cấp nhiều tư liệu làm bài tập.
D. Giúp giao lưu kết bạn.
Câu 45. Tại sao thư điện tử nhanh hơn thư truyền thống? 
A. Vì phải chờ nhân viên bưu điện giao.	B. Vì gửi và nhận tức thì qua mạng Internet. 
C. Vì viết tay chậm.	D. Vì cần giấy mực.
Câu 46. Ưu điểm chính của thư điện tử so với thư truyền thống là gì?
A. Có tính pháp lý cao hơn. 	B. Nhanh chóng, chi phí thấp, gửi kèm tệp dễ dàng. 
C. Có thể gửi vật liệu thực tế. 	D. Không cần mạng.
D. Mạng không dây dễ dàng lắp đặt hơn vì không cần khoan đục, lắp đặt đường dây.
Câu 47. World Wide Web là gì? 
A. Một trò chơi máy tính.		B. Mạng thông tin toàn cầu.
C.	 Một phần mềm máy tính. 	D. Tên khác của Internet.
Câu 48. Một người có thể mở bao nhiêu tài khoản thư điện tử? 
A. Chỉ một tài khoản duy nhất. 		B. Nhiều tài khoản với các tên khác nhau. 
C. Không thể mở tài khoản. 		D. Chỉ hai tài khoản.
Câu 49. Phần mềm giúp người sử dụng truy cập các trang web trên Internet gọi là gì?
A. Website.							B. Địa chỉ web.
C. Trình duyệt web.					D. Công cụ tìm kiếm.
Câu 50. Địa chỉ trang web nào sau đây là hợp lệ?
A. https \\: www. thanhnien.vn .			B. www \\ thanhnien.vn .
C. https://www.thanhnien.vn .				D.  //ww: thanhnien.vn .
Câu 51. Địa chỉ thư điện tử có dạng 
A. <Tên người sử dụng>&<Tên máy chủ thư điện tử>.
B. <Tên người sử dụng>@<Địa chỉ nơi ở người sử dụng>.
C. <Tên đăng nhập>@<Địa chỉ máy chủ thư điện tử>.
D. <Tên đăng nhập>#<Địa chỉ máy chủ thư điện tử>.
Câu 52. Để đăng nhập hộp thư điện tử cần gì? 
A. Số điện thoại cố định.						B. Địa chỉ nhà. 
C. Tên đăng nhập và mật khẩu. 					D. Giấy tờ tùy thân.
Câu 53. Trang được mở ra đầu tiên khi truy cập website gọi là
A. trang con.			B. website.		C. trang mở đầu.	D. trang chủ.
Câu 54. Địa chỉ thư điện tử nào sau đây không chính xác?
A. thcstinhson@gmail.com.				B. thcstinhson@qn.edu.vn.
C. thcstinhson@yahoo.com.				D. thcstinhson.gmail.com.
Câu 55. Thư điện tử góp phần vào trao đổi thông tin như thế nào trong học tập? 
A. Chỉ dùng để chơi game. 				B. Chỉ gửi thư tay.
C. Không hữu ích. 		D. Gửi bài tập, tài liệu nhanh chóng cho bạn bè, thầy cô.
Câu 56. Để tìm kiếm thông tin về ngày thành lập quân đội nhân dân Việt Nam 22/12  em sử dụng từ khóa nào sau đây để thu hẹp phạm vi tìm kiếm?
A. Ngày thành lập quân đội nhân dân Việt Nam 22/12.
B. Quân đội nhân dân Việt Nam.
C. “Quân đội nhân dân” + “Việt Nam”.				
D. “Ngày thành lập quân đội nhân dân Việt Nam 22/12”.

phần đáp án 1. C	2. A	3. D	4 .B	5. B	6. D	7. C	8. A	9. B	10. A
11. C	12. B	13. D	14. C	15. A	16. C	17. D	18. C	19. B	20. B
21. D	22. C	23. A	24. A	25. B	26. A	27. C	28. A	29. A	30. A
31.A	32.A	33.A	34.A	35.B	36.B	37.B	38.B	39.C	40.C
41.A	42.A	43.A	44.A	45.B	46.B	47.B	48.B	49.C	50.C
51.C	52.C	53.D	54.D	55.D	56.D				

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

