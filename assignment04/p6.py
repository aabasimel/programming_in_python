# CTMS-14
# a4 p6.py
# Ahmed Abasimel
# myemail@constructor.university


# Function to print a frame
def print_frame(n, m, c):
    for i in range(n):  # loop over rows
        if i == 0 or i == n - 1:
            print(c * m)          # first or last row: full of c
        else:
            print(c + ' ' * (m - 2) + c)  # middle rows: c at edges, spaces in between

# Read input
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
c = input("Enter a character: ")

# Call the function
print_frame(n, m, c)
