#Bài 2B.02: Lấy dữ liệu từ cửa sổ dòng lệnh
#Trong python có module gọi là sys, đây là module có sẵn. Trong module này có hàm argv, Hàm này trả về một danh sách các đối số dòng lệnh được truyền cho tập lệnh Python. Tên của tập lệnh luôn là mục ở chỉ số 0 và phần còn lại của các đối số được lưu trữ tại các chỉ mục tiếp theo.
# Để lấy được đối số ta làm:
import sys
doi_so = sys.argv
dem = len(doi_so)
print(type(doi_so))
i = 0
for x in doi_so:
  print (f"tham số[{i}] = {x}, type({type(x)}")
  i += 1
print (f"tổng số tham số = {dem}")