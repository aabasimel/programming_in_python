# CTMS-14
# a6 p3.py
# Ahmed Abasimel
# aabasimel@constructor.university

filename = input("Enter the name of the text file: ")

try:
    with open(filename, "r") as file:
        line_number=1
        for line in file:
            line= line.strip()
            words=line.split()
            word_count= len(words)

            print(f"Line {line_number}: {word_count} words")
            line_number +=1
except FileNotFoundError:
    print(f"Error: The file {filename} was not found.")