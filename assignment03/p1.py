

def sum(n):
    total = 0
    while(n>0):
        d=n%10
        total+=d
        n=n//10
    return total

print(sum(123))