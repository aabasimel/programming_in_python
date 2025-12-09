
class Person:
    def __init__(self, fname,lname,profession):
        self.fname = fname
        self.lname = lname
        self.profession = profession

    def __eq__(self, other):
        return (self.fname == other.fname and
                self.lname == other.lname 
               )
    def __lt__(self, other):
        if self.lname == other.lname:
            return self.fname < other.fname
        return self.lname < other.lname
    def __gt__(self, other):
        return (self.lastname, self.firstname) > (other.lastname, other.firstname)

    def __str__(self):
        return f"{self.fname} {self.lname}"