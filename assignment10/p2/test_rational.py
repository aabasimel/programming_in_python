# CTMS-14
# a10 p2.py
# Ahmed Abasimel
# aabasimel@constructor.university



from rational import Rational

def test_equality():
    """Test the __eq__ method"""
    r1 = Rational(1, 2)
    r2 = Rational(2, 4)
    r3 = Rational(3, 6)
    r4 = Rational(2, 3)
    r5 = Rational(-1, 2)
    r6 = Rational(1, -2)

    assert r1 == r2
    assert r1 == r3
    assert not (r1 == r4)
    assert r5 == r6
    assert not (r1 == r5)
    print("test_equality passed!")


def test_inequality():
    """Test the __ne__ method"""
    r1 = Rational(1, 2)
    r2 = Rational(2, 4)
    r3 = Rational(3, 4)
    r4 = Rational(1, 3)
    r5 = Rational(0, 1)
    r6 = Rational(0, 5)

    assert not (r1 != r2)
    assert r1 != r3
    assert r1 != r4
    assert r3 != r4
    assert not (r5 != r6)
    assert r1 != r5
    print("test_inequality passed!")

def test_less_than():
    """Test the __lt__ method"""
    r1 = Rational(1, 2)  # 0.5
    r2 = Rational(3, 4)  # 0.75
    r3 = Rational(1, 3)  # ~0.333
    r4 = Rational(2, 4)  # 0.5
    r5 = Rational(-1, 2)  # -0.5
    r6 = Rational(-1, 4)  # -0.25

    assert r1 < r2
    assert r3 < r1
    assert not (r2 < r1)
    assert not (r1 < r4)
    assert r5 < r6
    assert r5 < r1
    assert not (r6 < r5)
    print("test_less_than passed!")

def test_less_than_or_equal():
    """Test the __le__ method"""
    r1 = Rational(1, 2)  # 0.5
    r2 = Rational(3, 4)  # 0.75
    r3 = Rational(1, 3)  # ~0.333
    r4 = Rational(2, 4)  # 0.5

    assert r1 <= r2
    assert r3 <= r1
    assert r1 <= r4
    assert not (r2 <= r1)
    assert r2 <= r2
    print("test_less_than_or_equal passed!")

def test_greater_than():
    """Test the __gt__ method"""
    r1 = Rational(1, 2)  # 0.5
    r2 = Rational(3, 4)  # 0.75
    r3 = Rational(1, 3)  # ~0.333
    r4 = Rational(2, 4)  # 0.5
    r5 = Rational(5, 1)  # 5.0
    r6 = Rational(10, 2)  # 5.0

    assert r2 > r1
    assert r1 > r3
    assert not (r1 > r4)
    assert not (r3 > r1)
    assert r5 > r1
    assert not (r5 > r6)
    print("test_greater_than passed!")

def test_greater_than_or_equal():
    """Test the __ge__ method"""
    r1 = Rational(1, 2)  # 0.5
    r2 = Rational(3, 4)  # 0.75
    r3 = Rational(1, 3)  # ~0.333
    r4 = Rational(2, 4)  # 0.5
    r5 = Rational(0, 1)  # 0
    r6 = Rational(1, 2)  # 0.5

    assert r2 >= r1
    assert r1 >= r3
    assert r1 >= r4
    assert not (r3 >= r1)
    assert r1 >= r1
    assert r6 >= r5
    assert r5 >= r5
    assert not (r5 >= r6)
    print("test_greater_than_or_equal passed!")

def test_arithmetic_operations():
    r1 = Rational(1, 2)  # 1/2 = 0.5
    r2 = Rational(2, 3)  # 2/3 ≈ 0.666
    r3 = Rational(3, 4)  # 3/4 = 0.75
    r4 = Rational(2, 4)  # 2/4 = 1/2 = 0.5

    # Test addition
    assert r1 + r2 == Rational(7,6)
    result_add1 = r1 + r2
    print(f"{r1} + {r2} = {result_add1} (expected: 7/6)")

    assert r1 + r4 == Rational(1,1)
    result_add2 = r1 + r4
    print(f"{r1} + {r4} = {result_add2} (expected: 1/1)")


    # Test substraction
    print("Subtraction:")
    result_sub1 = r2 - r1
    assert result_sub1 == Rational(1,6)
    print(f"{r2} - {r1} = {result_sub1} (expected: 1/6)")
    
    result_sub2 = r1 - r4
    assert result_sub2 == Rational(0,1)
    print(f"{r1} - {r4} = {result_sub2} (expected: 0/1)")
    
    result_sub3 = r3 - r2
    assert result_sub3 == Rational(1,12)
    print(f"{r3} - {r2} = {result_sub3} (expected: 1/12)")
    print()


    # Test multiplication
    print("Multiplication:")
    result_mul1 = r1 * r2
    assert result_mul1 == Rational(1,3)
    print(f"{r1} * {r2} = {result_mul1} (expected: 1/3)")
    
    result_mul2 = r1 * r4
    assert result_mul2 == Rational(1,4)
    print(f"{r1} * {r4} = {result_mul2} (expected: 1/2)")
    
    result_mul3 = r3 * r2
    assert result_mul3 == Rational(1,2)
    print(f"{r3} * {r2} = {result_mul3} (expected: 3/4)")
    print()

    # Test division
    print("Division:")
    result_div1 = r2 / r1
    assert result_div1 == Rational(4,3)
    print(f"{r2} / {r1} = {result_div1} (expected: 4/3)")
    
    result_div2 = r1 / r4       
    assert result_div2 == Rational(1,1)
    print(f"{r1} / {r4} = {result_div2} (expected: 1/1)")
    
    result_div3 = r3 / r2           
    assert result_div3 == Rational(9,8)
    print(f"{r3} / {r2} = {result_div3} (expected: 9/8)")
    print()


    print("Operations with Negative Numbers:")
    r5 = Rational(-1, 3)  # -1/3 ≈ -0.333
    r6 = Rational(2, -5)  # -2/5 = -0.4
    
    print(f"r5 = {r5}")
    print(f"r6 = {r6}")
    print()
    
    result_add_neg = r5 + r6
    print(f"{r5} + {r6} = {result_add_neg} (expected: -11/15)")
    
    result_sub_neg = r5 - r6
    print(f"{r5} - {r6} = {result_sub_neg} (expected: 1/15)")
    
    result_mul_neg = r5 * r6
    print(f"{r5} * {r6} = {result_mul_neg} (expected: 2/15)")
    
    result_div_neg = r5 / r6
    print(f"{r5} / {r6} = {result_div_neg} (expected: 5/6)")
    print()
    
    print("Division by Zero Test:")
    r_zero = Rational(0, 1)
    try:
        result = r1 / r_zero
        print(f"ERROR: Should have raised ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Correctly raised ZeroDivisionError: {e}")
    print()




    
    


    

def main():
    test_equality()
    test_inequality()
    test_less_than()
    test_less_than_or_equal()
    test_greater_than()
    test_greater_than_or_equal()
    test_arithmetic_operations()


if __name__ == "__main__":
    main()