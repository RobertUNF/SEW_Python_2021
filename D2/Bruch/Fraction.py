# Robert Unfried
from functools import total_ordering

@total_ordering
class Fraction:
    """
    Python Doc
    """

    def __init__(self, zaehler: int = 1, nenner: int = 1):
        if nenner == 0:
            raise ArithmeticError
        self._positive = True
        if nenner * zaehler < 0:
            self._positive = False
        self._numerator = abs(zaehler)
        self._denominator = abs(nenner)
        self.__reduce()

    def __str__(self):
        num = ""
        if not self._positive:
            num = "-"
        frac = ""
        if self._numerator // self._denominator != 0:
            num += str(self._numerator // self._denominator) + " "
        if self._numerator % self._denominator != 0:
            frac = str(self._numerator % self._denominator) + "/" + str(self._denominator)
        

        return num + frac

    def __repr__(self):
        mult = 1 if self._positive else -1
        return self.__class__.__name__ + f"({self._numerator * mult}, {self._denominator})"

    def __reduce(self):
        """
        Verwendeter Algorithmus: https://de.wikipedia.org/wiki/Euklidischer_Algorithmus (klassisch)
        """
        x, y = self._numerator, self._denominator
        while x!=y: x, y = min(x, y), abs(x-y)
        self._numerator, self._denominator = self._numerator // y, self._denominator // y
    
    def __add__(self, other: "Fraction"):
        return Fraction((self._numerator * other._denominator) + (other._numerator * self._denominator), self._denominator * other._denominator)
    
    def __sub__(self, other: "Fraction"):
        return Fraction((self._numerator * other._denominator) - (other._numerator * self._denominator), self._denominator * other._denominator)

    def __mul__(self, other: "Fraction"):
        return Fraction(self._numerator * other._numerator, self._denominator * other._denominator)

    def __truediv__(self, other: "Fraction"):
        return Fraction(self._numerator * other._denominator, self._denominator * other._numerator)

    def __floordiv__(self, other: "Fraction"):
        return Fraction((self._numerator * other._denominator) // (self._denominator * other._numerator), 1)

    def __eq__(self, other: "Fraction"):
        return self._numerator == other._numerator and self._denominator == other._denominator and \
               self._positive == other._positive

    def __lt__(self, other: "Fraction"):
        if self._positive != other._positive:
            if self._positive:
                return True
            return False
        return self._numerator * other._denominator > other._numerator * self._denominator

    def __abs__(self, other: "Fraction"):
        return Fraction(self._numerator, self._denominator)

    @property
    def numerator(self):
        """The numerator of the fraction"""
        return self._numerator

    @numerator.setter
    def numerator(self, value):
        self._numerator = value

    @numerator.deleter
    def numerator(self):
        del self._numerator

    @property
    def denominator(self):
        """The denominator of the fraction"""
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        self._denominator = value

    @denominator.deleter
    def denominator(self):
        del self._denominator

    @property
    def positive(self):
        """Boolean is true if the fraction is positive"""
        return self._positive

    @positive.setter
    def positive(self, value):
        self._positive = value

    @positive.deleter
    def positive(self):
        del self._positive


if __name__ == '__main__':
    f = Fraction(44, 12)
    print(f)
    print(repr(f))