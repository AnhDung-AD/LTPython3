import math

def luy_thua_de_quy(a, b):
    if b == 0:
        return 1
    return a * luy_thua_de_quy(a, b - 1)
a = int(input("3) Nhập cơ số a: "))
b = int(input("   Nhập số mũ b: "))
print(f"==> Kết quả đệ quy: {luy_thua_de_quy(a, b)}")
print(f"==> Kiểm tra bằng thư viện math: {math.pow(a, b)}")