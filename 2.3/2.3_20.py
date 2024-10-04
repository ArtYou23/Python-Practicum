n = int(input())
h = [0] * (n + 1)
c = 0
for i in range(1, n + 1):
    u = int(input())
    h[i] = u % 256
    r = (u // 256) % 256
    m = u // 256 ** 2
    if h[i] == (37 * (m + r + h[i - 1])) % 256 and h[i] < 100:
        h[i] = (37 * (m + r + h[i - 1])) % 256
    else:
        c = i
        print(i - 1)
        break
if c == 0:
    print(-1)