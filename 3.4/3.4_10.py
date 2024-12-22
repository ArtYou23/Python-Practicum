from itertools import product

n = int(input())
k = [i for i in range(1, n + 1)]
g = [i for i in range(1, n + 1)]
p = [i for i in range(1, n + 1)]
print("А Б В")
print('\n'.join(list([f"{i} {j} {u}" for i, j, u in product(k, g, p) if i + j + u == n])))