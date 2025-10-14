# CTMS-14
# a4 p1.py
# Ahmed Abasimel
# aabasimel@constructor.university

# Function to convert gallons and cups to liters
def to_liter(gallon, cup):
    GALLON_TO_LITER = 3.7854
    CUP_TO_LITER = 0.2366
    return (gallon * GALLON_TO_LITER) + (cup * CUP_TO_LITER)

cup = float(input("Enter volume in cups: "))
gallon = float(input("Enter volume in gallons: "))

total_liters = to_liter(gallon, cup)

print("Total volume in liters:", total_liters)
