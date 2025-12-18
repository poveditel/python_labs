s, a, k, e, abc, p = input(), "0987654321", "", 0, "ASDFGHJKLQWERTYUIOPZXCVBNM", "s"
for i in s:
    if i not in a:
        if i in abc:
            k += i
            ns = s[s.index(i) + 1 :]
            break
for n in range(len(ns)):
    i = ns[n]
    if p in a:
        k += i
        e = n
        nks = ns[n + 1 :]
        break
    p = i
t = len(nks)
while t > e:
    k += nks[e]
    nks = nks[e + 1 :]
    t -= e + 1
print(k)
