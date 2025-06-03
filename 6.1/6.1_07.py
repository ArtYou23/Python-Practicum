import numpy as np


def make_board(n):
    return np.fromfunction(
        lambda i, j: 1 - (i + j) % 2,
        (n, n),
        dtype=int
    ).astype(np.int8)