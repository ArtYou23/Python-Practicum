from math import gcd
from sys import stdin


print(*[gcd(*map(int, i.split())) for i in stdin], sep="\n")