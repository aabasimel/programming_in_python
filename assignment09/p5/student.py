# CTMS-14
# a9 p5.py
# Ahmed Abasimel
# aabasimel@constructor.university

class Student:
    def __init__(self,name,quiz1,quiz2,quiz3):
        print("Constructor being called")
        self.name = name
        self.quiz1=quiz1
        self.quiz2 = quiz2
        self.quiz3 = quiz3
    
    def __str__(self):
        """Readable string representation of the student."""
        return (f"Student: {self.name}, Quiz1: {self.quiz1}, "
                f"Quiz2: {self.quiz2}, Quiz3: {self.quiz3}")

    def setName(self,new_name):
        self.name = new_name
