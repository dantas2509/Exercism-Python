from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.reduce()

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        result = Rational(1,1)
        result.numer = self.numer * other.denom + other.numer * self.denom
        result.denom = self.denom * other.denom
        result.reduce()
        
        return result
        

    def __sub__(self, other):
        result = Rational(1,1)
        result.numer = (self.numer * other.denom) - (other.numer * self.denom)
        result.denom = (self.denom * other.denom)
        result.reduce()

        return result

    def __mul__(self, other):
        result = Rational(1,1)
        result.numer = (self.numer * other.numer)
        result.denom = (self.denom * other.denom)
        result.reduce()

        return result

    def __truediv__(self, other):
        if self.numer == 0 or other.numer == 0:
            return Rational(0,1)
        result = Rational(1,1)
        result.numer = (self.numer * other.denom)
        result.denom = (self.denom * other.numer)
        result.reduce()

        return result

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        result = Rational(1,1)
        if power > 0:
            result.numer = self.numer**power
            result.denom = self.denom**power
        elif power < 0:
            power = abs(power)
            result.numer = self.denom**power
            result.denom = self.numer**power
        self.reduce()
        return result


    def __rpow__(self, base):
        return base ** (self.numer/self.denom)

    def reduce(self):
        if self.numer == 0 and self.denom != 0:
            self.denom /= self.denom
            return
        num = max(abs(self.numer), abs(self.denom))
        gcd = min(abs(self.numer), abs(self.denom))
        aux = 1
    
        while True:
            aux = num % gcd
            num = gcd
            if aux == 0:
                break
            else:
                gcd = aux
        self.numer /= gcd
        self.denom /= gcd

        if self.numer > 0 and self.denom < 0:
            self.denom *= -1
            if self.numer > 0:
                self.numer *= -1
        elif self.numer < 0 and self.denom < 0:
            self.numer = abs(self.numer)
            self.denom = abs(self.denom)