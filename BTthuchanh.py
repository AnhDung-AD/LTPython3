import math

print("--- KẾT QUẢ THỰC HIỆN CÁC CÂU HỎI ---")
#(A)
tri_tuyet_doi = lambda n: abs(n)
print(f"a) Trị tuyệt đối của -10 là: {tri_tuyet_doi(-10)}")

#(B)
cong_15 = lambda n: n + 15
print(f"b) Lấy 20 cộng thêm 15 kết quả: {cong_15(20)}")

#(C)
tich_hai_so = lambda x, y: x * y
print(f"c) Tích của 6 và 7 là: {tich_hai_so(6, 7)}")
#(D)
la_boi_so = lambda n: n % 13 == 0 or n % 19 == 0
print(f"d) Số 38 có là bội của 13 hoặc 19? {la_boi_so(38)}")
dien_tich_tron = lambda r: math.pi * (r**2)
#(E)
print(f"e) Diện tích hình tròn bán kính r=5: {dien_tich_tron(5):.2f}")
#(F)
chu_vi_hcn = lambda d, r: (d + r) * 2
print(f"f) Chu vi hình chữ nhật (dài 10, rộng 4): {chu_vi_hcn(10, 4)}")
#(G)
la_so_cp = lambda n: n >= 0 and math.isqrt(n)**2 == n
print(f"g) Số 16 có là số chính phương? {la_so_cp(16)}")

#(H)
la_so_nt = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
print(f"h) Số 17 có là số nguyên tố? {la_so_nt(17)}")
#(I)
phan_loai_tg = lambda a, b, c: (
    "Tam giác Đều" if a == b == c else
    "Tam giác Vuông" if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) else
    "Tam giác Cân" if (a == b or b == c or a == c) else
    "Tam giác Thường"
) if (a + b > c and a + c > b and b + c > a) else "Không phải tam giác"

print(f"i) Bộ ba (3, 4, 5) tạo thành: {phan_loai_tg(3, 4, 5)}")
print(f"i) Bộ ba (2, 2, 2) tạo thành: {phan_loai_tg(2, 2, 2)}")
print(f"i) Bộ ba (1, 2, 10) tạo thành: {phan_loai_tg(1, 2, 10)}")

