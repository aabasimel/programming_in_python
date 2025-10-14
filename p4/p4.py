# CTMS-14
# a6 p4.py
# Ahmed Abasimel
# aabasimel@constructor.university

filename = input("Enter the name of the text file: ")

with open(filename, "r") as fin:
    data=fin.read().strip()


with open("copy.txt", "w") as fout:
    fout.write(data + "\n")