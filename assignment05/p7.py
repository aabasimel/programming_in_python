# CTMS-14
# a4 p7.py
# Ahmed Abasimel
# aabasimel@constructor.university



s = input("Enter a string: ")

while True:
    try:
        a=int(input("Enter a starting index a: "))
        b=int(input("Enter ending index b: "))
        if a<0 or b<0:
            print(f"Error: Indices cannot be negative. Please try again.\n")
        elif a>len(s) or b>len(s):
            print(f"Error: Indices must be less than string length ({len(s)}). Please try again.\n")
        elif a>b:
            print(f"Error: starting index cannot be greater than ending. please try again\n")
        else:
            break
    except ValueError as e:
        print(f"Enter a valid integer {e}")
substring = s[a:b+1]  # Include both positions a and b
print(f"The sliced substring from position {a} to {b} is: '{substring}'")
    
    



