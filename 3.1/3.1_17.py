n = input()
nn = []
nn += [i.lower() for i in n.split()]
s = ''
for i in nn:
    s += i
if s == s[::-1]:
    print("YES")
else:
    print("NO")