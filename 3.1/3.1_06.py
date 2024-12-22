n = int(input())
c = 0
ss = ''
for i in range(n):
    u = input()
    ss += u + ' '
m = ss.split()
for j in m:
    if j == "зайка":
        c += 1
print(c)