#import modules
from abc import ABC, abstractmethod

#create base class
class Animal:

    def move(self):
    pass

#sub classes
class Human(Animal):
    
    def move(self):
        print("I can walk and run")

class Dog(Animal):

    def move(self):
        print("I can bark")