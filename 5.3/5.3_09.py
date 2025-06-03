class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def name_validation(nick):
    if not isinstance(nick, str):
        raise TypeError
    elif sum(letter.lower() in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" for letter in nick) != len(nick):
        raise CyrillicError
    elif nick != nick.lower().capitalize():
        raise CapitalError
    return nick


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError
    cond = "1234567890_abcdefghijklmnopqrstuvwxyz"
    if sum(i.lower() not in cond for i in name) > 0:
        raise BadCharacterError
    elif name[0] in "1234567890":
        raise StartsWithDigitError
    return name


def user_validation(**kwargs):
    k = [key for key in kwargs]
    val = [value for value in kwargs.values()]
    if not ("last_name" in k and "first_name" in k and "username" in k and len(k) == 3):
        raise KeyError
    elif sum(not isinstance(v, str) for v in val) > 0:
        raise TypeError
    name_validation(kwargs["last_name"])
    name_validation(kwargs["first_name"])
    username_validation(kwargs["username"])
    return dict(zip(k, val))