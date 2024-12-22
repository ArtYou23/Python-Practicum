n = int(input())
c = 0
for i in range(n):
    u = input()
    if u[0] in "абв":
        c += 1
if c == n:
    print("YES")
else:
    print("NO")