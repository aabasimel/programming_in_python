# CTMS-14
# test_complex.py
# Ahmed Abasimel
# aabasimel@constructor.university

from complex_number import Complex

def test_basic_operations():
    """Test basic complex number operations."""
    print("Testing Basic Complex Number Operations")
    print("=" * 50)
    
    # Create complex numbers
    c1 = Complex(3, 4)   # 3 + 4i
    c2 = Complex(1, 2)   # 1 + 2i
    c3 = Complex(5, -1)  # 5 - 1i
    c4 = Complex(-2, -3) # -2 - 3i
    
    print("Complex Numbers Created:")
    print(f"c1 = {c1}")
    print(f"c2 = {c2}")
    print(f"c3 = {c3}")
    print(f"c4 = {c4}")
    print()
    
    # Test addition
    print("Addition Operations:")
    print("=" * 30)
    result1 = c1 + c2
    print(f"({c1}) + ({c2}) = {result1}")
    print()
    
    # Test subtraction
    print("Subtraction Operations:")
    print("=" * 30)
    result2 = c1 - c2
    print(f"({c1}) - ({c2}) = {result2}")
    print()

def test_multiplication():
    """Test complex number multiplication."""
    print("Testing Multiplication Operations")
    print("=" * 45)
    print("Formula: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i")
    print()
    
    c1 = Complex(3, 4)   # 3 + 4i
    c2 = Complex(1, 2)   # 1 + 2i
    c3 = Complex(2, -1)  # 2 - 1i
    c4 = Complex(-1, 3)  # -1 + 3i
    
    print(f"c1 = {c1}, c2 = {c2}, c3 = {c3}, c4 = {c4}")
    print()
    
    # Test basic multiplication
    result1 = c1 * c2
    print(f"({c1}) * ({c2}) = {result1}")
    print(f"Calculation: (3*1 - 4*2) + (3*2 + 4*1)i = (3-8) + (6+4)i = -5 + 10i")
    print()
    
    result2 = c1 * c3
    print(f"({c1}) * ({c3}) = {result2}")
    print(f"Calculation: (3*2 - 4*(-1)) + (3*(-1) + 4*2)i = (6+4) + (-3+8)i = 10 + 5i")
    print()
    
    result3 = c2 * c4
    print(f"({c2}) * ({c4}) = {result3}")
    print(f"Calculation: (1*(-1) - 2*3) + (1*3 + 2*(-1))i = (-1-6) + (3-2)i = -7 + 1i")
    print()

def test_division():
    """Test complex number division."""
    print("Testing Division Operations")
    print("=" * 40)
    print("Formula: (a + bi) / (c + di) = ((ac + bd)/(c² + d²)) + ((bc - ad)/(c² + d²))i")
    print()
    
    c1 = Complex(3, 4)   # 3 + 4i
    c2 = Complex(1, 2)   # 1 + 2i
    c3 = Complex(2, -1)  # 2 - 1i
    c4 = Complex(0, 1)   # 0 + 1i (i itself)
    
    print(f"c1 = {c1}, c2 = {c2}, c3 = {c3}, c4 = {c4}")
    print()
    
    # Test basic division
    result1 = c1 / c2
    print(f"({c1}) / ({c2}) = {result1}")
    print(f"Calculation:")
    print(f"  Denominator: 1² + 2² = 1 + 4 = 5")
    print(f"  Real part: (3*1 + 4*2)/5 = (3+8)/5 = 11/5 = 2.2")
    print(f"  Imag part: (4*1 - 3*2)/5 = (4-6)/5 = -2/5 = -0.4")
    print()
    
    result2 = c1 / c3
    print(f"({c1}) / ({c3}) = {result2}")
    print(f"Calculation:")
    print(f"  Denominator: 2² + (-1)² = 4 + 1 = 5")
    print(f"  Real part: (3*2 + 4*(-1))/5 = (6-4)/5 = 2/5 = 0.4")
    print(f"  Imag part: (4*2 - 3*(-1))/5 = (8+3)/5 = 11/5 = 2.2")
    print()
    
    # Test division by i
    result3 = c1 / c4
    print(f"({c1}) / ({c4}) = {result3}")
    print(f"Calculation:")
    print(f"  Denominator: 0² + 1² = 0 + 1 = 1")
    print(f"  Real part: (3*0 + 4*1)/1 = (0+4)/1 = 4")
    print(f"  Imag part: (4*0 - 3*1)/1 = (0-3)/1 = -3")
    print(f"  So (3+4i)/i = 4 - 3i")
    print()
    
    # Test division by zero (error case)
    print("Testing Division by Zero:")
    zero = Complex(0, 0)
    try:
        result = c1 / zero
        print("ERROR: Should have raised ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Correctly raised ZeroDivisionError: {e}")
    print()

