# Robert Unfried

class Fraction:
    """
    Python Doc
    """

    def __init__(self, zaehler: int = 1, nenner: int = 1):
        if nenner == 0:
            raise ArithmeticError
        mult = 1
        if nenner < 0:
            mult = -1
        self.zaehler = zaehler * mult
        self.nenner = nenner * mult

    def __str__(self):
        num = ""
        frac = ""
        if self.zaehler // self.nenner != 0:
            num = str(self.zaehler // self.nenner) + " "
        if self.zaehler % self.nenner != 0:
            frac = str(self.zaehler % self.nenner) + "/" + str(self.nenner)
        return num + frac

    def __repr__(self):
        return self.__class__.__name__ + f"({self.zaehler}, {self.nenner})"


if __name__ == '__main__':
    f = Fraction(5, 3)
    print(f)
    print(repr(f))
