import math

class HinhTron:
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def tinh_chu_vi(self):
        return 2 * math.pi * self.ban_kinh

    def tinh_dien_tich(self):
        return math.pi * (self.ban_kinh ** 2)

try:
    r = float(input("Nhập bán kính: "))
    hinh_tron_1 = HinhTron(r)
    print("Chu vi:", hinh_tron_1.tinh_chu_vi())
    print("Diện tích:", hinh_tron_1.tinh_dien_tich())
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ.")
