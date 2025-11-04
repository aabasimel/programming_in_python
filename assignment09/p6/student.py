# student.py
# CTMS-14
# a9 p6.py
# Ahmed Abasimel
# aabasimel@constructor.university

class Student:
    def __init__(self, name, quiz1, quiz2, quiz3, age):
        print("Constructor being called")
        self.name = name
        self.quiz1 = quiz1
        self.quiz2 = quiz2
        self.quiz3 = quiz3
        self.age = age  # store age

    # Name methods
    def setName(self, new_name):
        self.name = new_name

    # Age methods
    def setAge(self, new_age):
        self.age = new_age

    def getAge(self):
        return self.age

    def __str__(self):
        return (f"Student: {self.name}, Age: {self.age}, "
                f"Quiz1: {self.quiz1}, Quiz2: {self.quiz2}, Quiz3: {self.quiz3}")

    def __repr__(self):
        return (f"Student(name={self.name!r}, age={self.age}, quiz1={self.quiz1}, "
                f"quiz2={self.quiz2}, quiz3={self.quiz3})")
