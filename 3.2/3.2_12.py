n = int(input())
d = {}
for i in range(n):
    k = input()
    if k in d:
        d[k] += 1
    else:
        d[k] = 1
cc = 0
c = ""
for i in d:
    if d[i] > 1:
        cc += 1
        c += i + " - " + str(d[i]) + "\n"
ll = [[0 for _ in range(2)] for _ in range(cc)]
if c == "":
    print("Однофамильцев нет")
else:
    c = c.split("\n")
    c.pop(-1)
    lll = sorted([[nn, int(ss)] for nn, ss in (u.split(" - ") for u in c)])
    for i in lll:
        print(*(i[0], "-", i[1]))