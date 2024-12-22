from itertools import count

i, j, k = [float(u) for u in (input().split())]
for u in count(i, k):
    if u >= j:
        break
    else:
        print(f"{u:.2f}")