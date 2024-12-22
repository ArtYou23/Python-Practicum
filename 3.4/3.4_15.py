from itertools import product, permutations

s = ''
for i in range((n := int(input()))):
    s += input().replace(',', '') + ' '
m = sorted(s.split())
print('\n'.join(list(f"{i} {j} {k}" for i, j, k in permutations(m, 3))))