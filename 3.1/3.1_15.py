n = input()
m = [int(i) for i in n.split()]
mm = min(m)
for i in range(mm, 0, -1):
    c = 0
    for u in m:
        if u % i == 0:
            c += 1
    if c == len(m):
        print(i)
        break