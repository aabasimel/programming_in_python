# CTMS-14
# a4 p2.py
# Ahmed Abasimel
# myemail@constructor.university



# Problem 4.2 Next Characters

ch = input("Enter an uppercase letter: ")

if len(ch) != 1 or not ch.isupper():
    print("It needs to be an uppercase letter")
else:
    n = int(input("Enter a number: "))
    for i in range(n + 1): 
        print(chr(ord(ch) + i))
