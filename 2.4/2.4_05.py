n = int(input())
cc = 0
for i in range(n):
    c = 0
    p = input()
    if "зайка" in p:
        c += 1
    while p != "ВСЁ":
        p = input()
        if "зайка" in p:
            c += 1
    if c >= 1:
        cc += 1
print(cc)