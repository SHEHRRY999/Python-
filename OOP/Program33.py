class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print(self.role, " ", self.dept, " ", self.salary)
class Engineer(Employee):
    def __init__(self, role, dept, salary, name, age):
        super().__init__(role, dept, salary)
        self.name = name
        self.age = age
    
engineer1 = Engineer("Engineer", "IT", 450000, "Shehryar", 23)
engineer1.showDetails()