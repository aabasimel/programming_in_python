# CTMS-14
# a10 p1.py
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

def main():
    test_equality()
    test_inequality()
    test_less_than()
    test_less_than_or_equal()
    test_greater_than()
    test_greater_than_or_equal()

if __name__ == "__main__":
    main()