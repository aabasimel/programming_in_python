# CTMS-14
# a4 p4.py
# Ahmed Abasimel
# myemail@constructor.university



# Computing Sum and Average

sum = 0
count=0
while True:
    n = int(input("Enter a number: "))
    if n == -9 or count>=10:
        break
    sum += n
    count+=1

print("The average is: ", sum/count)

    

    
    