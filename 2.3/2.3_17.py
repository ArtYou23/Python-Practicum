a = input()
m = []
for i in range(len(a)):
    if int(a[i]) % 2 == 1:
        m.append(a[i])
print(*m, sep='')