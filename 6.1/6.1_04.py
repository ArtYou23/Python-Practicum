from math import prod, pow


m = [float(i) for i in input().split()]
print(pow(prod(i for i in m), (1 / len(m))))