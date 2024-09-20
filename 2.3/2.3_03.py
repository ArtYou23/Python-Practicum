a = int(input())
b = int(input())
m = []
for i in range(a, b + 1, 1):
    m.append(i)
print(*m)