p = [0, 1]
x = input()
print('a b c f')
for a in p:
    for b in p:
        for c in p:
            if eval(x):
                print(a, b, c, 1)
            elif not eval(x):
                print(a, b, c, 0)
            else:
                print(a, b, c, eval(x))