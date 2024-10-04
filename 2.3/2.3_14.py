def f(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


j = int(input())
if j == 1:
    print("NO")
elif f(j) == 0:
    print("NO")
elif f(j) == 1:
    print("YES")