from itertools import product

s = ["пик", "треф", "бубен", "червей"]
s.remove(input())
m = [2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"]
print('\n'.join(list(f"{i} {j}" for i, j in product(m, s))))