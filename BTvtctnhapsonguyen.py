import math

def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def kiem_tra_tang_dan(lst):
    # Trả về True nếu list rỗng hoặc chỉ có 1 phần tử
    if len(lst) < 2: return True 
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]: return False
    return True

danh_sach = []
while True:
    try:
        val = int(input("Nhập số nguyên: "))
        danh_sach.append(val)
    except ValueError:
        print("Lỗi: Chỉ được nhập số nguyên!")
        continue

    confirm = input("Tiếp tục nhập? (Y/N): ").strip().lower()
    if confirm == 'n':
        break

print("\n" + "="*40)
print("BÁO CÁO KẾT QUẢ")
print("="*40)
# a) Lọc số nguyên tố
primes = [x for x in danh_sach if la_so_nguyen_to(x)]
print(f"a. Số nguyên tố trong list: {primes}")
# b.1) Trung bình cộng số dương
positives = [x for x in danh_sach if x > 0]
tbc_duong = sum(positives)/len(positives) if positives else 0
print(f"b.1. TBC số dương: {round(tbc_duong, 2)}")
# b.2) Trung bình cộng số âm
negatives = [x for x in danh_sach if x < 0]
tbc_am = sum(negatives)/len(negatives) if negatives else 0
print(f"b.2. TBC số âm: {round(tbc_am, 2)}")
# c) Max - Min
if danh_sach:
    print(f"c. Max: {max(danh_sach)} | Min: {min(danh_sach)}")
# d) Kiểm tra sắp xếp
status = "Đã sắp xếp tăng dần" if kiem_tra_tang_dan(danh_sach) else "Chưa sắp xếp tăng dần"
print(f"d. Trạng thái list: {status}")
print("="*40)
