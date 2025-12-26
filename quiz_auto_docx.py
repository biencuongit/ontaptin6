import streamlit as st
import random
import time

# ====================== DỮ LIỆU ĐỀ THI - NHẬP THỦ CÔNG TỪ TỆP ======================

# PHẦN I: TRẮC NGHIỆM (56 câu)
trac_nghiem = [
    {"cau": 1, "question": "Phát biểu nào sau đây là đúng?", "options": ["A. Dữ liệu chỉ có thể được hiểu bởi những người có trình độ cao.", "B. Dữ liệu là những giá trị số do con người nghĩ ra.", "C. Dữ liệu được thể hiện dưới dạng con số, văn bản, hình ảnh, âm thanh.", "D. Dữ liệu chỉ có ở trong máy tính."], "answer": "C"},
    {"cau": 2, "question": "Xem bản tin dự báo thời tiết như Hình 1, bạn Khoa kết luận: \"Hôm nay, trời có mưa\". Phát biểu nào sau đây đúng?", "options": ["A. Bản tin dự báo thời tiết là dữ liệu, kết luận của Khoa là thông tin.", "B. Bản tin dự báo thời tiết là thông tin, kết luận của Khoa là dữ liệu.", "C. Những con số trong bản tin dự báo thời tiết là thông tin.", "D. Bản tin dự báo thời tiết và kết luận của Khoa đều là dữ liệu"], "answer": "A"},
    {"cau": 3, "question": "Phát biểu nào sau đây đúng về lợi ích của thông tin?", "options": ["A. Có độ tin cậy cao, đem lại hiểu biết cho con người.", "B. Đem lại hiểu biết cho con người, không phụ thuộc vào dữ liệu.", "C. Có độ tin cậy cao, không phụ thuộc vào dữ liệu.", "D. Đem lại hiểu biết và giúp con người có những lựa chọn tốt."], "answer": "D"},
    {"cau": 4, "question": "Các hoạt động xử lí thông tin gồm:", "options": ["A. Đầu vào, đầu ra.", "B. Thu nhận, xử lí, lưu trữ, truyền.", "C. Nhìn, nghe, suy đoán, kết luận.", "D. Mở bài, thân bài, kết luận."], "answer": "B"},
    {"cau": 5, "question": "Thao tác ghi nhớ và cất giữ tài liệu của con người được xếp vào hoạt động nào trong quá trình xử lí thông tin?", "options": ["A. Thu nhận.", "B. Lưu trữ", "C. Xử lí.", "D. Truyền."], "answer": "B"},
    {"cau": 6, "question": "Các thao tác nói, chia sẻ, thông báo, tuyên truyền, biểu đạt, trò chuyện,... của con người được xếp vào hoạt động nào trong quá trình xử lí thông tin?", "options": ["A. Thu nhận.", "B. Lưu trữ.", "C. Xử lí.", "D. Truyền."], "answer": "D"},
    {"cau": 7, "question": "Bàn phím, chuột, máy quét và webcam là những ví dụ về loại thiết bị nào của máy tính?", "options": ["A. Thiết bị ra.", "B. Thiết bị lưu trữ.", "C. Thiết bị vào.", "D. Bộ nhớ."], "answer": "C"},
    {"cau": 8, "question": "Thiết bị nào sau đây không phải là thiết bị ra của máy tính?", "options": ["A. Micro.", "B. Máy in.", "C. Màn hình.", "D. Loa."], "answer": "A"},
    {"cau": 9, "question": "Đặc điểm nào sau đây không thuộc về máy tính?", "options": ["A. Thực hiện nhanh và chính xác.", "B. Suy nghĩ sáng tạo", "C. Lưu trữ lớn", "D. Hoạt động bền bỉ"], "answer": "B"},
    {"cau": 10, "question": "Đơn vị đo dữ liệu nào sau đây là lớn nhất?", "options": ["A. Gigabyte.", "B. Megabyte,", "C. Kilobyte.", "D. Bit."], "answer": "A"},
    {"cau": 11, "question": "Tệp ảnh Hà Nội có dung lượng bao nhiêu? (giả sử từ hình)", "options": ["A. 103 byte.", "B. 103 kilobit", "C. 103 kilobyte.", "D. 0,846 megabyte."], "answer": "C"},
    {"cau": 12, "question": "Dữ liệu được máy tính lưu trữ dưới dạng", "options": ["A. thông tin.", "B. dãy bít.", "C. số thập phân.", "D. các kí tự."], "answer": "B"},
    {"cau": 13, "question": "Dữ liệu trong máy tính được mã hoá thành dãy bít vì", "options": ["A. dãy bít đáng tin cậy hơn.", "B. dãy bít được xử lí dễ dàng hơn.", "C. dãy bít chiếm ít dung lượng nhớ hơn.", "D. máy tính chỉ làm việc với hai kí hiệu 0 và 1."], "answer": "D"},
    {"cau": 14, "question": "Một bít được biểu diễn bằng", "options": ["A. một chữ cái.", "B. một ki hiệu đặc biệt.", "C. kí hiệu 0 hoặc 1.", "D. chữ số bất kì."], "answer": "C"},
    {"cau": 15, "question": "Bao nhiêu ‘bit’ tạo thành một ‘byte’?", "options": ["A. 8.", "B. 9.", "C. 32.", "D. 36"], "answer": "A"},
    {"cau": 16, "question": "Một thẻ nhớ 4 GB lưu trữ được khoảng bao nhiêu ảnh 512 KB?", "options": ["A. 2 nghìn ảnh.", "B. 4 nghìn ảnh.", "C. 8 nghìn ảnh.", "D. 8 triệu ảnh"], "answer": "C"},
    {"cau": 17, "question": "Một ổ cứng di động 2 TB có dung lượng nhớ tương đương bao nhiêu?", "options": ["A. 2 048 KB.", "B. 1 024 MB.", "C. 2 048 MB.", "D. 2 048 GB."], "answer": "D"},
    {"cau": 18, "question": "Một mạng máy tính gồm", "options": ["A. Tối thiểu năm máy tính được liên kết với nhau.", "B. Một số máy tính bàn.", "C. Hai hoặc nhiều máy tính được kết nối với nhau.", "D. Tất cả các máy tính trong một phòng hoặc trong một toà nhà."], "answer": "C"},
    {"cau": 19, "question": "Mạng máy tính không cho phép người sử dụng chia sẻ", "options": ["A. Máy in", "B. Bàn phím và chuột", "C. Máy quét.", "D. Dữ liệu"], "answer": "B"},
    {"cau": 20, "question": "Trong các nhận định sau, nhận định nào không phải là lợi ích của việc sử dụng mạng máy tính?", "options": ["A. Giảm chi phí khi dùng chung phần cứng.", "B. Người sử dụng có quyền kiểm soát độc quyền đối với dữ liệu và ứng dụng của riêng họ.", "C. Giảm chi phí khi dùng chung phần mềm.", "D. Cho phép chia sẻ dữ liệu, tăng hiệu quả sử dụng."], "answer": "B"},
    {"cau": 21, "question": "Phát biểu nào sau đây không chính xác?", "options": ["A. Mạng không dây thuận tiện cho những người di chuyển nhiều.", "B. Mạng không dây dễ dàng lắp đặt hơn vì không cần khoan đục và lắp đặt đường dây.", "C. Mạng không dây thường được sử dụng cho các thiết bị di động như máy tính bảng, điện thoại,...", "D. Mạng không dây nhanh và ổn định hơn mạng có dây."], "answer": "D"},
    {"cau": 22, "question": "Mạng máy tính gồm các thành phần:", "options": ["A. Máy tính và thiết bị kết nối.", "B. Thiết bị đầu cuối và thiết bị kết nối.", "C. Thiết bị đầu cuối, thiết bị kết nối và phần mềm mạng.", "D. Máy tính và phần mềm mạng."], "answer": "C"},
    {"cau": 23, "question": "Ghép hành động của Sherlock Holmes với hoạt động xử lí thông tin (theo truyện)", "options": ["A. 1 - c ; 2 – d ;3 – a ; 4 – b", "B. 4 – b; 1 – c ; 2 – d ;3 – a", "C. 1 - c ; 2 – d ; 4 – b ;3 – a", "D. 1 - c ; 4 – b ; 2 – d ;3 – a"], "answer": "D"},
    {"cau": 24, "question": "Ghép mỗi ô ở cột bên trái với một ô ở cột bên phải cho phù hợp.", "options": ["A. 1 - c ; 2 – d ;3 – a ; 4 – b", "B. 4 – b; 1 – c ; 2 – d ;3 – a", "C. 1 - c ; 2 – d ; 4 – b ;3 – a", "D. 1 - c ; 4 – b ; 2 – d ;3 – a"], "answer": "D"},
    {"cau": 25, "question": "Thông tin là gì?", "options": ["A. Các văn bản và số liệu.", "B. Những gì đem lại hiểu biết cho con người về thế giới xung quanh và về chính bản thân mình.", "C. Văn bản, Hình ảnh, âm thanh.", "D. Hình ảnh, âm thanh, tệp tin."], "answer": "B"},
    {"cau": 26, "question": "Thứ tự các hoạt động của quá trình xử lý thông tin bao gồm những gì?", "options": ["A. Thu nhận, lưu trữ, xử lý và truyền thông tin.", "B. Thu nhận, xử lý, lưu trữ và truyền thông tin.", "C. Thu nhận, xử lý, truyền thông tin và lưu trữ.", "D. Xử lý, thu nhận, lưu trữ và truyền thông tin."], "answer": "B"},
    {"cau": 27, "question": "Máy tính gồm có bao nhiêu thành phần thực hiện các hoạt động xử lý thông tin", "options": ["A. 2", "B. 3", "C. 4", "D. 5"], "answer": "C"},
    {"cau": 28, "question": "Thông tin khi đưa vào máy tính, chúng đều được biến đổi thành dạng chung đó là", "options": ["A. dãy bit.", "B. văn bản.", "C. hình ảnh.", "D. âm thanh."], "answer": "A"},
    {"cau": 29, "question": "Kết quả của việc nhìn thấy hoặc nghe thấy ở con người được xếp vào hoạt động nào trong quá trình xử lí thông tin?", "options": ["A. Thu nhận.", "B. Lưu trữ.", "C. Xử lí.", "D. Truyền."], "answer": "A"},
    {"cau": 30, "question": "Mạng máy tính cho phép người dùng chia sẻ", "options": ["A. máy in.", "B. bàn phím và chuột.", "C. bàn phím.", "D. chuột."], "answer": "A"},
    {"cau": 31, "question": "Mạng máy tính gồm các thành phần nào?", "options": ["A. Thiết bị đầu cuối, thiết bị kết nối và phần mềm mạng.", "B. Máy tính và phần mềm mạng.", "C. Máy tính và thiết bị kết nối.", "D. Thiết bị đầu cuối và thiết bị kết nối."], "answer": "A"},
    {"cau": 32, "question": "Thiết bị nào dưới đây không phải là thiết bị đầu cuối?", "options": ["A. Bộ định tuyến.", "B. Máy tính.", "C. Điện thoại.", "D. Máy in."], "answer": "A"},
    {"cau": 33, "question": "Người sử dụng có thể tìm kiếm, lưu trữ, trao đổi và chia sẻ thông tin một cách thuận lợi, nhanh chóng ở mọi lúc, mọi nơi là đặc điểm nào của Internet?", "options": ["A. Tính dễ tiếp cận.", "B. Tính toàn cầu.", "C. Tính tương tác.", "D. Tính không chủ sở hữu."], "answer": "A"},
    {"cau": 34, "question": "Phát biểu nào sau đây không nêu đúng lợi ích của việc sử dụng Internet đối với học sinh?", "options": ["A. Giúp giải trí bằng cách xem mạng xã hội và chơi điện tử suốt ngày.", "B. Giúp nâng cao kiến thức bằng cách tham gia khóa học trực tuyến.", "C. Giúp tiết kiệm thời gian và cung cấp nhiều tư liệu làm bài tập.", "D. Giúp giao lưu kết bạn."], "answer": "A"},
    {"cau": 35, "question": "Trong trường hợp nào dưới đây mạng không dây tiện dụng hơn mạng có dây?", "options": ["A. Mạng không dây ổn định hơn mạng có dây.", "B. Các thiết bị có thể linh hoạt thay đổi vị trí mà vẫn duy trì kết nối mạng.", "C. Mạng không dây trao đổi thông tin tốc độ cao hơn mạng có dây.", "D. Mạng không dây trao đổi thông tin có tính bảo mật cao hơn mạng có dây."], "answer": "A"},
    {"cau": 36, "question": "Phát biểu nào sau đây là SAI?", "options": ["A. Mạng không dây thuận tiện cho những người di chuyển nhiều.", "B. Mạng không dây nhanh và ổn định hơn mạng có dây.", "C. Mạng không dây thường được sử dụng cho các thiết bị di động như máy tính bảng, điện thoại,...", "D. Mạng không dây dễ dàng lắp đặt hơn vì không cần khoan đục, lắp đặt đường dây."], "answer": "B"},
    {"cau": 37, "question": "World Wide Web là gì?", "options": ["A. Một trò chơi máy tính.", "B. Mạng thông tin toàn cầu.", "C. Một phần mềm máy tính.", "D. Tên khác của Internet."], "answer": "D"},
    {"cau": 38, "question": "Mỗi website bắt buộc phải có", "options": ["A. tên cá nhân hoặc tổ chức sở hữu.", "B. một địa chỉ truy cập.", "C. địa chỉ trụ sở của đơn vị sở hữu.", "D. địa chỉ thư điện tử."], "answer": "B"},
    {"cau": 39, "question": "Phần mềm giúp người sử dụng truy cập các trang web trên Internet gọi là gì?", "options": ["A. Website.", "B. Địa chỉ web.", "C. Trình duyệt web.", "D. Công cụ tìm kiếm."], "answer": "C"},
    {"cau": 40, "question": "Địa chỉ trang web nào sau đây là hợp lệ?", "options": ["A. https \\: www. tienphong.vn .", "B. www \\ tienphong.vn .", "C. https://www.tienphong.vn .", "D.  //ww: tienphong.vn ."], "answer": "C"},
    {"cau": 41, "question": "Khái niệm Internet dùng để chỉ điều gì?", "options": ["A. Mạng máy tính toàn cầu, kết nối hàng triệu máy tính và mạng máy tính trên khắp thế giới.", "B. Mạng máy tính chỉ giới hạn trong một thành phố.", "C. Bộ phận của một máy tính dùng để truy cập thông tin.", "D. Phần mềm ứng dụng để đọc báo và xem phim."], "answer": "A"},
    {"cau": 42, "question": "Đặc điểm nào sau đây không phải là đặc điểm chính của Internet?", "options": ["A. Chỉ có thể dùng để trao đổi thư điện tử.", "B. Cung cấp kho thông tin đa dạng, khổng lồ.", "C. Mang tính toàn cầu.", "D. Hỗ trợ nhiều dịch vụ (học tập, giao tiếp, giải trí)."], "answer": "A"},
    {"cau": 43, "question": "Thông tin được cập nhật thường xuyên là đặc điểm nào của Internet?", "options": ["A. Tính cập nhật.", "B. Tính toàn cầu.", "C. Tính tương tác.", "D. Tính không chủ sở hữu."], "answer": "A"},
    {"cau": 44, "question": "Phát biểu nào sau đây không nêu đúng lợi ích của việc sử dụng Internet đối với học sinh?", "options": ["A. Giúp giải trí bằng cách chơi trò chơi trực tuyến suốt ngày.", "B. Giúp nâng cao kiến thức bằng cách tham gia khóa học trực tuyến.", "C. Giúp tiết kiệm thời gian và cung cấp nhiều tư liệu làm bài tập.", "D. Giúp giao lưu kết bạn."], "answer": "A"},
    {"cau": 45, "question": "Tại sao thư điện tử nhanh hơn thư truyền thống?", "options": ["A. Vì phải chờ nhân viên bưu điện giao.", "B. Vì gửi và nhận tức thì qua mạng Internet.", "C. Vì viết tay chậm.", "D. Vì cần giấy mực."], "answer": "B"},
    {"cau": 46, "question": "Ưu điểm chính của thư điện tử so với thư truyền thống là gì?", "options": ["A. Có tính pháp lý cao hơn.", "B. Nhanh chóng, chi phí thấp, gửi kèm tệp dễ dàng.", "C. Có thể gửi vật liệu thực tế.", "D. Không cần mạng."], "answer": "B"},
    {"cau": 47, "question": "World Wide Web là gì?", "options": ["A. Một trò chơi máy tính.", "B. Mạng thông tin toàn cầu.", "C. Một phần mềm máy tính.", "D. Tên khác của Internet."], "answer": "D"},
    {"cau": 48, "question": "Một người có thể mở bao nhiêu tài khoản thư điện tử?", "options": ["A. Chỉ một tài khoản duy nhất.", "B. Nhiều tài khoản với các tên khác nhau.", "C. Không thể mở tài khoản.", "D. Chỉ hai tài khoản."], "answer": "B"},
    {"cau": 49, "question": "Phần mềm giúp người sử dụng truy cập các trang web trên Internet gọi là gì?", "options": ["A. Website.", "B. Địa chỉ web.", "C. Trình duyệt web.", "D. Công cụ tìm kiếm."], "answer": "C"},
    {"cau": 50, "question": "Địa chỉ trang web nào sau đây là hợp lệ?", "options": ["A. https \\: www. thanhnien.vn .", "B. www \\ thanhnien.vn .", "C. https://www.thanhnien.vn .", "D.  //ww: thanhnien.vn ."], "answer": "C"},
    {"cau": 51, "question": "Địa chỉ thư điện tử có dạng", "options": ["A. <Tên người sử dụng>&<Tên máy chủ thư điện tử>.", "B. <Tên người sử dụng>@<Địa chỉ nơi ở người sử dụng>.", "C. <Tên đăng nhập>@<Địa chỉ máy chủ thư điện tử>.", "D. <Tên đăng nhập>#<Địa chỉ máy chủ thư điện tử>."], "answer": "C"},
    {"cau": 52, "question": "Để đăng nhập hộp thư điện tử cần gì?", "options": ["A. Số điện thoại cố định.", "B. Địa chỉ nhà.", "C. Tên đăng nhập và mật khẩu.", "D. Giấy tờ tùy thân."], "answer": "C"},
    {"cau": 53, "question": "Trang được mở ra đầu tiên khi truy cập website gọi là", "options": ["A. trang con.", "B. website.", "C. trang mở đầu.", "D. trang chủ."], "answer": "D"},
    {"cau": 54, "question": "Địa chỉ thư điện tử nào sau đây không chính xác?", "options": ["A. thcstinhson@gmail.com.", "B. thcstinhson@qn.edu.vn.", "C. (không có C)", "D. thcstinhson.gmail.com."], "answer": "D"},
    {"cau": 55, "question": "Thư điện tử góp phần vào trao đổi thông tin như thế nào trong học tập?", "options": ["A. Chỉ dùng để chơi game.", "B. Chỉ gửi thư tay.", "C. Không hữu ích.", "D. Gửi bài tập, tài liệu nhanh chóng cho bạn bè, thầy cô."], "answer": "D"},
    {"cau": 56, "question": "Để tìm kiếm thông tin về ngày thành lập quân đội nhân dân Việt Nam 22/12 em sử dụng từ khóa nào sau đây để thu hẹp phạm vi tìm kiếm?", "options": ["A. Ngày thành lập quân đội nhân dân Việt Nam 22/12.", "B. Quân đội nhân dân Việt Nam.", "C. “Quân đội nhân dân” + “Việt Nam”.", "D. “Ngày thành lập quân đội nhân dân Việt Nam 22/12”."], "answer": "D"},
]

