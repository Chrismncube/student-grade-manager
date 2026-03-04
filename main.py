from student import Student

students = {}

def add_student():
    name = input("Enter student name: ")
    students[name] = Student(name)

def add_grade():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))
    students[name].add_grade(grade)

def show_students():
    for student in students.values():
        print(student)

while True:
    print("\n1. Add Student")
    print("2. Add Grade")
    print("3. Show Students")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_grade()
    elif choice == "3":
        show_students()
    elif choice == "4":
        break
