# CTMS-14
# a4 p8.py
# Ahmed Abasimel
# myemail@constructor.university



def convert(miles):
    # Conversion: 1 mile = 1.609344 km
    return miles * 1.609344

# Read input
miles = float(input("Enter distance in miles: "))

km = convert(miles)

print(f"{miles} miles is {km} kilometers")
