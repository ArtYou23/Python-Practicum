class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(nick):
    if not isinstance(nick, str):
        raise TypeError
    elif sum(letter.lower() in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" for letter in nick) != len(nick):
        raise CyrillicError
    elif nick != nick.lower().capitalize():
        raise CapitalError
    return nick