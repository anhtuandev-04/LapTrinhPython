# Bài 9B.06 Đối tượng Toán học
class ToanHoc:
    def __init__(self, *nso):
        self.ds = list(nso)

    def tinh_tong(self):
        return sum(self.ds)

    def tinh_trung_binh(self):
        return self.tinh_tong() / len(self.ds) if self.ds else 0

    def tinh_max(self):
        return max(self.ds)

    def tinh_min(self):
        return min(self.ds)

    def hien_thi(self):
        print("Danh sách số:", self.ds)

n = int(input("Nhập số lượng phần tử: "))
ds = []
for i in range(n):
    ds.append(float(input(f"Số thứ {i+1}: ")))

th = ToanHoc(*ds)
th.hien_thi()
print("Tổng =", th.tinh_tong())
print("Trung bình =", round(th.tinh_trung_binh(), 2))
print("Số lớn nhất =", th.tinh_max())
print("Số nhỏ nhất =", th.tinh_min())
