import pandas as pd


def get_long(ser, min_length=5):
    return ser[ser >= min_length]