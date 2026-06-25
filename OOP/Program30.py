class Student:
    makrs1 = None
    marks2 = None
    marks3 = None
    name = None
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3

students = Student("Ali", 80, 90, 70)
print("The average marks of", students.name, "is", students.average())