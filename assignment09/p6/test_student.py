# test_student.py
# student.py
# CTMS-14
# a9 p6.py
# Ahmed Abasimel
# aabasimel@constructor.university

from student import Student

def main():
    # Create a student named John, age 20
    student = Student("John", 100, 95, 50, 20)
    print("Before changing name and age:")
    print(student)

    # Change the student's name to Jack
    student.setName("Jack")
    # Change the student's age to 21
    student.setAge(21)

    print("\nAfter changing name and age:")
    print(student)

    # Test getAge
    print("\nRetrieved age:", student.getAge())

if __name__ == "__main__":
    main()
