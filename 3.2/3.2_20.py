def vzaimno_prostye(a, b):
    i = max(a, b)
    j = min(a, b)
    while j:
        i, j = j, i % j
    return i


def f(a, b):
    if vzaimno_prostye(a, b) == 1:
        return 1
    else:
        return 0


n = sorted(set((int(i) for i in input().split("; "))))
for i in range(len(n)):
    k = n.pop(0)
    kk = []
    for u in n:
        if f(k, u):
            kk.append(u)
    if kk:
        print(k, "-", ", ".join(str(i) for i in sorted(kk)))
    else:
        ...
    n.append(k)