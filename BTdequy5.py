import math

def fibonacci_de_quy(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)
print("-" * 20, "TÍNH SỐ FIBONACCI", "-" * 20)
n = int(input("5) Nhập vị trí n cần tính (n >= 0): "))

if n < 0:
    print("Lỗi: Vui lòng nhập số nguyên dương!")
else:
    ket_qua = fibonacci_de_quy(n)
    
    print(f"==> Kết quả đệ quy tại vị trí F{n}: {ket_qua}")
    print(f"Dãy Fibonacci từ F0 đến F{n}: ", end="")
    for i in range(n + 1):
        print(fibonacci_de_quy(i), end=" ")
    