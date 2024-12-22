def to_string(*data, sep=" ", end="\n"):
    return sep.join(str(x) for x in data) + end