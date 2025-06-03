import pandas as pd
from numpy import arange


def values(func, start, end, step):
    ind = arange(start, end + step, step)
    return pd.Series(map(func, ind), index=ind, dtype=float)


def min_extremum(data):
    return min(data[data == min(data)].index)


def max_extremum(data):
    return max(data[data == max(data)].index)