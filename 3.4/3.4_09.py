import itertools

n = int(input())
k = [i for i in range(1, n + 1)]
g = [i for i in range(1, n + 1)]
s = ''
m = list([i * j for i, j in itertools.product(k, g)])
for i in range(len(m)):
    if i % n == n - 1:
        s += str(m[i]) + '\n'
    else:
        s += str(m[i]) + ' '
print(s)