
# Read an integer number from the user
num = int(input("Enter a number: "))

# Check if the number is divisible by 11
if num % 11 == 0:  # % is the modulus operator; checks remainder
    print("The number is divisible by 11")  # Executed if remainder is 0
else:
    print("The number is not divisible by 11")  # Executed if remainder is not 0
