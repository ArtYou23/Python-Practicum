import itertools


def re_name(k):
    if k == "буби":
        return "бубен"
    elif k == "пики":
        return "пик"
    elif k == "трефы":
        return "треф"
    elif k == "черви":
        return "червей"


mast = re_name(input())
dost = sorted(["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"])
dd = input()
pred = input()
dost.remove(dd)
masts = ["бубен", "пик", "треф", "червей"]
c = 0
for x in itertools.combinations(itertools.product(dost, masts), 3):
    m = []
    [[m.append(j) for j in i] for i in x]
    if c == 1 and mast in m:
        print(', '.join(' '.join(i) for i in x))
        break
    if mast in m:
        if pred == ', '.join(' '.join(i) for i in x):
            c = 1