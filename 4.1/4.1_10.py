def merge(tt1, tt2):
    t1 = list(tt1)
    t2 = list(tt2)
    t = []
    while t1 and t2:
        if t1[0] < t2[0]:
            t.append(t1.pop(0))
        elif t1[0] > t2[0]:
            t.append(t2.pop(0))
        elif t1[0] == t2[0]:
            t.append(t1.pop(0))
    t.extend(t1)
    t.extend(t2)
    return tuple(t)