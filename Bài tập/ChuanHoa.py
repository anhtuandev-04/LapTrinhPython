import sys

def main():
    if len(sys.argv) > 1:
        ho_ten = ' '.join(sys.argv[1:])
    else:
        ho_ten = input("Nhap ho ten: ")

    ho_ten = ho_ten.strip()

    danh_sach_tu = ho_ten.split()

    danh_sach_tu_chuan = []
    for tu in danh_sach_tu:
        tu_chuan = tu.capitalize()
        danh_sach_tu_chuan.append(tu_chuan)

    ho_ten_chuan = ' '.join(danh_sach_tu_chuan)

    print("Ho ten da chuan hoa:", ho_ten_chuan)

if __name__ == "__main__":
    main()