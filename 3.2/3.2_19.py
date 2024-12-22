m, s = [], []
for i in range(int(input())):
    k = input().split()[1:]
    m.extend(set([i.replace(",", "") for i in k]))
for i in range(len(m)):
    p = m.pop(0)
    if p not in m:
        s.append(p)
    m.append(p)
print("\n".join(sorted(s)))