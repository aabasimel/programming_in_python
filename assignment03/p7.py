# CTMS-14
# a3 p7.py
# Ahmed Abasimel
# aabasimel@constructor.university

# Read an integer n (number of minutes)
n = int(input("Enter an integer >= 1: "))

# Initialize counter
i = 1

# Loop from 1 to n
while i <= n:
    # Determine singular/plural for minute
    minute_word = "minute" if i == 1 else "minutes"
    # Calculate seconds
    seconds = i * 60
    print(f"{i} {minute_word} = {seconds} seconds")
    # Increment counter
    i += 1