# PHẦN II: TỰ LUẬN (8 câu)
tu_luan = [
    {"cau": 57, "question": "Máy tìm kiếm là gì?", "dap_an": "Máy tìm kiếm là một website đặc biệt, giúp người sử dụng tìm kiếm thông tin trên Internet một cách nhanh chóng, hiệu quả thông qua các từ khóa."},
    {"cau": 58, "question": "Nêu những ưu, nhược điểm cơ bản của dịch vụ thư điện tử.", "dap_an": "- Ưu điểm: chi phí thấp, tiết kiệm thời gian, thuận tiện, gửi kèm tệp dễ dàng...\n- Nhược điểm: phải sử dụng phương tiện điện tử kết nối mạng, có thể gặp một số nguy cơ, phiền toái (thư rác, virus...)."},
    {"cau": 59, "question": "Trong chuyến du lịch cùng gia đình, An đã sử dụng điện thoại để chụp ảnh và gửi cho bạn thân của mình. Vậy điện thoại đã giúp An thu thập, lưu trữ và truyền thông tin như thế nào?", "dap_an": "- Chụp ảnh: thu nhận thông tin.\n- Lưu trong bộ nhớ điện thoại: lưu trữ thông tin.\n- Gửi cho bạn: truyền thông tin."},
    {"cau": 60, "question": "Một bài hát có dung lượng 2MB, vậy USB 32GB có thể chứa bao nhiêu bài hát?", "dap_an": "32GB = 32 × 1024 = 32768 MB\n32768 ÷ 2 = 16384 bài hát."},
    {"cau": 61, "question": "Website là gì?", "dap_an": "Website là tập hợp các trang web liên quan được truy cập thông qua một địa chỉ."},
    {"cau": 62, "question": "So sánh việc tìm kiếm thông tin bằng từ khóa và từ khóa đặt trong dấu ngoặc kép.", "dap_an": "- Từ khóa thường: tìm các trang có chứa từng từ riêng lẻ → kết quả rộng.\n- Trong ngoặc kép: tìm chính xác cụm từ → kết quả sát hơn."},
    {"cau": 63, "question": "Trong buổi sinh hoạt dưới cờ, Thầy Quy đã sử dụng điện thoại để chụp hình và sử dụng Zalo gửi cho thầy Cương. Vậy điện thoại đã giúp thầy Quy thu thập, lưu trữ và truyền thông tin như thế nào?", "dap_an": "- Chụp hình: thu nhận thông tin.\n- Lưu trong bộ nhớ: lưu trữ thông tin.\n- Gửi qua Zalo: truyền thông tin."},
    {"cau": 64, "question": "Một ổ cứng có dung lượng là 64GB. Hiện tại ổ cứng này đã chứa tệp video 4GB. Vậy ổ cứng này có thể chứa thêm tối đa bao nhiêu tệp ảnh. Biết rằng mỗi tệp ảnh có dung lượng 5MB.", "dap_an": "Dung lượng còn lại: 64 - 4 = 60GB = 60 × 1024 = 61440 MB\n61440 ÷ 5 = 12288 tệp ảnh."},
]

