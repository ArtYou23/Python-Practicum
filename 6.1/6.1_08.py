import numpy as np


def snake(m, n, direction='H'):
    if direction == 'V':
        return np.fromfunction(
            lambda i, j: j * n + np.where(j % 2 == 0, i, n - 1 - i) + 1,
            (n, m),
            dtype=int
        ).astype(np.int16)
    return np.fromfunction(
        lambda i, j: i * m + np.where(i % 2 == 0, j, m - 1 - j) + 1,
        (n, m),
        dtype=int
    ).astype(np.int16)


print(snake(5, 3, direction='H'))