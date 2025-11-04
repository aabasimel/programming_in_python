# test_rational.py
"""
This program uses the Rational class from rational.py
to compute 1/2 + 1/8 and print the result.
"""

from rational import Rational

def main():
    # Create two Rational number objects
    r1 = Rational(1, 2)
    r2 = Rational(1, 8)

    # Compute their sum
    r_sum = r1 + r2

    # Print the results
    print("First Rational:", r1)
    print("Second Rational:", r2)
    print("Sum:", r_sum)

if __name__ == "__main__":
    main()
