m, n = [int(input()) for _ in range(2)]
print(', '.join([str(i) for i in range(n, m + 1, (n - m) % 10)]))