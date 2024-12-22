from sys import stdin

c = r = 0
for i in stdin:
    i = i.split()
    r += int(i[2]) - int(i[1])
    c += 1
print(round(r / c))