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
        self.positive = True
        if nenner * zaehler < 0:
            self.positive = False
        self.zaehler = abs(zaehler)
        self.nenner = abs(nenner)
        self.__reduce()

    def __str__(self):
        num = ""
        if not self.positive:
            num = "-"
        frac = ""
        if self.zaehler // self.nenner != 0:
            num += str(self.zaehler // self.nenner) + " "
        if self.zaehler % self.nenner != 0:
            frac = str(self.zaehler % self.nenner) + "/" + str(self.nenner)
        

        return num + frac

    def __repr__(self):
        mult = 1 if self.positive else -1
        return self.__class__.__name__ + f"({self.zaehler*mult}, {self.nenner})"

    def __reduce(self):
        """
        Verwendeter Algorithmus: https://de.wikipedia.org/wiki/Euklidischer_Algorithmus (klassisch)
        """
        x = self.zaehler
        y = self.nenner
        while x!=y:
            x, y = min(x, y), abs(x-y)
        self.zaehler = int(self.zaehler/y)
        self.nenner = int(self.nenner/y)
    
    def __add__(self, other: "Fraction"):
        return Fraction((self.zaehler*other.nenner)+(other.zaehler*self.nenner), self.nenner * other.nenner)
    
    def __sub__(self, other: "Fraction"):
        return Fraction((self.zaehler*other.nenner)-(other.zaehler*self.nenner), self.nenner * other.nenner)

    def __mul__(self, other: "Fraction"):
        return Fraction(self.zaehler*other.zaehler, self.nenner * other.nenner)

    def __truediv__(self, other: "Fraction"):
        return Fraction(self.zaehler*other.nenner, self.nenner * other.zaehler)

    def __floordiv__(self, other: "Fraction"):
        return Fraction((self.zaehler*other.nenner) // (self.nenner*other.zaehler), 1)


if __name__ == '__main__':
    f = Fraction(44, 12)
    print(f)
    print(repr(f))#