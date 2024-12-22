from itertools import permutations

n = int(input())
m = sorted([input() for _ in range(n)])
print('\n'.join([', '.join(j for j in i) for i in permutations(m, 3)]))