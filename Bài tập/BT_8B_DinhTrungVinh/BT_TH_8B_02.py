# 8B.02 - Quản lý sinh viên
import os

filename = "SinhVien_02.txt"

def tai_danh_sach():
    ds = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    parts = line.split(',')
                    if len(parts) == 5: 
                        ds.append(parts)
    return ds

def luu_danh_sach(ds):
    with open(filename, "w", encoding="utf-8") as f:
        for sv in ds:
            f.write(','.join(sv) + "\n")

def nhap_sv():
    ma = input("Mã SV: ")
    holot = input("Họ và chữ lót: ")
    ten = input("Tên: ")
    lop = input("Lớp: ")
    que = input("Quê quán: ")
    return [ma, holot, ten, lop, que]

def hien_thi(ds):
    tieu_de = ["Mã SV", "Họ và chữ lót", "Tên", "Lớp", "Quê quán"]
    max_lens = [len(td) for td in tieu_de] 
    
    for sv in ds:
        for i, item in enumerate(sv):
            max_lens[i] = max(max_lens[i], len(item))
    max_lens = [length + 3 for length in max_lens]
    header_line = ""
    for i, td in enumerate(tieu_de):
        header_line += td.ljust(max_lens[i])
    print(header_line)
    print("-" * sum(max_lens)) 

    for sv in ds:
        data_line = ""
        for i, item in enumerate(sv):
            data_line += item.ljust(max_lens[i])
        print(data_line)

def tim_theo_lop(ds, lop):
    return [sv for sv in ds if sv[3] == lop]

def tim_theo_ten(ds, ten):
    return [sv for sv in ds if sv[2].lower() == ten.lower()]

def luu_theo_lop(ds):
    lop_dict = {}
    for sv in ds:
        lop = sv[3]
        if lop not in lop_dict:
            lop_dict[lop] = []
        lop_dict[lop].append(sv)
    for lop, dslop in lop_dict.items():
        tenfile = f"Sinhvien_{lop}.txt"
        with open(tenfile, "w", encoding="utf-8") as f:
            for sv in dslop:
                f.write(','.join(sv) + "\n")

ds = tai_danh_sach()
while True:
    print("\n--- MENU ---")
    print("1. Xem danh sách")
    print("2. Nhập sinh viên mới")
    print("3. Sửa thông tin sinh viên")
    print("4. Lưu danh sách")
    print("5. Tìm theo lớp")
    print("6. Tìm theo tên")
    print("7. Lưu ra file theo lớp")
    print("0. Thoát")
    chon = input("Chọn: ")

    if chon == "1":
        hien_thi(ds)
    elif chon == "2":
        ds.append(nhap_sv())
    elif chon == "3":
        ma = input("Nhập mã SV cần sửa: ")
        tim_thay = False
        for sv in ds:
            if sv[0] == ma:
                print("Nhập thông tin mới:")
                moi = nhap_sv()
                sv[:] = moi
                tim_thay = True
                break
        if not tim_thay:
             print("Không tìm thấy Mã SV.")
    elif chon == "4":
        luu_danh_sach(ds)
        print("Đã lưu vào file.")
    elif chon == "5":
        lop = input("Nhập lớp: ")
        dskq = tim_theo_lop(ds, lop)
        if dskq:
            hien_thi(dskq)
        else:
            print(f"Không tìm thấy sinh viên lớp {lop}.")
    elif chon == "6":
        ten = input("Nhập tên: ")
        dskq = tim_theo_ten(ds, ten)
        if dskq:
            hien_thi(dskq)
        else:
            print(f"Không tìm thấy sinh viên tên {ten}.")
    elif chon == "7":
        luu_theo_lop(ds)
        print("Đã lưu file theo lớp.")
    elif chon == "0":
        break
    else:
        print("Lựa chọn không hợp lệ!")