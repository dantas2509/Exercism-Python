from math import sqrt, cos, sin, e
import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.imaginary * other.real + self.real * other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) / (pow(other.real, 2) + (pow(other.imaginary, 2))),
                             (self.imaginary * other.real - self.real * other.imaginary)/(pow(other.real, 2) + pow(other.imaginary, 2)))

    def __abs__(self):
        return sqrt(pow(self.real, 2) + pow(self.imaginary, 2))

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(pow(e, self.real), 0) * ComplexNumber(cos(self.imaginary), sin(self.imaginary))



c1 = ComplexNumber(math.log(2), math.pi).exp()
c2 = ComplexNumber(-2, 0)

print(c1.real, c1.imaginary)
print(c2.real, c2.imaginary)