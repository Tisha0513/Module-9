class Cat:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def info(self):
        print("I am a cat. My name is " + self.name + " and I am " + str(self.age) + " years old")

    # Method
    def make_sound(self):
        print("Meow")


class Dog:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def info(self):
        print("I am a dog. My name is " + self.name + " and I am " + str(self.age) + " years old")

    # Method
    def make_sound(self):
        print("Woof")


# Object creation
catobj = Cat("Oreo", "1.5")
dogobj = Dog("Ralph", "3")

# Iterating through objects
for animal in (catobj, dogobj):
    animal.info()
    animal.make_sound()
