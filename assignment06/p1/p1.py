# CTMS-14
# a6 p1.py
# Ahmed Abasimel
# aabasimel@constructor.university

with open("input.txt", "r") as fin:
    data=fin.read().strip()

c1,c2=data[0],data[1]

#computes the product of the ASCII values of c1 and c2
product = ord(c1) * ord(c2)

with open("output.txt", "w") as fout:
    fout.write(str(product)+"\n")


