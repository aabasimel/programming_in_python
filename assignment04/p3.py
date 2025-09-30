# CTMS-14
# a4 p3.py
# Ahmed Abasimel
# myemail@constructor.university


while True:
    ch = input("Enter an uppercase letter: ")
    if len(ch)==1 and ch.isupper():
        break
    else:
        print("It needs to be a single uppercaseletter(A-Z)")


while True:
    try:
        n=int(input("Enter a number (0-32): "))
        if 0<=n<=32:
            break
        else:
            print("Number must be between 0 and 32")
    except ValueError:
        print("Please enter a valid integer")


for i in range(n+1):
    print(chr(ord(ch)+i))


    


