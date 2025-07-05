class Parrot:

    species = "bird"


    def __init__(self, name,age):
        self.name = name
        self.age = age

obj = Parrot("Christof", 7)

print("{} is a {} and is {} years old".format(obj.name,obj.species,obj.age))