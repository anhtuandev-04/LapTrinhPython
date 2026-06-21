# Bài 8B.01 Đọc dữ liệu từ tập tin Sinhvien.txt
# Viết chương trình đọc dữ liệu từ tập tin SinhVien.txt và
#hiển thị ra màn hình Danh sách sinh viên đã được sắp xếp theo Lớp, 
#Mã số sinh viên.
# Khởi tạo một lớp (class) SinhVien để lưu trữ thông tin
class SinhVien:
    def __init__(self, mssv, ho_lot, ten, lop, que_quan):
        self.mssv = mssv.strip()
        self.ho_lot = ho_lot.strip()
        self.ten = ten.strip()
        self.lop = lop.strip()
        self.que_quan = que_quan.strip()

    def __repr__(self):
        # hiển thị khi in ra
        return f"| {self.lop:<10} | {self.mssv:<10} | {self.ho_lot} {self.ten:<15} | {self.que_quan:<15} |"
#Bước 1: Đọc tệp
def doc_du_lieu_va_sap_xep(ten_tap_tin="Sinhvien.txt"):
    """Đọc dữ liệu từ tập tin, lưu vào danh sách và sắp xếp."""
    danh_sach_sinh_vien = []
    
    try:
        # Mở tệp ở chế độ đọc r
        with open(ten_tap_tin, 'r', encoding='utf-8') as f:
            for line in f:
                # Xóa khoảng trắng thừa ở đầu/cuối dòng và tách chuỗi bằng dấu phẩy
                parts = [p.strip() for p in line.strip().split(',')]
                
                # Ktra số lượng phần tử
                if len(parts) == 4:
                    mssv, ho_ten, lop, que_quan = parts
                    ten = ho_ten.split()[-1]
                    ho_lot = " ".join(ho_ten.split()[:-1])
                    
                    sv = SinhVien(mssv, ho_lot, ten, lop, que_quan)
                    danh_sach_sinh_vien.append(sv)
                else:
                    print(f"Bỏ qua dòng không đúng định dạng: {line.strip()}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tập tin '{ten_tap_tin}'. Vui lòng tạo tập tin.")
        return

    danh_sach_sinh_vien.sort(key=lambda sv: (sv.lop, sv.mssv))

    print("\n" + "="*70)
    print("Danh sách Sinh viên đã được sắp xếp (theo Lớp, sau đó MSSV):")
    print("="*70)
    print("| Lớp        | MSSV       | Họ và Tên               | Quê quán        |")
    print("-" * 70)
    for sv in danh_sach_sinh_vien:
        print(sv)
    print("-" * 70)

if __name__ == "__main__":
    doc_du_lieu_va_sap_xep()
