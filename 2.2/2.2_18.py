a = int(input())
b = int(input())
c = int(input())
d = []
d.append(a)
d.append(b)
d.append(c)
dd = sorted(d)
if (dd[2] ** 2) < ((dd[0] ** 2) + (dd[1] ** 2)):
    print("крайне мала")
elif (dd[2] ** 2) == ((dd[0] ** 2) + (dd[1] ** 2)):
    print("100%")
else:
    print("велика")