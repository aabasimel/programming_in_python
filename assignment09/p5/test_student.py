# test_student.py
# CTMS-14
# a9 p5.py
# Ahmed Abasimel
# aabasimel@constructor.university

from student import Student

def main():
    # Create a student named John
    student = Student("John", 100, 95, 50)
    print("Before changing name:")
    print(student)

    # Change the student's name to Jack
    student.setName("Jack")
    print("\nAfter changing name:")
    print(student)

if __name__ == "__main__":
    main()
