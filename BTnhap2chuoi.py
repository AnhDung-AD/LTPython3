from collections import Counter

def giai_quyet_bai_tap_dictionary():
    s1 = input("Nhập chuỗi S1: ")
    s2 = input("Nhập chuỗi S2: ")

    dict1 = Counter(s1)
    dict2 = Counter(s2)
    set1 = set(s1)
    set2 = set(s2)

    print("\n" + "="*30)
    print("KẾT QUẢ PHÂN TÍCH CHUỖI")
    print("="*30)
    common_dict = dict1 & dict2
    print(f"a) Ký tự chung: {list(common_dict.keys())}")
    diff1 = list(set1 - set2)
    diff2 = list(set2 - set1)
    print(f"c) Có trong S1 nhưng không có trong S2: {diff1}")
    print(f"   Có trong S2 nhưng không có trong S1: {diff2}")
    total_diff = len(diff1) + len(diff2)
    print(f"b) Tổng số lượng ký tự khác biệt: {total_diff}")
    print("="*30)
