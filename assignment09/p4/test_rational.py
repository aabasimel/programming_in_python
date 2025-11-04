from rational import Rational
"""
This program tests the Rational class from rational.py
by creating two Rational number objects entered from the keyboard,
then displaying their numerators, denominators, and their sum.
"""


def main():
    print("Enter the first rational number:")
    n1 = int(input("Numerator: "))
    d1 = int(input("Denominator: "))
    r1 = Rational(n1, d1)

    print("\nEnter the second rational number:")
    n2 = int(input("Numerator: "))
    d2 = int(input("Denominator: "))
    r2 = Rational(n2, d2)

    print(f"First Rational: {r1}")
    print(f"Numerator: {r1.getNumerator()}, Denominator: {r1.getDenominator()}")

    print(f"\nSecond Rational: {r2}")
    print(f"Numerator: {r2.getNumerator()}, Denominator: {r2.getDenominator()}")

    # Compute and print their sum
    r_sum = r1 + r2
    print(f"\nSum of both: {r_sum}")

if __name__ == "__main__":
    main()
