class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)
        
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

try:
    dai = float(input("Nhập chiều dài: "))
    rong = float(input("Nhập chiều rộng: "))
    hinh_1 = HinhChuNhat(dai, rong)
    print("Chu vi:", hinh_1.tinh_chu_vi())
    print("Diện tích:", hinh_1.tinh_dien_tich())
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ.")
