# Bài 9B.07 Chương trình Quản lý học viên trung tâm Anh ngữ
class MonHoc:
    def __init__(self, ma, ten, sotiet):
        self.ma = ma
        self.ten = ten
        self.sotiet = sotiet

    def __str__(self):
        return f"{self.ma} - {self.ten} ({self.sotiet} tiết)"

class HocVien:
    def __init__(self, cccd, ten, namsinh):
        self.cccd = cccd
        self.ten = ten
        self.namsinh = namsinh
        self.ds_mon = []

    def them_mon(self):
        ma = input("Nhập mã môn: ")
        ten = input("Nhập tên môn: ")
        sotiet = int(input("Nhập số tiết: "))
        self.ds_mon.append(MonHoc(ma, ten, sotiet))

    def hien_thi(self):
        print(f"\nHọc viên: {self.ten} ({self.cccd}) - Năm sinh: {self.namsinh}")
        if self.ds_mon:
            print("Danh sách môn học:")
            for mh in self.ds_mon:
                print("   ", mh)
        else:
            print("Chưa đăng ký môn học nào!")

class QuanLyHocVien:
    def __init__(self):
        self.ds = []

    def nhap(self):
        cccd = input("Nhập CCCD: ")
        ten = input("Nhập tên học viên: ")
        namsinh = int(input("Nhập năm sinh: "))
        hv = HocVien(cccd, ten, namsinh)
        n = int(input("Số môn học đăng ký: "))
        for _ in range(n):
            hv.them_mon()
        self.ds.append(hv)

    def hien_thi_tat_ca(self):
        for hv in self.ds:
            hv.hien_thi()

    def hien_thi_hv_2mon(self):
        print("\nHọc viên đăng ký ít nhất 2 môn:")
        for hv in self.ds:
            if len(hv.ds_mon) >= 2:
                hv.hien_thi()

    def ghi_file(self, tenfile="DSHV.txt"):
        with open(tenfile, "w", encoding="utf-8") as f:
            for hv in self.ds:
                line = f"{hv.cccd}|{hv.ten}|{hv.namsinh}"
                for mh in hv.ds_mon:
                    line += f"|{mh.ma},{mh.ten},{mh.sotiet}"
                f.write(line + "\n")
        print("Đã ghi dữ liệu vào", tenfile)

    def doc_file(self, tenfile="DSHV.txt"):
        self.ds.clear()
        try:
            with open(tenfile, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("|")
                    cccd, ten, namsinh = parts[:3]
                    hv = HocVien(cccd, ten, int(namsinh))
                    for mh_str in parts[3:]:
                        ma, tenmh, sotiet = mh_str.split(",")
                        hv.ds_mon.append(MonHoc(ma, tenmh, int(sotiet)))
                    self.ds.append(hv)
            print("Đọc dữ liệu thành công!")
        except FileNotFoundError:
            print("Chưa có file dữ liệu!")

ql = QuanLyHocVien()
while True:
    print("\n--- MENU QUẢN LÝ HỌC VIÊN ---")
    print("1. Nhập học viên")
    print("2. Hiển thị tất cả học viên")
    print("3. Hiển thị học viên có ≥ 2 môn")
    print("4. Ghi file")
    print("5. Đọc file")
    print("0. Thoát")
    chon = input("Chọn: ")
    if chon == "1": ql.nhap()
    elif chon == "2": ql.hien_thi_tat_ca()
    elif chon == "3": ql.hien_thi_hv_2mon()
    elif chon == "4": ql.ghi_file()
    elif chon == "5": ql.doc_file()
    elif chon == "0": break
