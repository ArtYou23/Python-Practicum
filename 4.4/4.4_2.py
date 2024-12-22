import math


def add_number(dig):
    global m
    m.append(dig)


def get_prod():
    global m
    return ' * '.join(str(i) for i in m) + " = " + str(math.prod(x for x in m))


m = []