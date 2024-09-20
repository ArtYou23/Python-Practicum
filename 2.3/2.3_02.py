m = []
c = 0
a = input()
m.append(a)
while a != 'Приехали!':
    a = input()
    m.append(a)
for i in range(len(m)):
    if "зайка" in m[i]:
        c += 1
print(c)