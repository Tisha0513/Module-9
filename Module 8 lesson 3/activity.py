class Student:
    grade = 11
    name = "Tisha"

    def introduction(self):
        print("Hello! I am", self.name)
        print("Hi! I am a student of grade", self.grade)

    ob = Student() #Accessing the class through object
    ob.introduction() #Accessing a function through object