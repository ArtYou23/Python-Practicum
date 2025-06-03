class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError
    cond = "1234567890_abcdefghijklmnopqrstuvwxyz"
    if sum(i.lower() not in cond for i in name) > 0:
        raise BadCharacterError
    elif name[0] in "1234567890":
        raise StartsWithDigitError
    return name