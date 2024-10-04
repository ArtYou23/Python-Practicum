n = int(input())
c = h = 1
s = ''
cc = ''
pos = mm = 0
for i in range(1, n + 1):
    s += str(i) + ' '
    cc += str(i) + ' '
    mm = max(mm, len(cc))
    if s.count(' ') == c:
        s = s + '\n'
        h += 1
        c += h
        mm = max(mm, len(cc))
        cc = ''
mmm = mm
c2 = h2 = 1
s2 = ''
cc2 = ''
pos2 = 0
for i in range(1, n + 1):
    s2 += str(i) + ' '
    cc2 += str(i) + ' '
    if s2.count(' ') == c2:
        s2 = s2 + '\n'
        h2 += 1
        c2 += h2
        print(f"{cc2: ^{mmm}}")
        cc2 = ''
        pos2 = i
    if i == n and pos2 != i:
        print(f"{cc2: ^{mmm}}")