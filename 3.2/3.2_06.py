n, m = [int(input()) for _ in range(2)]
s, ss = [], []
for i in range(n + m):
    if (k := input()) in s:
        ss.append(k)
    else:
        s.append(k)
t = sorted(set(s) - set(ss))
if len(t) == 0:
    print("Таких нет")
else:
    print('\n'.join(t))