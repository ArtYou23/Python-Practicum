ln = int(input())
n = int(input())
for i in range(n):
    p = input()
    if len(p) >= ln - 3:
        print(p[:ln - 3] + "...")
        break
    else:
        ln -= len(p)
        print(p)