# ====================== ỨNG DỤNG STREAMLIT ======================
st.set_page_config(page_title="Kiểm tra Tin học 6 - HK1 2025-2026", layout="centered")
st.title("📘 Kiểm tra học kỳ 1 - Tin học lớp 6")
st.markdown("**Năm học 2025-2026**")

# Khởi tạo session state
if 'mode' not in st.session_state:
    st.session_state.mode = None
if 'ten_hs' not in st.session_state:
    st.session_state.ten_hs = ""
if 'lop' not in st.session_state:
    st.session_state.lop = ""
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'shuffled_tracnghiem' not in st.session_state:
    st.session_state.shuffled_tracnghiem = []

# Trang chọn chế độ
if st.session_state.mode is None:
    st.markdown("### 🎯 Chọn chế độ làm bài")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📚 **Chế độ Ôn tập** (xem đáp án ngay)", use_container_width=True):
            st.session_state.mode = "on_tap"
            st.rerun()
    with col2:
        if st.button("✍️ **Chế độ Kiểm tra** (như thi thật)", use_container_width=True):
            st.session_state.mode = "kiem_tra"
            st.rerun()

# Chế độ ôn tập
if st.session_state.mode == "on_tap":
    st.success("📖 Chế độ ôn tập - Xem câu hỏi và đáp án chi tiết")
    tabs = st.tabs(["Trắc nghiệm (56 câu)", "Tự luận (8 câu)"])
    with tabs[0]:
        for q in trac_nghiem:
            st.markdown(f"**Câu {q['cau']}.** {q['question']}")
            for opt in q['options']:
                if opt.startswith(q['answer']):
                    st.success(opt + " ← Đáp án đúng")
                else:
                    st.write(opt)
            st.markdown("---")
    with tabs[1]:
        for q in tu_luan:
            st.markdown(f"**Câu {q['cau']}.** {q['question']}")
            st.info(q['dap_an'])
            st.markdown("---")

