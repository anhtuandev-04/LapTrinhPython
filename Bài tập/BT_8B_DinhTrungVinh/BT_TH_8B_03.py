# 8B.03 - Ghi các số nguyên từ a đến b vào file

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

if 0 < a < b:
    tenfile = f"data{a}_{b}.txt"
    with open(tenfile, "w", encoding="utf-8") as f:
        for i in range(a, b+1):
            f.write(str(i) + "\n")
    print("Đã ghi vào", tenfile)
else:
    print("Giá trị không hợp lệ (0 < a < b).")
