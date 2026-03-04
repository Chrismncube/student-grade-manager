# student.py

class Student:
    def __init__(self, name, grades=None):
        if grades is None:
            grades = []
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return f"{self.name} | Grades: {self.grades} | Average: {self.calculate_average():.2f}"
