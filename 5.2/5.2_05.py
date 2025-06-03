class Fraction:

    def __init__(self, *args):
        if isinstance(args[0], str):
            ch, z = map(int, args[0].split('/'))
            self.__num = ch
            self.__den = z
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def __reduction(self):
        gcd = self.__gcd(self.__num, self.__den)
        self.__num = self.__num // gcd
        self.__den = self.__den // gcd
        if self.__num * self.__den < 0:
            self.__num = abs(self.__num)
            self.__den = abs(self.__den)
            self.__num *= -1
        else:
            self.__num = abs(self.__num)
            self.__den = abs(self.__den)
        return self

    def __str__(self):
        return f'{self.__num}/{self.__den}'

    def __repr__(self):
        return f"Fraction('{self.__num}/{self.__den}')"

    def __sign(self):
        return -1 if self.__num < 0 else 1

    def __neg__(self):
        return Fraction(-self.__num, self.__den)

    def numerator(self, *args):
        if len(args):
            self.__num = args[0] * self.__sign()
            self.__reduction()
        else:
            return abs(self.__num)

    def denominator(self, *args):
        if len(args):
            self.__den = args[0]
            self.__reduction()
        else:
            return abs(self.__den)