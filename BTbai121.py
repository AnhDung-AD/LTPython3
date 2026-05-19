def phat_sinh_strobogrammatic(n, n_goc, la_mo_rong=False):

    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1", "8"] if not la_mo_rong else ["0", "1", "8", "2", "5"]
    danh_sach_con = phat_sinh_strobogrammatic(n - 2, n_goc, la_mo_rong)
    ket_qua = []
    for s in danh_sach_con:
        if n != n_goc:
            ket_qua.append("0" + s + "0")
        ket_qua.append("1" + s + "1")
        ket_qua.append("8" + s + "8")
        ket_qua.append("6" + s + "9")
        ket_qua.append("9" + s + "6")
        if la_mo_rong:
            ket_qua.append("2" + s + "2")
            ket_qua.append("5" + s + "5")

    return ket_qua
def main():
    while True:
        try:
            n = int(input("Nhập số nguyên n (2 <= n <= 10): "))
            if 2 <= n <= 10:
                break
            else:
                print("Vui lòng nhập đúng khoảng từ 2 đến 10!")
        except ValueError:
            print("Dữ liệu nhập vào phải là số nguyên!")

    print(f"\n--- ĐANG XỬ LÝ PHÁT SINH SỐ CÓ {n} CHỮ SỐ ---")

    # a
    ds_cau_a = phat_sinh_strobogrammatic(n, n, la_mo_rong=False)
    ds_cau_a.sort(key=int)

    # b
    ds_cau_b = phat_sinh_strobogrammatic(n, n, la_mo_rong=True)
    ds_cau_b.sort(key=int)
    
    print(f"a.- Tất cả các số strobogrammatic gồm {n} chữ số:")
    print(f"-> Tìm thấy tổng cộng: {len(ds_cau_a)} số.")
    if len(ds_cau_a) <= 50:
        print(f"-> Danh sách: {', '.join(ds_cau_a)}")
    else:
        print(f"-> 30 số đầu tiên: {', '.join(ds_cau_a[:30])} ...")
        print(f"-> 5 số cuối cùng: {', '.join(ds_cau_a[-5:])}")
        
    print("-" * 55)
    
    print(f"b.- Tất cả các số strobogrammatic mở rộng gồm {n} chữ số:")
    print(f"-> Tìm thấy tổng cộng: {len(ds_cau_b)} số.")
    if len(ds_cau_b) <= 50:
        print(f"-> Danh sách: {', '.join(ds_cau_b)}")
    else:
        print(f"-> 30 số đầu tiên: {', '.join(ds_cau_b[:30])} ...")
        print(f"-> 5 số cuối cùng: {', '.join(ds_cau_b[-5:])}")