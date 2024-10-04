n = int(input())
pp = [0] * n
m = 0
a = p = ''
for ii in range(n):
    pp[ii] = [0] * 2
for i in range(n):
    p = input()
    c = int(input())
    pp[i][1] = p
    pp[i][0] = sum(map(int, str(c)))
spp = sorted(pp, key=lambda x: x[0])
print(spp[n - 1][1])