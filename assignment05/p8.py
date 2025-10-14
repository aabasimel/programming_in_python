# CTMS-14
# a4 p8.py
# Ahmed Abasimel
# aabasimel@constructor.university



data = "Python is a great programming language"

#This prints the list of words within the string
words_list=data.split()
print("a) List of words: ", words_list)





uppercase_data=data.upper()
print("b) Uppercase: ",uppercase_data)

position=data.find("programming")
print("c) Postion of 'programming': ", position)

replaced_data=data.replace('g', 'G')
print("d) After replacing 'g' with 'G': ", replaced_data)



