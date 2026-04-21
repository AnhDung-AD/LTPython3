s = '''   Quê huong
Quê huong , la chum khe ngot .
   Cho con treo hai moi ngay .
Quê huong la duong di hoc .
   Con ve , rop buom vang bay .
   Do Trung Quan   '''

lines = s.split('\n')

ketqua = []

for line in lines:
    line = line.strip()
    
    words = line.split()
    line = " ".join(words)
    
    line = line.replace(" ,", ",").replace(" .", ".")
    
    ketqua.append(line)

result = "\n".join(ketqua)

print(result)