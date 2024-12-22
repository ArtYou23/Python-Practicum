p = {}
while (s := input()) != "":
    s = s.split()
    for i in s:
        if i not in p:
            p[i] = 1
        else:
            p[i] += 1
for i in p:
    print(i, p[i])