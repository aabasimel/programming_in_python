# CTMS-14
# a7 p8.py
# Ahmed Abasimel
# aabasimel@constructor.university


stack=[]

def push(num):
    stack.append(num)
    print(f'Pushing {num}')

def pop():
    if stack:
        elem=stack.pop()
        print(f'Popping element {elem}')
    else:
        print("Stack underflow")

def empty():
    print("Emptying stack")
    while stack:
        pop()
while True:
    command = input().strip().lower()
    
    if command == "s":  
        num = int(input().strip())
        push(num)
    
    elif command == "p":
        pop()
    
    elif command == "e":
        empty()
    
    elif command == "q":
        print("Good Bye!")
        break
    
    else:
        print("Invalid command")