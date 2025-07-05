class Parrot:

    species = "bird"

    #instance attributes
    def __init__(self, name,age):
        self.name = name
        self.age = age

        #instance method
        def sing(self, song):
            return "{} sings {}".format(self.name, song)

            #method
            def dance(self):
                return "{} is dancing".format(self.name)

obj = Parrot("Christof", 7)

print("{} is a {} and is {} years old".format(obj.name,obj.species,obj.age))

print(obj.sing("Happy"))
print(obj.dance())