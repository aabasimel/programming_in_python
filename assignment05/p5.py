text = input("Enter a string: ")

for i in range(len(text)):
    spaces = " " * i  
    print(spaces + text[i])


