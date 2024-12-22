import math

n = [i for i in input().split()]
sim = "+-*/~!#@"
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
        if i == "/":
            i1 = m.pop(-2)
            i2 = m.pop(-1)
            m.append(i1 // i2)
        if i == "~":
            i1 = m[-1]
            m[-1] = -i1
        if i == "!":
            i1 = m[-1]
            m[-1] = math.factorial(i1)
        if i == "#":
            i1 = m[-1]
            m.append(i1)
        if i == "@":
            i1 = m.pop(-3)
            i2 = m.pop(-2)
            i3 = m.pop(-1)
            m.append(i2)
            m.append(i3)
            m.append(i1)
    elif i.isnumeric():
        m.append(int(i))
print(*m)