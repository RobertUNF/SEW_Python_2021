# Robert Unfried
from functools import total_ordering


@total_ordering
class Fraction:
    """ Class for Fractions
    >>> f1 = Fraction(1,2)
    >>> f1 # __repr__
    Fraction(1, 2)
    >>> print(f1) # __str__
    1/2
    >>> f2 = Fraction(1,4)
    >>> print(f2)
    1/4
    >>> f1+f2
    Fraction(3, 4)
    >>> f3 = Fraction(1,-4)
    >>> print(f3)
    -1/4
    >>> f1+f2+f3
    Fraction(1, 2)
    >>> f2 = Fraction(1,0)
    Traceback (most recent call last):
    ArithmeticError
    """

    def __init__(self, zaehler: int = 1, nenner: int = 1):
        if nenner == 0:
            raise ArithmeticError
        self._positive = 1
        if nenner * zaehler < 0:
            self._positive = -1
        self._numerator = abs(zaehler)
        self._denominator = abs(nenner)
        self.__reduce()

    def __str__(self):
        """ prints the fration 
        >>> f1 = Fraction(13,-45)
        >>> print(f1)
        -13/45
        >>> f2 = Fraction(77,25)
        >>> print(f2)
        3 2/25
        """
        num = ""
        if not self._positive > 0:
            num = "-"
        frac = ""
        if self._numerator // self._denominator != 0:
            num += str(self._numerator // self._denominator) + " "
        if self._numerator % self._denominator != 0:
            frac = str(self._numerator % self._denominator) + "/" + str(self._denominator)
        return (num + frac).strip()

    def __repr__(self):
        """ __repr__ method
        >>> f1 = Fraction(13,-45)
        >>> f1 # __repr__
        Fraction(-13, 45)
        >>> f2 = Fraction(77,25)
        >>> f2 # __repr__
        Fraction(77, 25)
        """
        return self.__class__.__name__ + f"({self._numerator * self._positive}, {self._denominator})"

    def __reduce(self):
        """
        Verwendeter Algorithmus: https://de.wikipedia.org/wiki/Euklidischer_Algorithmus (klassisch)
        >>> f1 = Fraction(44, 12)
        >>> print(f1)
        3 2/3
        >>> f2 = Fraction(115,25)
        >>> print(f2)
        4 3/5
        """
        x, y = self._numerator, self._denominator
        while x != y: x, y = min(x, y), abs(x - y)
        self._numerator, self._denominator = self._numerator // y, self._denominator // y

    def __add__(self, other: "Fraction"):
        return Fraction((self._numerator * other._denominator * self._positive) + \
                        (other._numerator * self._denominator * other._positive),
                        self._denominator * other._denominator)

    def __sub__(self, other: "Fraction"):
        return Fraction((self._numerator * other._denominator * self._positive) - \
                        (other._numerator * self._denominator * other._positive),
                        self._denominator * other._denominator)

    def __mul__(self, other: "Fraction"):
        return Fraction(self._numerator * other._numerator * self._positive * other._positive, \
                        self._denominator * other._denominator)

    def __truediv__(self, other: "Fraction"):
        return Fraction(self._numerator * other._denominator * self._positive * other._positive, \
                        self._denominator * other._numerator)

    def __floordiv__(self, other: "Fraction"):
        return Fraction((self._numerator * other._denominator) // (self._denominator * other._numerator) \
                        * self._positive * other._positive, 1)

    def __eq__(self, other: "Fraction"):
        return self._numerator == other._numerator and self._denominator == other._denominator and \
               self._positive == other._positive

    def __lt__(self, other: "Fraction"):
        if self._positive != other._positive:
            if self._positive > 0:
                return True
            return False
        return self._numerator * other._denominator > other._numerator * self._denominator

    def __abs__(self, other: "Fraction"):
        return Fraction(self._numerator, self._denominator)

    def __float__(self):
        return self._positive * (self._numerator / self._denominator)

    @property
    def numerator(self):
        """The numerator of the fraction"""
        return self._numerator * self._positive

    @numerator.setter
    def numerator(self, value):
        if value < 0: self._positive *= -1
        self._numerator = abs(value)
        self.__reduce()

    @numerator.deleter
    def numerator(self):
        self._numerator = 1

    @property
    def denominator(self):
        """The denominator of the fraction"""
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        if value < 0: self._positive *= -1
        self._denominator = abs(value)
        self.__reduce()

    @denominator.deleter
    def denominator(self):
        self._denominator = 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
