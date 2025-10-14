# CTMS-14
# a6 p2.py
# Ahmed Abasimel
# aabasimel@constructor.university

with open("numbers.txt", "r") as fin:
    numbers = fin.readlines()
    total= sum(int(num.strip()) for num in numbers)
  
print(total)

