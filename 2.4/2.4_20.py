n = int(input())
mss = ms = 0
for ss in range(10, 1, -1):
    nn = n
    s = 0
    while nn != 0:
        s += nn % ss
        nn = nn // ss
    if s >= ms:
        ms = s
        mss = ss
print(mss)