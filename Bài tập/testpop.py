# my_list = [10, 20, 30]
# ptu_cuoi = my_list.pop()
# print("Phần tử cuối cùng đã bị loại bỏ:", ptu_cuoi)
# print("Danh sách sau khi loại bỏ phần tử cuối cùng:", my_list)

# set([1,1,2,3])
# print(set([1,1,2,3]))

# a={1,2,3} & {2,3,4}
# print(a)

# a = {"a":1, "b":2}.get("c",3)
# print(a)

# my_dict = {"a": 1, "b": 2}
# print("a" in my_dict)  # True
# print("c" in my_dict)  # False

# my_dict = {"VN": "Vietnam", "US": "USA", "UK": "England"}
# print(len(my_dict))  # Kết quả: 3 (vì có 3 cặp)

# a = int("99")
# print(a)

# a = bin(8)
# print(a)  # Kết quả: '0b1010' (biểu diễn nhị phân của số 10)

# Tạo bài toán chuyển số thập phân sang nhị phân thủ công, ko sử dụng hàm bin()
# def decimal_to_binary(n):
#     if n == 0:
#         return "0"
#     binary_digits = []
#     while n > 0:
#         remainder = n % 2
#         binary_digits.append(str(remainder))
#         n = n // 2
#     binary_digits.reverse()
#     return ''.join(binary_digits)
# number = 8
# binary_representation = decimal_to_binary(number)
# print("0b" + binary_representation)  # Kết quả: '1000' (biểu diễn nhị phân của số 8)

# a=int(5.9)
# print(a)

#a= "abc".upper()
# print("apple,banana,cherry".split(","))
# print("5"*3)
# a="5"*3
# print(type(a))

# a="""This is a comment

# spanning multiple lines.""" 
# print(a)

# my_list = [1, 2, 3]
# for so in my_list:
#     print(so) # In ra 1, 2, 3 lần lượt

# dem = 0
# while dem < 3: # Điều kiện: dem < 3
#     print(dem)
#     dem = dem + 1 # Phải có câu lệnh làm thay đổi điều kiện!
# # Kết quả: 0, 1, 2
# for i in range(5):
#     print(i)

# for i in range(2,10,3): 
#     print(i)

# while True:
#     print("Hello, World!")

# danh_sach_so = [1, 5, 8, 12, 15]
# so_can_tim = 10
# da_tim_thay = False

# for so in danh_sach_so:
#     if so == so_can_tim:
#         print(f"✅ Đã tìm thấy số {so_can_tim}!")
#         da_tim_thay = True
#         break  # Ngắt vòng lặp, bỏ qua khối else

# else:
#     # Khối này chỉ chạy nếu vòng lặp FOR kết thúc bình thường (không gặp lệnh 'break')
#     print(f"❌ Đã duyệt hết danh sách, không tìm thấy số {so_can_tim}.")

# for i in range(5):
#     if i == 3:
#         break
# print(i)

# for i in "Python":
#     print(i)

# a=sum(range(4))
# print(a)

# danh_sach = ["apple", "banana", "cherry"]

# # Duyệt bằng CHỈ SỐ
# print("--- Duyệt bằng Chỉ số ---")
# for i in range(len(danh_sach)):
#     print(f"Chỉ số {i}: {danh_sach[i]}")

# # Duyệt TRỰC TIẾP (thường được ưu tiên hơn nếu không cần chỉ số)
# print("\n--- Duyệt Trực tiếp ---")
# for item in danh_sach:
#     print(f"Phần tử: {item}")

# for i in range(2): 
#     for j in range(2): 
#         print(i,j)

# danh_sach = ["cam", "quýt", "xoài"]
# for index, item in enumerate(danh_sach):
#     print(f"Vị trí {index} là: {item}")
# # Kết quả: Vị trí 0 là: cam, Vị trí 1 là: quýt, ...

# a=0%2 # chia lấy dư
# print(a)

# for x in range(5): 
#     if x%2==0:
#         print(x)

# while False:
#     print("Hello, World!")  

# for i in range(10): 
#     if i%3==0: 
#         continue 
#     print(i) 

# for i in range(1,4):
#     print(i*"#")

# sum([x for x in range(1,6)])
# print(sum([x for x in range(1,6)]))

# print(sum([1,2,3,4,5]))

# i=0
# while i<3: 
#     print(i)
#     i+=1

# print(any(["", "", ""])) 

# def show(x): print(x)
# y = show
# y("Hello")














