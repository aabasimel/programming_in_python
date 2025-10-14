# CTMS-14
# a6 p8.py
# Ahmed Abasimel
# aabasimel@constructor.university


def overlapping(lst1:list, lst2:list)->bool:
    for num in lst1:
        if num in lst2:
            return True
    return False

list1=[]
while True:
    number= int(input("Enter a number for list1 (negative to stop): "))
    if number <0:
        break
    list1.append(number)
list2=[]
while True:
    number= int(input("Enter a number for list2 (negative to stop): "))
    if number <0:
        break
    list2.append(number)

result = overlapping(list1, list2)
print(result)