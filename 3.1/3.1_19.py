n = [i for i in input().split()]
sim = "+-*"
m = []
for i in n:
    if i in sim:
        if i == "+":
            i1 = m.pop(-2)
            i2 = m.pop(-1)
            m.append(i1 + i2)
        if i == "-":
            i1 = m.pop(-2)
            i2 = m.pop(-1)
            m.append(i1 - i2)
        if i == "*":
            i1 = m.pop(-2)
            i2 = m.pop(-1)
            m.append(i1 * i2)
    elif i.isnumeric():
        m.append(int(i))
print(*m)