from math import log, pow, sin, cos, pi, e


x = float(input())
y = log(pow(x, 3 / 16), 32) + pow(x, cos((pi * x) / (2 * e))) - pow(sin(x / pi), 2)
print(y)