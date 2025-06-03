import numpy as np


def stairs(x):
    return np.lib.stride_tricks.sliding_window_view(np.tile(x, 2), x.size)[-x.size:][::-1]