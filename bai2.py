'''
print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")

# Vòng lặp chạy đúng 3 lần cho 3 nhân viên
for employee_number in range(1, 4):
    print("--- Đang xử lý nhân viên số", employee_number, "---")

    # Yêu cầu kế toán nhập dữ liệu
    working_days = int(input("Nhập số ngày công trong tháng: "))

    # Kiểm tra điều kiện
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")

    bonus_amount = working_days * 200000
    print("→ Đã gửi Email: Chúc mừng nhận được", bonus_amount, "VNĐ tiền thưởng!")
    print("---------------------------------------------------\n")

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")
-- nếu người dùng nhập 0 vào thì vòng lặp k gặp bất kì cái nào ngăn nó lại, phải có thêm từ khóa continue để khi nhập 0 nó chỉ đưa ra thông báo chứ k hiện chức mừng
'''
print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")

# Vòng lặp chạy đúng 3 lần cho 3 nhân viên
for employee_number in range(1, 4):
    print("--- Đang xử lý nhân viên số", employee_number, "---")

    # Yêu cầu kế toán nhập dữ liệu
    working_days = int(input("Nhập số ngày công trong tháng: "))

    # Kiểm tra điều kiện
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        continue
    bonus_amount = working_days * 200000
    print("→ Đã gửi Email: Chúc mừng nhận được", bonus_amount, "VNĐ tiền thưởng!")
    print("---------------------------------------------------\n")

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")