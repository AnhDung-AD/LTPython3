X = int(input("Nhap so tien X: "))

so_tien_goc = X
tong_so_to = 0
ds_menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]

print("So tien", so_tien_goc, "duoc doi thanh:")
for mg in ds_menh_gia:
    so_to = X // mg 
    X = X % mg
    tong_so_to = tong_so_to + so_to
    print("Loai", mg, "gom", so_to, "to")
print("TONG CONG CO", tong_so_to, "TO")