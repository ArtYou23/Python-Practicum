n = int(input())
ss = {}
for i in range(n):
    ss[input()] = 0
m = int(input())
for i in range(m):
    pp = int(input())
    for j in range(pp):
        if (y := input()) in ss:
            del ss[y]
if len(ss) == 0:
    print("Готовить нечего")
else:
    kl = list(sorted(ss.keys()))
    print("\n".join(i for i in kl))