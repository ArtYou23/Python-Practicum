from itertools import combinations

print('\n'.join(list(f"{i} - {j}" for i, j in list(combinations([input() for _ in range(int(input()))], 2)))))