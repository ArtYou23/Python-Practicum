d = dict()
m = []
while (n := input()) != '':
    m += list([i.upper() for i in n.split()])
for i in m:
    if len(i) in d:
        d[len(i)].add(i)
    else:
        d[len(i)] = {i}
for i in d:
    print(f"{i}: {'; '.join(sorted(d[i], reverse=True))}")