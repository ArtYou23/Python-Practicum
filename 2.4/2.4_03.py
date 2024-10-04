n = int(input())
c = h = 1
s = ''
for i in range(1, n + 1):
    s = s + str(i) + ' '
    if s.count(' ') == c:
        s = s + '\n'
        h += 1
        c += h
print(s)