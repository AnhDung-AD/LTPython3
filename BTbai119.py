import math

def la_so_nguyen_to(n):
    """Kiểm tra một số có phải là số nguyên tố hay không."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

STRO_MAP = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

def la_strobogrammatic(n):
    """Kiểm tra số strobogrammatic chuẩn."""
    s = str(n)
    left, right = 0, len(s) - 1
    while left <= right:
        if s[left] not in STRO_MAP or s[right] not in STRO_MAP:
            return False
        if STRO_MAP[s[left]] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def xoay_so_180_do(n):
    """
    Xoay số 180 độ từ phải qua trái.
    Trả về số nguyên sau khi xoay. Nếu chứa ký tự không hợp lệ, trả về None.
    """
    s = str(n)
    s_xoay = ""
    for chu_so in reversed(s):
        if chu_so not in STRO_MAP:
            return None
        s_xoay += STRO_MAP[chu_so]
    return int(s_xoay)
STRO_EXT_MAP = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6', '2': '2', '5': '5'}

def la_strobogrammatic_mo_rong(n):
    """Kiểm tra số strobogrammatic mở rộng."""
    s = str(n)
    left, right = 0, len(s) - 1
    while left <= right:
        if s[left] not in STRO_EXT_MAP or s[right] not in STRO_EXT_MAP:
            return False
        if STRO_EXT_MAP[s[left]] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def main():
    LIMIT = 1000000
    ket_qua_a = []
    ket_qua_b = []
    ket_qua_c = []
    ket_qua_d = []
    ket_qua_e = []

    for i in range(1, LIMIT):
        check_stro = la_strobogrammatic(i)
        check_stro_ext = la_strobogrammatic_mo_rong(i)
        check_snt = la_so_nguyen_to(i)
        
        # a 
        if check_stro:
            ket_qua_a.append(i)
        # b
            if check_snt:
                ket_qua_b.append(i)
                
        # c
        if check_stro_ext:
            ket_qua_c.append(i)
        # d
            if check_snt:
                ket_qua_d.append(i)             
        # e
        if not check_stro and not check_snt:
            so_sau_xoay = xoay_so_180_do(i)
            if so_sau_xoay is not None and la_so_nguyen_to(so_sau_xoay):
                ket_qua_e.append(i)
    
    print("a.- Các số strobogrammatic nhỏ hơn 1 triệu:")
    print(f"-> Tìm thấy {len(ket_qua_a)} số. Ví dụ 20 số đầu: {ket_qua_a[:20]}...\n")
    
    print("b.- Các số nguyên tố strobogrammatic nhỏ hơn 1 triệu:")
    print(f"-> Kết quả: {ket_qua_b}\n")
    
    print("c.- Các số strobogrammatic mở rộng nhỏ hơn 1 triệu:")
    print(f"-> Tìm thấy {len(ket_qua_c)} số. Ví dụ 20 số đầu: {ket_qua_c[:20]}...\n")
    
    print("d.- Các số nguyên tố strobogrammatic mở rộng nhỏ hơn 1 triệu:")
    print(f"-> Kết quả: {ket_qua_d}\n")
    
    print("e.- Các số nhỏ hơn 1 triệu thỏa mãn điều kiện câu e:")
    print(f"-> Tìm thấy {len(ket_qua_e)} số. Ví dụ 20 số đầu: {ket_qua_e[:20]}...")
