# CTMS-14
# a3 p2.py
# Ahmed Abasimel
# aabasimel@constructor.university

# Mistake 1: Multiply a string with an integer value
s = input("Enter a string: ")        # e.g., "Hello"
i = int(input("Enter an integer: ")) # e.g., 3
print(s * i)  
# ✅ In Python, multiplying a string with an integer repeats the string.
# Example: "Hello" * 3 → "HelloHelloHello"
# So this does not cause an error — but might not be the "intended math".

# Mistake 2: Read two integers as strings and add them
a = input("Enter first integer: ")   
b = input("Enter second integer: ")  
print(a + b)  
#  Since we did NOT convert input() to int, both are strings.
# eg "2" + "3" = "23" (string concatenation, not numeric addition).

# Mistake 3: Multiply a string with a float value
t = input("Enter another string: ")     # e.g., "Hi"
f = float(input("Enter a float: "))     # e.g., 2.5
print(t * f)  
#  ERROR: Python only allows string * integer.
# Multiplying a string by float gives:
# TypeError: can't multiply sequence by non-int of type 'float'

