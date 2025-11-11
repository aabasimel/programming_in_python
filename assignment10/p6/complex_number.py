# CTMS-14
# complex_number.py
# Ahmed Abasimel
# aabasimel@constructor.university

class Complex:
    """Represents a complex number."""
    
    def __init__(self, real, imag):
        """Constructor creates a complex number with given real and imaginary parts."""
        self.real = real
        self.imag = imag
    
    def getReal(self):
        """Returns the real part."""
        return self.real
    
    def getImag(self):
        """Returns the imaginary part."""
        return self.imag
    
    def __str__(self):
        """Returns the string representation of the complex number."""
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"
    
    def __repr__(self):
        """Returns the official string representation."""
        return f"Complex({self.real}, {self.imag})"
    
    def __add__(self, other):
        """Overloads the + operator for complex number addition."""
        if not isinstance(other, Complex):
            return NotImplemented
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return Complex(new_real, new_imag)
    
    def __sub__(self, other):
        """Overloads the - operator for complex number subtraction."""
        if not isinstance(other, Complex):
            return NotImplemented
        new_real = self.real - other.real
        new_imag = self.imag - other.imag
        return Complex(new_real, new_imag)
    
    def __mul__(self, other):
        """Overloads the * operator for complex number multiplication."""
        if not isinstance(other, Complex):
            return NotImplemented
        # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        a, b = self.real, self.imag
        c, d = other.real, other.imag
        new_real = (a * c) - (b * d)
        new_imag = (a * d) + (b * c)
        return Complex(new_real, new_imag)
    
    def __truediv__(self, other):
        """Overloads the / operator for complex number division."""
        if not isinstance(other, Complex):
            return NotImplemented
        
        # Check for division by zero
        if other.real == 0 and other.imag == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number")
        
        # (a + bi) / (c + di) = ((ac + bd)/(c² + d²)) + ((bc - ad)/(c² + d²))i
        a, b = self.real, self.imag
        c, d = other.real, other.imag
        denominator = (c * c) + (d * d)
        
        new_real = (a * c + b * d) / denominator
        new_imag = (b * c - a * d) / denominator
        
        return Complex(new_real, new_imag)
    
    def __eq__(self, other):
        """Overloads the == operator for complex number equality."""
        if not isinstance(other, Complex):
            return False
        # Two complex numbers are equal if both real and imaginary parts are equal
        return self.real == other.real and self.imag == other.imag
    
    def __ne__(self, other):
        """Overloads the != operator for complex number inequality."""
        return not self.__eq__(other)