class Robot:

    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    # Method to introduce the robot
    def introduce(self):
        print(f"Hello! My name is {self.name}.")
        print(f"I am model: {self.model}.")
        print(f"My purpose is {self.purpose}.")

# Create robot information
my_robot = Robot("BoogieBot", "TV-2027", "To help different students about Coding")

# Introduce the robot
my_robot.introduce()