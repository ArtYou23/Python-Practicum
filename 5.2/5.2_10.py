class Fraction:

    def __init__(self, *args):
        if isinstance(args[0], str):
            if "/" in args[0]:
                ch, z = map(int, args[0].split('/'))
                self.__num = ch
                self.__den = z
            else:
                self.__num = int(args[0])
                self.__den = 1
        elif isinstance(args[0], int):
            if len(args) == 2:
                self.__num = args[0]
                self.__den = args[1]
            else:
                self.__num = args[0]
                self.__den = 1
        else:
            print("idk")

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

    def __cden(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        scm = self.__den * other.__den // self.__gcd(self.__den, other.__den)
        m1 = scm // self.__den
        m2 = scm // other.__den
        return m1 * self.__num, m2 * other.__num, scm

    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        m1, m2, scm = self.__cden(other)
        return Fraction(m1 + m2, scm)

    def __radd__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        m1, m2, scm = self.__cden(other)
        return Fraction(m1 + m2, scm)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        m1, m2, scm = self.__cden(other)
        return Fraction(m1 - m2, scm)

    def __rsub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        m1, m2, scm = self.__cden(other)
        return Fraction(m2 - m1, scm)

    def __iadd__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        m1, m2, scm = self.__cden(other)
        self.__num = m1 + m2
        self.__den = scm
        self.__reduction()
        return self

    def __isub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        m1, m2, scm = self.__cden(other)
        self.__num = m1 - m2
        self.__den = scm
        self.__reduction()
        return self

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(self.__num * other.__num, self.__den * other.__den)

    def __rmul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(self.__num * other.__num, self.__den * other.__den)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(self.__num * other.__den, self.__den * other.__num)

    def __rtruediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(self.__den * other.__num, self.__num * other.__den)

    def __imul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        self.__num *= other.__num
        self.__den *= other.__den
        self.__reduction()
        return self

    def __itruediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        rev = other.reverse()
        self.__num *= rev.__num
        self.__den *= rev.__den
        self.__reduction()
        return self

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        m1, m2, scm = self.__cden(other)
        return m1 < m2

    def __le__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        m1, m2, scm = self.__cden(other)
        return m1 <= m2

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        m1, m2, scm = self.__cden(other)
        return m1 == m2

    def __ne__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        m1, m2, scm = self.__cden(other)
        return m1 != m2

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        m1, m2, scm = self.__cden(other)
        return m1 > m2

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        m1, m2, scm = self.__cden(other)
        return m1 >= m2

    def reverse(self):
        return Fraction(self.__den, self.__num)