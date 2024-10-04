def f(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


a = int(input())
m = []
aa = a
for i in range(2, a + 1):
    while a % i == 0:
        a = a // i
        m.append(i)
        m.append("*")
if f(aa):
    print(aa)
else:
    m.pop(-1)
    print(*m)