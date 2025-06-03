import numpy as np


def rotate(m, grad):
    if grad == 90:
        m = np.rot90(m, -1)
        return m
    elif grad == 180:
        m = np.rot90(m, -2)
        return m
    elif grad == 270:
        m = np.rot90(m, 1)
        return m
    else:
        return m