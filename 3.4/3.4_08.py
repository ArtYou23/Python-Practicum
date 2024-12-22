from itertools import islice

if len((m := [input() for _ in range(int(input()))])) >= (n := int(input())):
    print('\n'.join(list(islice(m, n))))
else:
    [m.append(m[i]) for i in range(n - len(m))]
    print('\n'.join(m))