# CTMS-14
# a8 p1.py
# Ahmed Abasimel
# aabasimel@constructor.university

start = float(input("Enter start length in inches: "))
end = float(input("Enter end length in inches: "))
step = float(input("Enter step size in inches: "))

# Print table header
print(f"{'inch':<10}{'cm':<10}")

length = start
while length <= end:
    cm = length * 2.54
    print(f"{length:<10.1f}{cm:<10.1f}")
    length += step
