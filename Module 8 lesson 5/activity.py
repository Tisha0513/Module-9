# Parent class
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.idnumber)

# Child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.name = name
        self.idnumber = idnumber
        self.salary = salary
        self.post = post

    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.idnumber)
        print("Salary:", self.salary)
        print("Post:", self.post)

emp = Employee("Tisha", "EMP1093", 100000, "Manager")

emp.display()
