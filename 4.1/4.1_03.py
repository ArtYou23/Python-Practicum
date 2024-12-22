def number_length(number):
    ns = str(number)
    if ns[0] == "-":
        return len(ns) - 1
    else:
        return len(ns)