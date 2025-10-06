"""Guessing Game"""

import random 
random.seed()
minval=1
maxval=50
r= random.randint(minval,maxval)
count=0
while True:
    guess=int(input("Enter your guess: "))
    count+=1
    if r==guess:
        print(f"You got it! (Try#{count})")
        break
    elif guess < r:
        print(f"Your guess is too small (Try#{count})")
    else:
        print(f"Your guess is too high (Try#{count})")
        
print("Bye")