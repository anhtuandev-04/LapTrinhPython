# 9B.04 - Quản lý Môn học

class MonHoc:
    def __init__(self, ma_mon, ten_mon, so_tin_chi):
        self.ma_mon = ma_mon
        self.ten_mon = ten_mon
        self.so_tin_chi = so_tin_chi

    def hien_thi(self):
        print(f"{self.ma_mon:<10} | {self.ten_mon:<25} | {self.so_tin_chi:<5}")

ds_mon = []

def them_mon():
    ma = input("Nhập mã môn: ")
    ten = input("Nhập tên môn: ")
    tin = int(input("Nhập số tín chỉ: "))
    ds_mon.append(MonHoc(ma, ten, tin))
    print("Đã thêm môn học!")

def xoa_mon():
    ma_xoa = input("Nhập mã môn cần xóa: ")
    for mh in ds_mon:
        if mh.ma_mon == ma_xoa:
            ds_mon.remove(mh)
            print("Đã xóa môn", ma_xoa)
            return
    print("Không tìm thấy môn cần xóa.")

def hien_thi_danh_sach():
    if not ds_mon:
        print("Danh sách rỗng.")
    else:
        print("MÃ MÔN   | TÊN MÔN                   | TÍN CHỈ")
        print("-" * 45)
        for mh in ds_mon:
            mh.hien_thi()

def tim_kiem():
    print("1. Theo mã môn")
    print("2. Theo tên môn")
    print("3. Theo số tín chỉ")
    chon = input("Chọn cách tìm: ")
    if chon == "1":
        ma = input("Nhập mã môn: ")
        kq = [mh for mh in ds_mon if mh.ma_mon == ma]
    elif chon == "2":
        ten = input("Nhập tên môn: ").lower()
        kq = [mh for mh in ds_mon if ten in mh.ten_mon.lower()]
    elif chon == "3":
        tin = int(input("Nhập số tín chỉ: "))
        kq = [mh for mh in ds_mon if mh.so_tin_chi == tin]
    else:
        print("Lựa chọn không hợp lệ.")
        return

    if kq:
        print("Kết quả tìm thấy:")
        for mh in kq:
            mh.hien_thi()
    else:
        print("Không tìm thấy kết quả phù hợp.")

def ghi_file():
    with open("monhoc.txt", "w", encoding="utf-8") as f:
        for mh in ds_mon:
            f.write(f"{mh.ma_mon},{mh.ten_mon},{mh.so_tin_chi}\n")
    print("Đã ghi dữ liệu ra monhoc.txt")

def doc_file():
    try:
        with open("monhoc.txt", "r", encoding="utf-8") as f:
            ds_mon.clear()
            for line in f:
                ma, ten, tin = line.strip().split(",")
                ds_mon.append(MonHoc(ma, ten, int(tin)))
        print("Đã đọc dữ liệu từ monhoc.txt")
    except FileNotFoundError:
        print("Chưa có file monhoc.txt")

while True:
    print("\n--- QUẢN LÝ MÔN HỌC ---")
    print("1. Thêm môn học")
    print("2. Xóa môn học")
    print("3. Hiển thị danh sách")
    print("4. Tìm kiếm")
    print("5. Ghi ra file")
    print("6. Đọc từ file")
    print("0. Thoát")
    chon = input("Chọn chức năng: ")

    if chon == "1": them_mon()
    elif chon == "2": xoa_mon()
    elif chon == "3": hien_thi_danh_sach()
    elif chon == "4": tim_kiem()
    elif chon == "5": ghi_file()
    elif chon == "6": doc_file()
    elif chon == "0":
        print("Kết thúc chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")
