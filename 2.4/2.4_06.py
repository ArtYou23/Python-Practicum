n = int(input())
m = []
for i in range(n):
    p = int(input())
    m.append(p)
mm = min(m)
for i in range(mm, 0, -1):
    c = 0
    for u in m:
        if u % i == 0:
            c += 1
    if c == n:
        print(i)
        break