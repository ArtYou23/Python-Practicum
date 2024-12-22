n = [bin(int(i))[2:] for i in input().split()]
m = []
for i in n:
    s = {}
    s["digits"] = len(i)
    s["units"] = i.count("1")
    s["zeros"] = i.count("0")
    m.append(s)
print(m)