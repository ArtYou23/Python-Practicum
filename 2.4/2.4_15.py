def ff(m):
    w = len(str(max(max(i) for i in m)))
    for i in m:
        print(' '.join(f"{num: >{w}}" for num in i))


y = int(input())
x = int(input())
m = [[0] * x for _ in range(y)]
for j in range(1, y + 1):
    for i in range(1, x + 1):
        if i % 2 == 1:
            m[j - 1][i - 1] = j + (i - 1) * y
        else:
            m[j - 1][i - 1] = 1 + (i - 1) * y + (y - j)
ff(m)