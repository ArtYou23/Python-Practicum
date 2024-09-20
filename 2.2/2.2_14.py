i = input()
a = int(i[0])
b = int(i[1])
c = int(i[2])
d = []
d.append(a)
d.append(b)
d.append(c)
dd = sorted(d)
if dd[0] == 0:
    print(dd[1], dd[0], " ", dd[2], dd[1], sep='')
else:
    print(dd[0], dd[1], " ", dd[2], dd[1], sep='')