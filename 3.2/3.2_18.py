d = dict()
for i in range(int(input())):
    x, y = input().split()
    j = (x[:-1], y[:-1])
    d[j] = d.get(j, 0) + 1
print(max(d.values()))