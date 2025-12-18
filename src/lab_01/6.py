a, b = 0, 0
for i in range(int(input())):
    k = input().split()[-1]
    if k == "True":
        a += 1
    else:
        b += 1
print(a, b)
