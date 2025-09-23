# CTMS-14
# a3 p5.py
# Ahmed Abasimel
# aabasimel@constructor.university

# Read a single character from the user
char = input("Enter a character: ")

# Check if input is a single character and alphabetic
if len(char) != 1 or not char.isalpha():
    print("Invalid input! Please enter a single alphabetic character.")
else:
    # Now check if it is lowercase
    if char.islower():
        print("The character is a lowercase alphabetic character")
    else:
        print("The character is NOT a lowercase alphabetic character")
