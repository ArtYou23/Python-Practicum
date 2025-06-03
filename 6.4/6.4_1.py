from math import sin, cos, tan, pi
from sys import stdin


for x in stdin:
    x = float(x)
    a = sin(pi - x) * cos(3 * pi / 2 + x) * tan(x - 3 * pi / 2)
    b = cos(pi / 2 - x) * cos(3 * pi / 2 - x) * tan(x - pi)
    print(f"{a / b:.3f}")