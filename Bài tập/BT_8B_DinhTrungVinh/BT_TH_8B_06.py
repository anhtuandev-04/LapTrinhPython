# 8B.06 - Tính tổng các giá trị trong file
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
tenfile = f"data{a}_{b}.txt"

try:
    with open(tenfile, "r", encoding="utf-8") as f:
        tong = 0
        for line in f:
            tong += int(line.strip())
    with open(tenfile, "a", encoding="utf-8") as f:
        f.write(f"Tổng = {tong}\n")
    print("Đã tính tổng và ghi nối vào file", tenfile)
except FileNotFoundError:
    print("Ko tìm thấy file", tenfile)
