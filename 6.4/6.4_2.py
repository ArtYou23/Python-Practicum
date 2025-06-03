import numpy as np


def update_cols(array, size, value, *cols):
    sh = array.shape
    cols = set(cols)
    arr = array.reshape(size)
    for i in cols:
        arr[:, i] += value
    return arr.reshape(sh)