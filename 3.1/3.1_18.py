n = input()
c = 0
m = []
for i in range(len(n) - 1):
    m.append(int(n[i]))
    if n[i] != n[i + 1]:
        m.append(" ")
m.append(int(n[-1]))
s = ''
for i in m:
    s += str(i)
s = s.split()
for i in s:
    print(i[0], len(i))