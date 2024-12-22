d = {}
while (a := input().split()) != []:
    if a[0] in d:
        d[a[0]].add(a[1])
    else:
        d[a[0]] = {a[1]}
    if a[1] in d:
        d[a[1]].add(a[0])
    else:
        d[a[1]] = {a[0]}
dn = {}
for k, v in d.items():
    for j in v:
        if k in dn:
            dn[k].extend(d[j])
        else:
            dn[k] = [i for i in d[j]]
for k in dn:
    dn[k] = set(dn[k])
for i in dn:
    if i in dn[i]:
        dn[i] = [u for u in dn[i] if u != i]

for k in dn:
    dn[k] = sorted(list(set(dn[k]) - set(d[k])))
dn = sorted(dn.items(), key=lambda x: x[0])
for k, v in dn:
    ss = ", ".join(v)
    print(f"{k}: {ss}")
