def gcd(*sqnc):
    mn = min(sqnc)
    while len(sqnc) != len([x for x in sqnc if x % mn == 0]):
        mn -= 1
    return mn