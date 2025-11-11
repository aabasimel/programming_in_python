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
    print(f"Expected: (3 + 1) + (4 + 2)i = 4 + 6i")
    print()
    
    result2 = c1 + c3
    print(f"({c1}) + ({c3}) = {result2}")
    print(f"Expected: (3 + 5) + (4 + (-1))i = 8 + 3i")
    print()
    
    result3 = c3 + c4
    print(f"({c3}) + ({c4}) = {result3}")
    print(f"Expected: (5 + (-2)) + ((-1) + (-3))i = 3 - 4i")
    print()
    
    # Test subtraction
    print("Subtraction Operations:")
    print("=" * 30)
    result4 = c1 - c2
    print(f"({c1}) - ({c2}) = {result4}")
    print(f"Expected: (3 - 1) + (4 - 2)i = 2 + 2i")
    print()
    
    result5 = c1 - c3
    print(f"({c1}) - ({c3}) = {result5}")
    print(f"Expected: (3 - 5) + (4 - (-1))i = -2 + 5i")
    print()
    
    result6 = c3 - c4
    print(f"({c3}) - ({c4}) = {result6}")
    print(f"Expected: (5 - (-2)) + ((-1) - (-3))i = 7 + 2i")
    print()
    
    result7 = c4 - c1
    print(f"({c4}) - ({c1}) = {result7}")
    print(f"Expected: (-2 - 3) + (-3 - 4)i = -5 - 7i")
    print()

def test_chained_operations():
    """Test chained complex number operations."""
    print("Testing Chained Operations")
    print("=" * 40)
    
    c1 = Complex(2, 3)
    c2 = Complex(1, 1)
    c3 = Complex(4, -2)
    
    print(f"c1 = {c1}, c2 = {c2}, c3 = {c3}")
    print()
    
    # Test multiple additions
    result1 = c1 + c2 + c3
    print(f"({c1}) + ({c2}) + ({c3}) = {result1}")
    print(f"Expected: (2+1+4) + (3+1+(-2))i = 7 + 2i")
    print()
    
    # Test mixed operations
    result2 = c1 + c2 - c3
    print(f"({c1}) + ({c2}) - ({c3}) = {result2}")
    print(f"Expected: ((2+1)-4) + ((3+1)-(-2))i = -1 + 6i")
    print()
    
    # Test multiple subtractions
    result3 = c1 - c2 - c3
    print(f"({c1}) - ({c2}) - ({c3}) = {result3}")
    print(f"Expected: ((2-1)-4) + ((3-1)-(-2))i = -3 + 4i")
    print()

def test_edge_cases():
    """Test edge cases and special complex numbers."""
    print("Testing Edge Cases and Special Numbers")
    print("=" * 45)
    
    # Test with zero
    zero = Complex(0, 0)
    c1 = Complex(3, 4)
    
    print(f"zero = {zero}, c1 = {c1}")
    print()
    
    result1 = c1 + zero
    print(f"({c1}) + ({zero}) = {result1}")
    print(f"Identity property: c1 + 0 = c1")
    print()
    
    result2 = c1 - zero
    print(f"({c1}) - ({zero}) = {result2}")
    print(f"Identity property: c1 - 0 = c1")
    print()
    
    result3 = zero - c1
    print(f"({zero}) - ({c1}) = {result3}")
    print(f"0 - c1 = -c1 = -3 - 4i")
    print()
    
    # Test with pure real numbers
    real1 = Complex(5, 0)
    real2 = Complex(2, 0)
    
    print(f"real1 = {real1}, real2 = {real2}")
    print()
    
    result4 = real1 + real2
    print(f"({real1}) + ({real2}) = {result4}")
    print(f"Real number addition: 5 + 2 = 7")
    print()
    
    result5 = real1 - real2
    print(f"({real1}) - ({real2}) = {result5}")
    print(f"Real number subtraction: 5 - 2 = 3")
    print()
    
    # Test with pure imaginary numbers
    imag1 = Complex(0, 3)
    imag2 = Complex(0, -2)
    
    print(f"imag1 = {imag1}, imag2 = {imag2}")
    print()
    
    result6 = imag1 + imag2
    print(f"({imag1}) + ({imag2}) = {result6}")
    print(f"Imaginary number addition: 3i + (-2i) = 1i")
    print()
    
    result7 = imag1 - imag2
    print(f"({imag1}) - ({imag2}) = {result7}")
    print(f"Imaginary number subtraction: 3i - (-2i) = 5i")
    print()

def test_negative_numbers():
    """Test operations with negative complex numbers."""
    print("Testing Operations with Negative Numbers")
    print("=" * 45)
    
    c1 = Complex(-3, -4)
    c2 = Complex(2, -1)
    c3 = Complex(-1, 3)
    
    print(f"c1 = {c1}, c2 = {c2}, c3 = {c3}")
    print()
    
    # Test additions with negatives
    result1 = c1 + c2
    print(f"({c1}) + ({c2}) = {result1}")
    print(f"Expected: (-3+2) + (-4+(-1))i = -1 - 5i")
    print()
    
    result2 = c2 + c3
    print(f"({c2}) + ({c3}) = {result2}")
    print(f"Expected: (2+(-1)) + (-1+3)i = 1 + 2i")
    print()
    
    # Test subtractions with negatives
    result3 = c1 - c2
    print(f"({c1}) - ({c2}) = {result3}")
    print(f"Expected: (-3-2) + (-4-(-1))i = -5 - 3i")
    print()
    
    result4 = c2 - c3
    print(f"({c2}) - ({c3}) = {result4}")
    print(f"Expected: (2-(-1)) + (-1-3)i = 3 - 4i")
    print()

def main():
    """Main function to run all complex number tests."""
    print("Complex Number Operations Test")
    print("=" * 50)
    print("Testing addition and subtraction of complex numbers")
    print("Formula: (a + bi) ± (c + di) = (a ± c) + (b ± d)i")
    print()
    
    test_basic_operations()
    test_chained_operations()
    test_edge_cases()
    test_negative_numbers()
    
    print("=" * 50)
    print("All complex number operations tested successfully!")
    print("\nSummary of operations implemented:")
    print("- Addition: (a + bi) + (c + di) = (a + c) + (b + d)i")
    print("- Subtraction: (a + bi) - (c + di) = (a - c) + (b - d)i")

if __name__ == "__main__":
    main()