# CTMS-14
# a7 p2.py
# Ahmed Abasimel
# aabasimel@constructor.university

dict = {
    "merry": "god",
    "christmas": "jul",
    "and": "och",
    "happy": "gott",
    "new": "nytt",
    "year": "\u00E5r"  
}

def translate(list_en):
    swedish_words=[]
    for word in list_en:
        translated=dict.get(word.lower(),word)
        swedish_words.append(translated)
    return swedish_words

english_greeting = input("Enter your Christmas greeting: ")

english_words=english_greeting.split()


swedish_translation = translate(english_words)
print("Swedish translation: ", " ".join(swedish_translation))

