a = int(input("Nhap so tien hang can thanh toan (a): "))
b = int(input("Nhap so tien khach hang thuc tra (b): "))
if a > b:
    print("So tien khach hang con thieu la:", a - b)
    print("Ket thuc chuong trinh.")

elif a == b:
    print("Cam on khach hang. Hen gap lai")

else:
    X = b - a  
    print("\nSo tien thua can thoi lai la:", X)
    print("Chi tiet cac loai tien thoi:")
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    tong_so_to = 0
    tong_so_loai = 0
    for mg in menh_gia:
        so_to = X // mg   
        X = X % mg       
        if so_to > 0:
            print("Loai", mg, "gom", so_to, "to")
            tong_so_to = tong_so_to + so_to
            tong_so_loai = tong_so_loai + 1           
    print("TONG CONG CO", tong_so_to, "TO")
    print("Tong so loai =", tong_so_loai)
    input("\nNhan phim Enter de tiep tuc...")
    print("Cam on khach hang. Hen gap lai")