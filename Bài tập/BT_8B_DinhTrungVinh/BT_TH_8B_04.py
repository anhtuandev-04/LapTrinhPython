# 8B.04 - Ghi các số nguyên tố từ a đến b

def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return True
        return True
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

if 0<a<b:
    tenfile = f"data{a}_{b}.txt"
    with open(tenfile, "w", encoding="utf-8") as f:
        for i in range(a, b+1):
            if la_nguyen_to(i):
                f.write(str(i) + "\n")
    print("Đã ghi các số nguyên tố vào", tenfile)
else:
    print("Giá trị ko hợp lệ (0<a<b)")