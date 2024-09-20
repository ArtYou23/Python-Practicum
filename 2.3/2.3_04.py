a = int(input())
b = int(input())
m = []
if a < b:
    for i in range(a, b + 1, 1):
        m.append(i)
else:
    for i in range(a, b - 1, -1):
        m.append(i)
print(*m)