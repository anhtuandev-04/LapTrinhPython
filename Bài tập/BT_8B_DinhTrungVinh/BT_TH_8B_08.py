# 8B.08 - Quản lý tiêu thụ điện
from collections import defaultdict

def nhap_thong_tin():
    while True:
        phong = input("Số hiệu phòng: ").strip()
        toa = input("Số hiệu tòa nhà: ").strip()
        chu = input("Tên chủ hộ: ").strip()
        try:
            sokw = float(input("Số kWh tiêu thụ: "))
        except:
            print("Vui lòng nhập số!")
            continue
        if phong and toa and chu and sokw >= 0:
            return [toa, phong, chu, sokw]
        else:
            print("Dữ liệu không hợp lệ, nhập lại!")

def tinh_tien_dien(kw):
    bac = [50, 50, 100, 100, 100]
    gia = [1678, 1734, 2014, 2536, 2834, 2927]
    tien = 0
    for i in range(6):
        if i < 5:
            dung = min(kw, bac[i])
            tien += dung * gia[i]
            kw -= dung
            if kw <= 0:
                break
        else:
            tien += kw * gia[i]
    return tien

def hien_thi_bang(ds):
    tieu_de = ["Toà", "Phòng", "Chủ hộ", "Điện tiêu thụ", "Tiền điện", "VAT", "Tổng phải trả"]
    
    ds_hien_thi = []
    for toa, phong, chu, kw in ds:
        tien = tinh_tien_dien(kw)
        vat = tien * 0.1
        tong = tien + vat
        
        kw_str = f"{kw:g}"
        tien_str = f"{tien:,.0f}"
        vat_str = f"{vat:,.0f}"
        tong_str = f"{tong:,.0f}"
        
        ds_hien_thi.append([toa, phong, chu, kw_str, tien_str, vat_str, tong_str])

    max_lens = [len(td) for td in tieu_de]
    
    for row in ds_hien_thi:
        for i, item in enumerate(row):
            max_lens[i] = max(max_lens[i], len(item))

    khoang_cach = 3
    max_lens = [length + khoang_cach for length in max_lens]

    header_line = ""
    for i, td in enumerate(tieu_de):
        header_line += td.ljust(max_lens[i])
    print(header_line)
    print("-" * sum(max_lens)) 

    for row in ds_hien_thi:
        data_line = ""
        for i, item in enumerate(row):
            data_line += item.ljust(max_lens[i])
        print(data_line)

ds = []
try:
    n = int(input("Nhập số hộ dân: "))
except ValueError:
    print("Vui lòng nhập một số nguyên.")
    n = 0
    
for i in range(n):
    print(f"--- Hộ {i+1} ---")
    ds.append(nhap_thong_tin())

if ds:
    print("\n--- BẢNG THỐNG KÊ TIÊU THỤ ĐIỆN ---")
    hien_thi_bang(ds)
else:
    print("Không có dữ liệu để hiển thị.")

ds_toa = defaultdict(list)
for toa, phong, chu, kw in ds:
    ds_toa[toa].append((phong, chu, kw))

if ds_toa:
    for toa, danh_sach in ds_toa.items():
        tenfile = f"{toa}.txt"
        with open(tenfile, "a", encoding="utf-8") as f:
            for phong, chu, kw in danh_sach:
                tien = tinh_tien_dien(kw)
                vat = tien * 0.1
                tong = tien + vat
                f.write(f"{toa},{phong},{chu},{kw},{tien},{vat},{tong}\n")
    print("\nĐã lưu thông tin theo từng tòa.")