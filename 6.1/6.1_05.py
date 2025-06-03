from math import sin, cos, dist


dec = [float(i) for i in input().split()]
pol = [float(j) for j in input().split()]
print(dist(dec, [cos(pol[1]) * pol[0], sin(pol[1]) * pol[0]]))