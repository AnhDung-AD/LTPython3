def tong_chu_so(n):
    if n == 0:
        return 0
    return (n % 10) + tong_chu_so(n // 10)
n = int(input("Nhập số nguyên n: "))
print(f"==> Tổng các chữ số của {n} là: {tong_chu_so(n)}")