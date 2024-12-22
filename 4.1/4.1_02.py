def gcd(a, b):
    mx = max(a, b)
    mn = min(a, b)
    for i in range(mn, 0, -1):
        if mx % i == 0 and mn % i == 0:
            return i