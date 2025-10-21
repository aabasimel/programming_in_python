# CTMS-14
# a7 p5.py
# Ahmed Abasimel
# aabasimel@constructor.university

# Collect integers from the user until a negative number is entered
elements = []

while True:
    n = int(input("Enter an integer (negative to stop): "))
    if n < 0:
        break
    elements.append(n)

tup = tuple(elements)

# Reverse the tuple
reversed_tup = tup[::-1]

# Print the reversed tuple
print("Reversed tuple:", reversed_tup)
