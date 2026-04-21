from datetime import datetime, date, timedelta

now = datetime(2019, 9, 18, 19, 25, 58)

print(now.year)
print(now.strftime("%B"))
print(now.isocalendar()[1])
print((now.day - 1)//7 + 1)
print(now.timetuple().tm_yday)
print(now.day)
print(now.strftime("%A"))
print(now.strftime("%H:%M:%S"))

print("-----")

d1 = date(2019, 9, 1)
d2 = date(2019, 9, 18)
print(abs((d2 - d1).days))

print("-----")

s = "Sep 18 2019 2:43PM"
d = datetime.strptime(s, "%b %d %Y %I:%M%p")
print(d)

print("-----")

print(now + timedelta(seconds=5))