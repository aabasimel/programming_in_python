
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    

    def getReal(self):
        return self.real
    def getImag(self):
        return self.imag
    

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    

   

    def modulus(self):
        return (self.real**2 + self.imag**2)**0.5

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"