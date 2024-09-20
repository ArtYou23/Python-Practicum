a = input()
b = input()
c = input()
d = []
d.append(a)
d.append(b)
d.append(c)
dd = sorted(d)
for i in range(3):
    if "зайка" in dd[i]:
        print(dd[i], len(dd[i]))
        break