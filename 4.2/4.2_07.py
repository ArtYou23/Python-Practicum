def enter_results(*cort):
    global pair
    pair += [(cort[x], cort[x + 1]) for x in range(0, len(cort), 2)]


def get_sum():
    global pair, c, cc
    c = sum(x[0] for x in pair)
    cc = sum(x[1] for x in pair)
    return round(c, 2), round(cc, 2)


def get_average():
    global pair, c, cc
    return round(c / len(pair), 2), round(cc / len(pair), 2)


pair = []
c, cc = 0, 0