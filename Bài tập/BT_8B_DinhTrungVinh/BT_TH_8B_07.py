# 8B.07 - Nhập và lưu thông tin người dùng
file = "data_dancu.txt"

cccd = input("Nhập mã CCCD: ")
ho = input("Nhập họ: ")
ten = input("Nhập tên: ")
tuoi = input("Nhập tuổi: ")

with open(file, "a", encoding="utf-8") as f:
    f.write(f"{cccd},{ho},{ten},{tuoi}\n")
    
print("Đã lưu thông tin vào", file)