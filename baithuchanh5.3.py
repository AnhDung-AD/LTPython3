# Nhập dữ liệu
dai  = input("Nhập chiều dài đáy hình chữ nhật (cm): ")
rong = input("Nhập chiều rộng đáy hình chữ nhật (cm): ")
cao  = input("Nhập chiều cao hình khối chữ nhật (cm): ")

print("dai = ",dai)
print("rong = ",rong)
print("cao = ",cao)

sole = input("Số lượng số lẻ cần hiển thị: ")
dinhdang = '{:.'+sole+'f}'

dai = float(dinhdang.format(eval(dai)))
rong= float(dinhdang.format(eval(rong)))
cao = float(dinhdang.format(eval(cao)))

print("dai = ",dai)
print("rong = ",rong)
print("cao = ",cao)

dientich = dai*rong
dientich = float(dinhdang.format(dientich))

thetich = dai*rong*cao
thetich = float(dinhdang.format(thetich))

print("Diện tích đáy hình chữ nhật = ",dientich,"cm\u00b2")
print("Thể tích hình khối) = ",thetich,"cm\u00b3")