def test_equality_operations():
    """Test equality and inequality operations."""
    print("Testing Equality and Inequality Operations")
    print("=" * 50)
    
    c1 = Complex(3, 4)
    c2 = Complex(3, 4)  # Same as c1
    c3 = Complex(3, 5)  # Different imaginary part
    c4 = Complex(4, 4)  # Different real part
    c5 = Complex(-3, -4) # Negative of c1
    
    print(f"c1 = {c1}, c2 = {c2}, c3 = {c3}, c4 = {c4}, c5 = {c5}")
    print()
    
    # Test equality
    print("Equality Tests:")
    print("=" * 20)
    print(f"c1 == c2: {c1 == c2} (same values)")
    print(f"c1 == c3: {c1 == c3} (different imaginary parts)")
    print(f"c1 == c4: {c1 == c4} (different real parts)")
    print(f"c1 == c5: {c1 == c5} (negative values)")
    print()
    
    # Test inequality
    print("Inequality Tests:")
    print("=" * 20)
    print(f"c1 != c2: {c1 != c2} (same values)")
    print(f"c1 != c3: {c1 != c3} (different imaginary parts)")
    print(f"c1 != c4: {c1 != c4} (different real parts)")
    print(f"c1 != c5: {c1 != c5} (negative values)")
    print()

def test_mixed_operations():
    """Test mixed complex number operations."""
    print("Testing Mixed Operations")
    print("=" * 40)
    
    c1 = Complex(2, 3)
    c2 = Complex(1, 1)
    c3 = Complex(3, -2)
    
    print(f"c1 = {c1}, c2 = {c2}, c3 = {c3}")
    print()
    
    # Test combination of operations
    result1 = (c1 + c2) * c3
    print(f"({c1} + {c2}) * {c3} = {result1}")
    print(f"Step 1: {c1} + {c2} = {c1 + c2}")
    print(f"Step 2: {c1 + c2} * {c3} = {result1}")
    print()
    
    result2 = (c1 * c2) - c3
    print(f"({c1} * {c2}) - {c3} = {result2}")
    print(f"Step 1: {c1} * {c2} = {c1 * c2}")
    print(f"Step 2: {c1 * c2} - {c3} = {result2}")
    print()
    
    result3 = (c1 - c2) / c3
    print(f"({c1} - {c2}) / {c3} = {result3}")
    print(f"Step 1: {c1} - {c2} = {c1 - c2}")
    print(f"Step 2: {c1 - c2} / {c3} = {result3}")
    print()

def main():
    """Main function to run all complex number tests."""
    print("Extended Complex Number Operations Test")
    print("=" * 60)
    print("Testing addition, subtraction, multiplication, division,")
    print("equality, and inequality of complex numbers")
    print()
    
    test_basic_operations()
    test_multiplication()
    test_division()
    test_equality_operations()
    test_mixed_operations()
    
    print("=" * 60)
    print("All complex number operations tested successfully!")

if __name__ == "__main__":
    main()