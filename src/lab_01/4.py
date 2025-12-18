a = int(input())
print(f"Минуты: {a}")
d = a % 60
if d < 10:
    d = "0" + str(d)
print(f"{a // 60}:{d}")
