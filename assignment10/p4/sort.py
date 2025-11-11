# CTMS-14
# comp_students_shuffle_sort.py
# Ahmed Abasimel
# aabasimel@constructor.university

from student import Student
import random

def create_10_students():
    """Create 10 students with different names and scores."""
    print("Creating 10 Students")
    print("=" * 40)
    
    # List of diverse student names
    names = [
        "Alice", "Bob", "Charlie", "Diana", "Eve",
        "Frank", "Grace", "Henry", "Ivy", "Jack"
    ]
    
    students = []
    
    # Create 10 students with random scores
    for i, name in enumerate(names):
        # Each student has between 3-5 test scores
        num_scores = random.randint(3, 5)
        student = Student(name, num_scores)
        
        # Set random scores between 60-100
        for j in range(1, num_scores + 1):
            score = random.randint(60, 100)
            student.setScore(j, score)
        
        students.append(student)
        print(f"Created {student.getName()}: {num_scores} scores, Average: {student.getAverage():.2f}")
    
    print()
    return students

def display_students(students, title):
    """Display student information in a formatted way."""
    print(title)
    print("=" * 60)
    print(f"{'No.':<4} {'Name':<12} {'Scores':<20} {'Average':<8} {'High Score':<10}")
    print("-" * 60)
    
    for i, student in enumerate(students, 1):
        scores = [student.getScore(j+1) for j in range(len(student._scores))]
        scores_str = " ".join(map(str, scores))
        print(f"{i:<4} {student.getName():<12} {scores_str:<20} {student.getAverage():<8.2f} {student.getHighScore():<10}")
    print()

def main():
    """Main function to demonstrate shuffling and sorting of students."""
    print("Student Shuffling and Sorting Demonstration")
    print("=" * 60)
    print("Creating 10 students, shuffling them, and sorting in descending order")
    print("based on lexicographical ordering of names.\n")
    
    # Create 10 students
    students = create_10_students()
    
    # Display students in original order
    display_students(students, "Original Order of Students")
    
    # Shuffle the list of students
    print("Shuffling the list of students...")
    random.shuffle(students)
    print("List shuffled successfully!\n")
    
    # Display students after shuffling
    display_students(students, "After Shuffling - Random Order")
    
    # Sort students in descending order (reverse lexicographical order)
    print("Sorting students in descending order (reverse alphabetical)...")
    students.sort(reverse=True)
    print("Students sorted in descending order!\n")
    
    # Display students after sorting in descending order
    display_students(students, "After Sorting - Descending Order (Z to A)")
    
    # Additional demonstration: Show the actual order of names
    print("Name Order in Descending Sort:")
    print("-" * 30)
    for i, student in enumerate(students, 1):
        print(f"{i}. {student.getName()}")
    print()
    
    # Demonstrate that we can also sort in ascending order
    print("Sorting students in ascending order (alphabetical)...")
    students.sort()  # This is the same as students.sort(reverse=False)
    print("Students sorted in ascending order!\n")
    
    # Display students after sorting in ascending order
    display_students(students, "After Sorting - Ascending Order (A to Z)")
    
    # Show the actual order of names in ascending order
    print("Name Order in Ascending Sort:")
    print("-" * 30)
    for i, student in enumerate(students, 1):
        print(f"{i}. {student.getName()}")
    print()
    
    # Demonstrate multiple shuffles and sorts
    print("Final Demonstration: Multiple Shuffles and Sorts")
    print("=" * 50)
    
    for round_num in range(1, 4):
        print(f"\nRound {round_num}:")
        print("-" * 20)
        
        # Shuffle
        random.shuffle(students)
        print(f"After shuffle: {[student.getName() for student in students]}")
        
        # Sort in descending order
        students.sort(reverse=True)
        print(f"After descending sort: {[student.getName() for student in students]}")
    
    print("\n" + "=" * 60)
    print("Demonstration completed successfully!")
    print("The sort() method works because we implemented the comparison")
    print("methods (__lt__, __gt__, etc.) in the Student class.")

if __name__ == "__main__":
    main()