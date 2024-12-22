n = int(input())
bluda = {}
m = []
for i in range(n):
    bluda[input()] = 1
ingr = int(input())
for i in range(ingr):
    c = 0
    bl = input()
    k = int(input())
    for j in range(k):
        ing = input()
        if ing in bluda:
            bluda[ing] -= 1
            if bluda[ing] <= 0:
                c += 1
    if c == k:
        m.append(bl)

if len(m) != 0:
    print("\n".join(sorted(m)))
else:
    print("Готовить нечего")