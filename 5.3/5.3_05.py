def merge(a, b):
    if not hasattr(a, '__iter__') or not hasattr(b, '__iter__'):
        raise StopIteration
    if not all(isinstance(x, type(a[0])) for x in (list(a) + list(b))):
        raise TypeError
    if list(a) != sorted(list(a)) or list(b) != sorted(list(b)):
        raise ValueError
    return tuple(sorted(list(a) + list(b)))