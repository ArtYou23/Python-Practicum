def f(n):
    m = [[0] * n for _ in range(n)]
    for beg in range((n + 1) // 2):
        for i in range(beg, n - beg):
            m[beg][i] = beg + 1
            m[n - beg - 1][i] = beg + 1
        for j in range(beg, n - beg):
            m[j][beg] = beg + 1
            m[j][n - beg - 1] = beg + 1
    return m


def ff(m):
    w = len(str(max(max(i) for i in m)))
    for i in m:
        print(' '.join(f"{num: >{w}}" for num in i))


n = int(input())
m = f(n)
ff(m)