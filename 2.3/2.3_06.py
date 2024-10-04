a = int(input())
b = int(input())
k = max(a, b)
ll = min(a, b)
for i in range(k, 0, -1):
    if k % i == 0 and ll % i == 0:
        print(i)
        break