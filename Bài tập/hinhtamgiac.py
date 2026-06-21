import math

class HinhTamGiac:
    def __init__(self, a, b, c):
        self.canh_a = a
        self.canh_b = b
        self.canh_c = c

    def tinh_chu_vi(self):
        return self.canh_a + self.canh_b + self.canh_c

    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() / 2
        return math.sqrt(p * (p - self.canh_a) * (p - self.canh_b) * (p - self.canh_c))

    def loai_tam_giac(self):
        canh = sorted([self.canh_a, self.canh_b, self.canh_c])
        if canh[0] + canh[1] <= canh[2]:
            return "Không phải là tam giác"
        if canh[0] == canh[1] == canh[2]:
            return "Tam giác đều"
        if canh[0] == canh[1] or canh[1] == canh[2]:
            return "Tam giác cân"
        if canh[0]**2 + canh[1]**2 == canh[2]**2:
            return "Tam giác vuông"
        return "Tam giác thường"

try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    tam_giac_1 = HinhTamGiac(a, b, c)
    print("Chu vi:", tam_giac_1.tinh_chu_vi())
    print("Diện tích:", tam_giac_1.tinh_dien_tich())
    print("Loại tam giác:", tam_giac_1.loai_tam_giac())
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ.")
