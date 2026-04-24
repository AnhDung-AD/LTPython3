import math

def tim_gcd_de_quy(a, b):
    if b == 0:
        return a
    return tim_gcd_de_quy(b, a % b)
x = int(input("4) Nhập số thứ nhất: "))
y = int(input("   Nhập số thứ hai: "))
print(f"==> Kết quả đệ quy (Euclid): {tim_gcd_de_quy(x, y)}")
print(f"==> Kiểm tra bằng thư viện math: {math.gcd(x, y)}")