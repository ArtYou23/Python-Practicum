n, m = [int(input()) for _ in range(2)]
s, ss = set(), set()
for i in range(n):
    s.add(input())
for j in range(m):
    ss.add(input())
if len(s & ss) == 0:
    print("Таких нет")
else:
    print(len(s & ss))