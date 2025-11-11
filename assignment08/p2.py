# CTMS-14
# a8 p2.py
# Ahmed Abasimel
# aabasimel@constructor.university


# Read input values from the user
start = float(input("Enter start length in inches: "))
step = float(input("Enter step size in inches: "))
end = float(input("Enter end length in inches: "))

# Open file for writing
with open("table.txt", "w") as file:
    # Write table header
    file.write(f"{'inch':<10}{'cm':<10}{'meter':>10}{'kilometer':>12}\n")

    length = start
    while length <=end:
        cm = length * 2.54
        meter = length * 0.0254
        kilometer = length * 0.0000254
        file.write(f"{length:<10.1f}{cm:<10.1f}{meter:>10.4f}{kilometer:>12.7f}\n")
        length += step