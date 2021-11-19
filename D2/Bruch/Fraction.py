# Robert Unfried

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


if __name__ == '__main__':
    f = Fraction(5, 3)
    print(f)
    print(repr(f))#