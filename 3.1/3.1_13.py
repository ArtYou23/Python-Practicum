n = int(input())
m = [0] * n
for i in range(n):
    m[i] = int(input())
p = int(input())
for i in range(n):
    m[i] = (m[i]) ** p
    print(m[i])