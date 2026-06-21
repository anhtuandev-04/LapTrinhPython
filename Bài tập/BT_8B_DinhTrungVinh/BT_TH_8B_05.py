# 8B.05 - Ghi các số Fibonacci từ a đến b
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

def ds_fib(b):
    f = [0, 1]
    while f[-1] < b:
        f.append(f[-1] + f[-2])
    return f

if 0 < a < b:
    tenfile = f"data{a}_{b}.txt"
    with open(tenfile, "w", encoding="utf-8") as f:
        for n in ds_fib(b):
            if a <= n <= b:
                f.write(str(n) + "\n")
    print("Đã ghi các số Fib vào", tenfile)
else:
    print("Giá trị ko hợp lệ (0<a<b)")