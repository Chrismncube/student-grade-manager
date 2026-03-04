# main.py
from student import Student

students = []

# Example students
student1 = Student("Alice", [80, 90, 85])
student2 = Student("Bob", [70, 75, 80])
students.append(student1)
students.append(student2)

# Add a grade to a student
student1.add_grade(95)

# Print all student info
print("Student Grades Report:")
for s in students:
    print(s)

# Optional: add new student interactively
name = input("Enter new student name: ")
grades_input = input("Enter grades separated by commas: ")
grades = [int(g.strip()) for g in grades_input.split(",") if g.strip().isdigit()]
new_student = Student(name, grades)
students.append(new_student)

print("\nUpdated Student Report:")
for s in students:
    print(s)
