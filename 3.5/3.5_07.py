m = []
with open(input(), encoding='UTF-8') as file:
    for line in file:
        m += line.split()
c = pos = mx = sm = middle = 0
mn = 10**10
for i in m:
    i = int(i)
    c += 1
    sm += i
    if i > 0:
        pos += 1
    if i < mn:
        mn = i
    if i > mx:
        mx = i
middle = sm / c
print(c)
print(pos)
print(mn)
print(mx)
print(sm)
print(f"{middle:.2f}")