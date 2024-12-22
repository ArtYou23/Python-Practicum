ln = int(input())
n = int(input())
for i in range(n):
    u = input()
    if len(u) <= ln:
        print(u)
    else:
        print(u[:(ln - 3)] + "...")