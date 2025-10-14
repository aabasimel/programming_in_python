# CTMS-14
# a6 p5.py
# Ahmed Abasimel
# aabasimel@constructor.university

def add(lst,val):
    new_list = [val+x for x in lst]
    return new_list

def multiply (lst,val):
    new_list = [val*x for x in lst]
    return new_list

n= int(input("Enter a number: " ))
num_list = []
for i in range(n):
    lst=float(input("Enter a float number: "))
    num_list.append(lst)

added_list = add(num_list, 1.5)
multiplied_list = multiply(num_list, 5)

print("\nOriginal list:", num_list)
print("After adding 1.5:", added_list)
print("After multiplying by 5:", multiplied_list)