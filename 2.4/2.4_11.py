def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


c = 0
n = int(input())
for i in range(n):
    k = int(input())
    if f(k):
        c += 1
print(c)