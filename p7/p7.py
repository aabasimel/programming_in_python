# CTMS-14
# a6 p7.py
# Ahmed Abasimel
# aabasimel@constructor.university

numbers = []

while True:
    value = int(input("Enter a number (0 to stop): "))
    if value ==0:
        break
    numbers.append(value)
if numbers:
    max_value = max(numbers)
    min_value = min(numbers)
    print(f'Maximum: {max_value}')
    print(f'Minimum: {min_value}')
else:
    print("No numbers were entered.")