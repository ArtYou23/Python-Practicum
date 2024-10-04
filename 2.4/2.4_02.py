n = int(input())
for j in range(1, n + 1):
    for k in range(1, n + 1):
        r = k * j
        print(k, "*", j, "=", r)
