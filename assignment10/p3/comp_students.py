# CTMS-14
# comp_students.py
# Ahmed Abasimel
# aabasimel@constructor.university

from student import Student

def test_student_comparisons():
    """Test all comparison operations between Student objects."""
    print("Testing Student Class Comparisons")
    print("=" * 50)
    
    # Create test Student objects
    student1 = Student("Alice", 3)
    student2 = Student("Bob", 3)
    student3 = Student("Alice", 5)  # Same name as student1, different number of scores
    student4 = Student("Charlie", 3)
    
    student1.setScore(1, 85)
    student1.setScore(2, 90)
    student1.setScore(3, 78)
    
    student2.setScore(1, 92)
    student2.setScore(2, 88)
    student2.setScore(3, 95)
    
    student3.setScore(1, 85)
    student3.setScore(2, 90)
    student3.setScore(3, 78)
    student3.setScore(4, 82)
    student3.setScore(5, 91)
    
    student4.setScore(1, 76)
    student4.setScore(2, 84)
    student4.setScore(3, 79)
    
    print("Student Information:")
    print(f"Student 1: {student1}")
    print(f"Average: {student1.getAverage():.2f}, High Score: {student1.getHighScore()}")
    print()
    print(f"Student 2: {student2}")
    print(f"Average: {student2.getAverage():.2f}, High Score: {student2.getHighScore()}")
    print()
    print(f"Student 3: {student3}")
    print(f"Average: {student3.getAverage():.2f}, High Score: {student3.getHighScore()}")
    print()
    print(f"Student 4: {student4}")
    print(f"Average: {student4.getAverage():.2f}, High Score: {student4.getHighScore()}")
    print()
    
    # Test equality comparisons
    print("Equality Comparisons:")
    print("=" * 30)
    print(f"student1 == student2: {student1 == student2} (Alice == Bob)")
    print(f"student1 == student3: {student1 == student3} (Alice == Alice)")
    print(f"student2 == student4: {student2 == student4} (Bob == Charlie)")
    print()
    
    # Test inequality comparisons
    print("Inequality Comparisons:")
    print("=" * 30)
    print(f"student1 != student2: {student1 != student2} (Alice != Bob)")
    print(f"student1 != student3: {student1 != student3} (Alice != Alice)")
    print(f"student2 != student4: {student2 != student4} (Bob != Charlie)")
    print()
    
    # Test less than comparisons
    print("Less Than Comparisons:")
    print("=" * 30)
    print(f"student1 < student2: {student1 < student2} (Alice < Bob)")
    print(f"student2 < student1: {student2 < student1} (Bob < Alice)")
    print(f"student1 < student4: {student1 < student4} (Alice < Charlie)")
    print(f"student4 < student1: {student4 < student1} (Charlie < Alice)")
    print()
    
    # Test less than or equal comparisons
    print("Less Than or Equal Comparisons:")
    print("=" * 30)
    print(f"student1 <= student2: {student1 <= student2} (Alice <= Bob)")
    print(f"student1 <= student3: {student1 <= student3} (Alice <= Alice)")
    print(f"student2 <= student1: {student2 <= student1} (Bob <= Alice)")
    print()
    
    # Test greater than comparisons
    print("Greater Than Comparisons:")
    print("=" * 30)
    print(f"student1 > student2: {student1 > student2} (Alice > Bob)")
    print(f"student2 > student1: {student2 > student1} (Bob > Alice)")
    print(f"student4 > student1: {student4 > student1} (Charlie > Alice)")
    print(f"student1 > student4: {student1 > student4} (Alice > Charlie)")
    print()
    
    # Test greater than or equal comparisons
    print("Greater Than or Equal Comparisons:")
    print("=" * 30)
    print(f"student1 >= student2: {student1 >= student2} (Alice >= Bob)")
    print(f"student1 >= student3: {student1 >= student3} (Alice >= Alice)")
    print(f"student2 >= student1: {student2 >= student1} (Bob >= Alice)")
    print()
    
    # Test sorting students by name
    print("Sorting Students by Name:")
    print("=" * 30)
    students = [student2, student1, student4, student3]  # Bob, Alice, Charlie, Alice
    sorted_students = sorted(students)
    print("Original order: Bob, Alice, Charlie, Alice")
    print("Sorted order:")
    for i, student in enumerate(sorted_students, 1):
        print(f"  {i}. {student.getName()}")
    print()
    
    # Test edge cases
    print("Edge Cases:")
    print("=" * 30)
    student5 = Student("alice", 3)  # Lowercase 'a'
    print(f"student1 == student5: {student1 == student5} (Alice == alice)")
    print(f"student1 < student5: {student1 < student5} (Alice < alice)")
    print("Note: 'A' < 'a' in ASCII/Unicode, so Alice comes before alice")
    print()
    
    # Test with empty names
    student6 = Student("", 3)
    student7 = Student("Aaron", 3)
    print(f"student6 < student7: {student6 < student7} ('' < Aaron)")
    print(f"student6 == Student('', 5): {student6 == Student('', 5)}")

def main():
    """Main function to run student comparison tests."""
    print("Student Class Comparison Test Program")
    print("=" * 50)
    print("Comparing students based on lexicographical order of names")
    print("(Case-sensitive comparison using Python's string comparison)")
    print()
    
    test_student_comparisons()
    
    print("=" * 50)
    print("All comparison tests completed!")

if __name__ == "__main__":
    main()