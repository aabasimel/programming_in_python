# CTMS-14
# a4 p.5py
# Ahmed Abasimel
# myemail@constructor.university



# Function to print rectangle
def print_rectangle(n, m, c):
    for i in range(n):          
        print(c * m)            

# Read input
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
c = input("Enter a character: ")

# Call the function
print_rectangle(n, m, c)
