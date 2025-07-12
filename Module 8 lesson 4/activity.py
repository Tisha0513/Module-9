class Employee:
    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # Destructor
    def __del__(self):
        print("Destructor called. Employee deleted.")

# Object creation
obj = Employee("Tasmia", "2908")


print("The employee id of " + obj.name + " is " + obj.id)

del obj
