s = ''' Chiều chiều trước bến Văn Lâu
Ai ngồi, ai câu, ai sầu, ai thảm 
Ai thương, ai cảm, ai nhớ, ai trông
Thuyền ai thấp thoáng ven sông
Đưa câu mái vẩy chạnh lòng nước non '''

word = "ai"

ds = s.split()

dem = 0
for i in ds:
    if i == word:   # chỉ đúng "ai" (không tính "Ai," hay "Ai")
        dem += 1

print(dem)