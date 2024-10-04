n = int(input())
cc = 0
for j in range(n):
    a = input()
    c = 0
    for i in range(len(a) // 2):
        if a[i] != a[-(i + 1)]:
            c = 1
            break
    if c == 0:
        cc += 1
print(cc)