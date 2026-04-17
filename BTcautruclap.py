n = int(input("Nhap n: "))

temp = n

# ====== CAU 4 ======
chan = 0
le = 0
t = temp

while t > 0:
    if (t % 10) % 2 == 0:
        chan += 1
    else:
        le += 1
    t //= 10

print("So chu so chan:", chan)
print("So chu so le:", le)

# ====== CAU 5 ======
tong = 0
tich = 1
t = temp

while t > 0:
    tong += t % 10
    tich *= t % 10
    t //= 10

print("Tong =", tong)
print("Tich =", tich)

# ====== CAU 6 ======
maxx = 0
t = temp

while t > 0:
    if t % 10 > maxx:
        maxx = t % 10
    t //= 10

print("Chu so lon nhat:", maxx)

# ====== CAU 7 ======
t = temp
check = True

while t > 0:
    if t % 10 != 6 and t % 10 != 8:
        check = False
        break
    t //= 10

if check:
    print(temp, "la so may man")
else:
    print(temp, "khong phai so may man")