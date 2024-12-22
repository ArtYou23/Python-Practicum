from itertools import product

x = input()
var = sorted([i for i in set(x.split()) if i.isupper()])
print(*var, "F")
for i in product([0,1], repeat=len(var)):
    globals = {k: v for k, v in zip(var, i)}
    print(*globals.values(), int(eval(x, globals)))