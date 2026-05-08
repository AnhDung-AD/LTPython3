import os

def compress(input_file: str, output_file: str) -> None:
    """
    Đọc file văn bản gốc, nén lại và ghi ra output_file.

    Tham số:
        input_file  : đường dẫn file văn bản gốc (.txt)
        output_file : đường dẫn file nén đầu ra  (.cmp)
    """
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    vocab = []
    word_to_idx = {}

    for line in lines:
        for word in line.split():         
            if word not in word_to_idx:
                word_to_idx[word] = len(vocab)
                vocab.append(word)
    encoded_lines = []
    for line in lines:
        words = line.split()
        if words:
            encoded_lines.append(" ".join(str(word_to_idx[w]) for w in words))
        else:
            encoded_lines.append("")       
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"{len(vocab)}\n")
        for word in vocab:
            f.write(word + "\n")
        f.write(f"{len(encoded_lines)}\n")
        for enc in encoded_lines:
            f.write(enc + "\n")
    orig_size = os.path.getsize(input_file)
    comp_size = os.path.getsize(output_file)
    saved     = orig_size - comp_size
    ratio     = (saved / orig_size * 100) if orig_size > 0 else 0.0
    print("=" * 52)
    print("  KẾT QUẢ NÉN FILE")
    print("=" * 52)
    print(f"  File gốc            : {input_file}")
    print(f"  File nén            : {output_file}")
    print(f"  Kích thước gốc      : {orig_size:>8,} bytes")
    print(f"  Kích thước sau nén  : {comp_size:>8,} bytes")
    print(f"  Thay đổi            : {saved:>+8,} bytes  ({ratio:+.1f}%)")
    print(f"  Số từ duy nhất      : {len(vocab)}")
    print(f"  Số dòng văn bản     : {len(lines)}")
    print("=" * 52)
def decompress(compressed_file: str, output_file: str) -> None:
    """
    Đọc file nén và khôi phục lại văn bản ban đầu.

    Tham số:
        compressed_file : đường dẫn file nén (.cmp)
        output_file     : đường dẫn file văn bản khôi phục (.txt)
    """

    with open(compressed_file, "r", encoding="utf-8") as f:
        vocab_size = int(f.readline().strip())
        vocab = [f.readline().rstrip("\n") for _ in range(vocab_size)]
        num_lines = int(f.readline().strip())
        restored_lines = []

        for _ in range(num_lines):
            enc_line = f.readline().rstrip("\n")
            if enc_line.strip() == "":
                restored_lines.append("")
            else:
                words = [vocab[int(idx)] for idx in enc_line.split()]
                restored_lines.append(" ".join(words))
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(restored_lines) + "\n")
    print("=" * 52)
    print("  KẾT QUẢ GIẢI NÉN FILE")
    print("=" * 52)
    print(f"  File nén            : {compressed_file}")
    print(f"  File khôi phục      : {output_file}")
    print(f"  Số từ trong từ điển : {vocab_size}")
    print(f"  Số dòng khôi phục   : {num_lines}")
    print("=" * 52)
def verify(original_file: str, restored_file: str) -> bool:
    """
    So sánh nội dung file gốc và file khôi phục.
    Trả về True nếu khớp nhau hoàn toàn.
    """
    with open(original_file,  "r", encoding="utf-8") as f:
        original = f.read()
    with open(restored_file, "r", encoding="utf-8") as f:
        restored = f.read()
    if original == restored:
        print("Kiểm tra: File khôi phục KHỚP HOÀN TOÀN với file gốc!")
        return True
    else:
        print("Kiểm tra: File khôi phục KHÔNG khớp với file gốc!")
        orig_lines = original.splitlines()
        rest_lines = restored.splitlines()
        for i, (a, b) in enumerate(zip(orig_lines, rest_lines), 1):
            if a != b:
                print(f"   → Dòng {i} khác nhau:")
                print(f"     Gốc      : {repr(a)}")
                print(f"     Khôi phục: {repr(b)}")
        return False
if __name__ == "__main__":
    noi_dung_mau = """\
Thuyền và biển
Chỉ có thuyền mới hiểu
Biển mênh mông nhường nào
Chỉ có biển mới biết
Thuyền đi đâu về đâu
Những ngày không gặp nhau
Biển bạc đầu thương nhớ
Những ngày không gặp nhau
Lòng thuyền đau rạn vỡ
Nếu từ giã thuyền rồi
Biển chỉ còn sóng gió
Nếu phải cách xa anh
Em chỉ còn bão tố
"""
    FILE_GOC       = "fileName.txt"
    FILE_NEN       = "fileName.cmp"
    FILE_KHOI_PHUC = "fileName_restored.txt"
    with open(FILE_GOC, "w", encoding="utf-8") as f:
        f.write(noi_dung_mau)
    print(f"Đã tạo file mẫu : {FILE_GOC}\n")
    compress(FILE_GOC, FILE_NEN)
    print()
    decompress(FILE_NEN, FILE_KHOI_PHUC)
    print()
    verify(FILE_GOC, FILE_KHOI_PHUC)
    print()
    print("=" * 52)
    print(f"  NỘI DUNG FILE NÉN ({FILE_NEN}):")
    print("=" * 52)
    with open(FILE_NEN, "r", encoding="utf-8") as f:
        print(f.read())
    print("=" * 52)
    print(f"  NỘI DUNG FILE KHÔI PHỤC ({FILE_KHOI_PHUC}):")
    print("=" * 52)
    with open(FILE_KHOI_PHUC, "r", encoding="utf-8") as f:
        print(f.read())