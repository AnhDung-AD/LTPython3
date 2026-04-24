import math

def giai_thua_de_quy(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_de_quy(n - 1)
n = int(input("2) Nhập số tính giai thừa: "))
print(f"==> Kết quả đệ quy: {giai_thua_de_quy(n)}")
print(f"==> Kiểm tra bằng thư viện math: {math.factorial(n)}")