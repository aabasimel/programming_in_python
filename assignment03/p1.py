# CTMS-14
# a3 p1.py
# Ahmed Abasimel
# aabasimel@constructor.university

# Prompt user for input
minutes = int(input("Enter the number of minutes: "))

# Check if input is valid
if minutes < 0:
    print("Invalid input: minutes cannot be negative.")
else:
    hours = minutes // 60   # integer division for hours
    mins = minutes % 60     # remainder for minutes
    print(f"{minutes} minutes = {hours} hour(s) and {mins} minute(s).")
 