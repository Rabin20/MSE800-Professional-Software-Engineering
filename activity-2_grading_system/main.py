# main.py

from student import Student

# Create student objects
student1 = Student("Rabindra Joshi", "S001")
student2 = Student("Sita Sharma", "S002")

# Add grades to student1
student1.add_grade(85)
student1.add_grade(78)

# Add grades to student2
student2.add_grade(35)
student2.add_grade(42)

# Display student info
print("Student 1:")
student1.display_info()
print("\nStudent 2:")
student2.display_info()
