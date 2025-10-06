# CTMS-14
# a4 p6.py
# Ahmed Abasimel
# aabasimel@constructor.university



def count_vowels(s):
    """
    Count the number of vowels in a given string.
    
    Parameters:
    s (str): The string to count vowels in
    
    Returns:
    int: Number of vowels in the string
    """
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in s:
        if char in vowels:
            count += 1
            
    return count

while True:
    text = input("Enter a string (or press Enter to quit): ")
    
    if text == "":
        print("Goodbye!")
        break
    
    vowel_count = count_vowels(text)
    print(f"Number of vowels: {vowel_count}\n")