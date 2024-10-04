a = int(input())
b = int(input())
k = max(a, b)
ll = min(a, b)
for i in range(ll, a * b + 1):
    if i % k == 0 and i % ll == 0:
        print(i)
        break