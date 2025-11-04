# student.py

class Student:
    def __init__(self, name, quiz1, quiz2):
        print("Constructor being called")
        self.name = name
        self.quiz1 = quiz1
        self.quiz2 = quiz2

    def __str__(self):
        return f"Student: {self.name}, Quiz 1: {self.quiz1}, Quiz 2: {self.quiz2}"


jenny = Student("Jenny", 95, 90)
steve = Student("Steve", 95, 90)
celine = Student("Celine", 95, 90)

print(jenny)
print(steve)
print(celine)
