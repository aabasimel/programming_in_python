
class Person: 
    def __init__(self, fname,lname,profession):
        self.fname = fname
        self.lname = lname
        self.profession = profession

p1 = Person("John", "Doe", "Developer")
print(p1.fname)