# Chế độ kiểm tra
if st.session_state.mode == "kiem_tra":
    # Nhập thông tin học sinh
    if not st.session_state.ten_hs:
        st.info("Vui lòng nhập thông tin trước khi làm bài")
        ten = st.text_input("Họ và tên học sinh")
        lop = st.text_input("Lớp (ví dụ: 6A1, 6A2)")
        if st.button("Bắt đầu làm bài"):
            if ten.strip() and lop.strip():
                st.session_state.ten_hs = ten.strip()
                st.session_state.lop = lop.strip()
                st.session_state.start_time = time.time()

                # Đảo ngẫu nhiên câu hỏi trắc nghiệm và đáp án
                shuffled = trac_nghiem.copy()
                random.shuffle(shuffled)
                for q in shuffled:
                    correct_opt = q['answer']
                    opts = q['options'].copy()
                    random.shuffle(opts)
                    q['shuffled_options'] = opts
                    q['correct_option_text'] = next(o for o in opts if o.startswith(correct_opt))
                st.session_state.shuffled_tracnghiem = shuffled
                st.rerun()
            else:
                st.error("Vui lòng nhập đầy đủ tên và lớp!")
    else:
        st.markdown(f"**Học sinh:** {st.session_state.ten_hs} **Lớp:** {st.session_state.lop}")

        # Đồng hồ đếm ngược 45 phút
        if st.session_state.start_time:
            elapsed = time.time() - st.session_state.start_time
            remaining = max(2700 - int(elapsed), 0)
            mins, secs = divmod(remaining, 60)
            st.markdown(f"⏰ **Thời gian còn lại:** {mins:02d}:{secs:02d}")

            if remaining == 0 and not st.session_state.submitted:
                st.session_state.submitted = True
                st.rerun()

        if not st.session_state.submitted:
            st.markdown("### Phần I: Trắc nghiệm (56 câu - mỗi câu 0.15 điểm)")
            for i, q in enumerate(st.session_state.shuffled_tracnghiem):
                st.write(f"**Câu {i+1}:** {q['question']}")
                key = f"tn_{i}"
                chosen = st.radio("Chọn đáp án:", q['shuffled_options'], key=key, label_visibility="collapsed")
                st.session_state.answers[key] = chosen

            st.markdown("### Phần II: Tự luận (8 câu)")
            for i, q in enumerate(tu_luan):
                st.markdown(f"**Câu {q['cau']}:** {q['question']}")
                key = f"tl_{i}"
                st.session_state.answers[key] = st.text_area("Trả lời:", key=key, height=120, label_visibility="collapsed")

            if st.button("📤 **NỘP BÀI**", type="primary", use_container_width=True):
                st.session_state.submitted = True
                st.rerun()

        # Kết quả
        else:
            # Chấm trắc nghiệm
            diem_tracnghiem = 0
            for i, q in enumerate(st.session_state.shuffled_tracnghiem):
                key = f"tn_{i}"
                user_answer = st.session_state.answers.get(key, "")
                if user_answer == q['correct_option_text']:
                    diem_tracnghiem += 0.15

            # Tự luận tạm cho tối đa 1.6 điểm (có thể chấm tay sau)
            diem_tuluan = 1.6
            tong_diem = round(diem_tracnghiem + diem_tuluan, 1)

            st.balloons()
            st.success(f"### 🎉 Kết quả kiểm tra")
            st.markdown(f"**Học sinh:** {st.session_state.ten_hs}  |  **Lớp:** {st.session_state.lop}")
            st.markdown(f"**Điểm số:** {tong_diem} / 10")

            if tong_diem >= 6.0:
                st.success("🎊 Chúc mừng! Bạn đạt từ 6 điểm trở lên → Được xem đáp án chi tiết")

                with st.expander("📌 Đáp án Trắc nghiệm"):
                    for i, q in enumerate(st.session_state.shuffled_tracnghiem):
                        user = st.session_state.answers.get(f"tn_{i}", "Chưa trả lời")
                        correct = q['correct_option_text']
                        st.write(f"**Câu {i+1}:** Đáp án đúng → **{correct}**")
                        if user == correct:
                            st.success("✅ Đúng")
                        else:
                            st.error(f"Sai - Bạn chọn: {user}")

                with st.expander("📝 Đáp án Tự luận"):
                    for q in tu_luan:
                        st.markdown(f"**Câu {q['cau']}:** {q['question']}")
                        st.info(q['dap_an'])
                        st.markdown("---")
            else:
                st.warning("📚 Bạn chưa đạt 6 điểm. Hãy ôn lại kỹ và làm lại nhé!\nĐáp án sẽ chỉ hiển thị khi bạn đạt từ 6 điểm trở lên.")

            if st.button("🔄 Làm lại bài (xóa toàn bộ)"):
                st.session_state.clear()
                st.rerun()

st.caption("Ứng dụng ôn tập và kiểm tra Tin học lớp 6 - Học kỳ 1 năm 2025-2026")
