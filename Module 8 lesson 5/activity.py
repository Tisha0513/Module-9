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
        self.salary = salary
        self.post = post

        Person.__init__(self,name,idnumber)

    def display(Employee):
        print("ID Number:",Employee.idnumber)
        print("Salary:", Employee.salary)
        print("Post:", Employee.post)

emp = Employee("Tisha", "EMP1093", 100000, "Manager")

emp.display()