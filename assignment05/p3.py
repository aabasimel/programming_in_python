# CTMS-14
# a4 p3.py
# Ahmed Abasimel
# aabasimel@constructor.university


import math

def calculate_sphere_volume(radius):
    """
    Calculate the volume of a sphere given its radius.
    
    Parameters:
    radius (float): The radius of the sphere
    
    Returns:
    float: The volume of the sphere
    """
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

r = float(input("Enter the radius of the sphere: "))

# Calculate volume using the function
sphere_volume = calculate_sphere_volume(r)

print(f"The volume of a sphere with radius {r} is {sphere_volume}")