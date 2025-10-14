# CTMS-14
# a4 p9.py
# Ahmed Abasimel
# aabasimel@constructor.university



text = input("Enter the main text: ")
s = input("Enter the substring to be replaced: ")
r = input("Enter the replacing substring: ")

# Print the original text
print(f"\nOriginal text: {text}")

# Replace all occurrences of s with r
new_text = text.replace(s, r)

# Print the modified text
print(f"After replacing: {new_text}")