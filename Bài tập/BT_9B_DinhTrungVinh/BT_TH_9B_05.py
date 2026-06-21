# 9B.05 - Đối tượng Điểm trong không gian 2D
import math

class Diem:
    def __init__(self, x=0, y=0, mau="đen"):
        self.x = x
        self.y = y
        self.mau = mau

    def hien_thi(self):
        print(f"Điểm({self.x}, {self.y}), màu: {self.mau}")

    def tinh_tien(self, dx, dy):
        self.x += dx
        self.y += dy

    def khoang_cach_O(self):
        return math.sqrt(self.x**2 + self.y**2)

    def khoang_cach(self, p_other):
        return math.sqrt((self.x - p_other.x)**2 + (self.y - p_other.y)**2)

print("\n--- NHẬP ĐIỂM 1 ---")
x1, y1 = map(float, input("Nhập tọa độ x y: ").split())
mau1 = input("Nhập màu: ")
p1 = Diem(x1, y1, mau1)

print("\n--- NHẬP ĐIỂM 2 ---")
x2, y2 = map(float, input("Nhập tọa độ x y: ").split())
mau2 = input("Nhập màu: ")
p2 = Diem(x2, y2, mau2)

print("\nThông tin 2 điểm:")
p1.hien_thi()
p2.hien_thi()

print("Khoảng cách từ điểm 1 đến O:", round(p1.khoang_cach_O(), 2))
print("Khoảng cách giữa 2 điểm:", round(p1.khoang_cach(p2), 2))

dx, dy = map(float, input("\nNhập độ tịnh tiến dx, dy cho điểm 1: ").split())
p1.tinh_tien(dx, dy)
print("Sau khi tịnh tiến:")
p1.hien_thi()
