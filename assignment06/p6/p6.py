# CTMS-14
# a6 p6.py
# Ahmed Abasimel
# aabasimel@constructor.university

def histogram(lst):
    for num in lst:
        print('*' * num)  

n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    numbers.append(value)

histogram(numbers)
