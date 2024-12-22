n = int(input())
d = {}
for i in range(n):
    k = input()
    if k in d:
        d[k] += 1
    else:
        d[k] = 1
c = 0
for i in d.values():
    if int(i) > 1:
        c += int(i)
print(c)