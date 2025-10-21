# CTMS-14
# a7 p1.py
# Ahmed Abasimel
# aabasimel@constructor.university

def longest_word(lst):
    return max(lst,key=len)

text=input("Enter a sentence: ")
words=text.split()

longest= longest_word(words)

print("The longest word is:", longest)
print("Length of the longest word:", len(longest))