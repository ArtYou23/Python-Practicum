n = int(input())
s = {}
for i in range(n):
    k, ll = input().replace(" ", "*", 1).split("*")
    s[k] = ll
ko = input()
c = 0
ss = []
for i in s:
    if ko in s[i]:
        ss.append(i)
        c = 1
if c == 0:
    print("Таких нет")
print("\n".join(sorted(ss)))