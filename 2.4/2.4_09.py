n = int(input())
m = ''
for i in range(n):
    u = input()
    m += str(max(map(int, u)))
print(m, sep='')