def substitute_vowels(str,ch):
    voles = 'aeiouAEIOU'
    
    for char in str:
        if char in voles:
            str = str.replace(char,ch)

    return str
    
string = input("Enter a string: ")
char = input("Enter a character to substitute vowels: ")    
result = substitute_vowels(string, char)
print("String after substitution:", result)