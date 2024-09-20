i = str(abs(int(input())))
d = [0] * 3
d[0] = i[0]
d[1] = i[1]
d[2] = i[2]
dd = sorted(d)
if (int(dd[0]) + int(dd[2])) == (int(dd[1]) * 2):
    print("YES")
else:
    print("NO")