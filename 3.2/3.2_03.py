n = int(input())
s = set()
m = []
for i in range(n):
    m.append([j for j in input().split()])
    for j in range(len(m[i])):
        s.add(m[i][j])
m = list(s)
for i in range(len(m)):
    print(m[i])