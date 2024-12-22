n, m = [int(input()) for _ in range(2)]
s, ss = [], []
for i in range(n + m):
    if (k := input()) in s:
        ss.append(k)
    else:
        s.append(k)
pr = (len(s) - len(ss))
if pr == 0:
    print("Таких нет")
else:
    print(pr)