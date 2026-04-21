from datetime import datetime, date, timedelta

now = datetime.now()

print(f"Năm hiện tại: {now.year}")
print(f"Tháng hiện tại bằng chữ: {now.strftime('%B')}")
print(f"Tuần hiện tại là tuần thứ mấy trong năm: {now.isocalendar()[1]}")
print(f"Tuần hiện tại là tuần thứ mấy trong tháng: {(now.day - 1)//7 + 1}")
print(f"Ngày hiện tại là ngày thứ mấy trong năm: {now.timetuple().tm_yday}")
print(f"Ngày dương lịch hiện tại là ngày: {now.day}")
print(f"Thứ của ngày hiện tại: {now.strftime('%A')}")
print(f"Giờ phút giây hiện tại: {now.strftime('%H:%M:%S')}")

print("-" * 10)

d1 = date(now.year, now.month, 1)
d2 = now.date()
print(f"Số ngày từ đầu tháng ({d1}) đến hôm nay ({d2}): {abs((d2 - d1).days)} ngày")

print("-" * 10)

s = "Sep 18 2019 2:43PM"
d_converted = datetime.strptime(s, "%b %d %Y %I:%M%p")
print(f"Chuỗi '{s}' sau khi chuyển thành datetime: {d_converted}")

print("-" * 10)

new_time = now + timedelta(seconds=5)
print(f"Thời gian hiện tại: {now.strftime('%H:%M:%S')}")
print(f"Thời gian sau khi thêm 5 giây: {new_time.strftime('%H:%M:%S')}")