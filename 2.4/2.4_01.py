n = int(input())
for i in range(1, n + 1):
    m = []
    for j in range(1, n + 1):
        m.append(j * i)
    print(*m)