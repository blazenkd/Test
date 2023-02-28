# 2/18/2023
# ---FreeCodeCamp---
"""
What are objects in python?

In Python, an object is an instance of a class. 
It is a self-contained entity that consists of data (or state) and associated behavior 
(or methods/functions) that operate on that data. 
Objects are created from classes, which are essentially blueprints or templates that define the 
properties and behavior of the objects.

In other words, objects are the basic building blocks of Python programs, and nearly everything in Python 
is an object. For example, strings, lists, and dictionaries are objects in Python, and so are custom 
classes that you create.
"""

"""
In this example, Car is a class and my_car is an object (also called an instance) of the Car class. 
my_car has attributes like make, model, and year, and can perform actions like start_engine().
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Starting the engine...")

my_car = Car("Toyota", "Camry", 2022)
print(my_car.make) # Output: Toyota
my_car.start_engine() # Output: Starting the engine...

'''
This code defines a PartyAnimal class with an instance variable x and a method called party. 
x is initialized to 0 when the class is defined.

An instance of the class is created and assigned to the variable an. 
The party method is called on an twice.

The party method increments the value of x by 2 and prints the updated value each time it is called. 
Therefore, this code would output:
'''
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()


'''
The dir() function returns a list of all the valid attributes and methods of the object that is passed as 
an argument.

In the case of print(dir(PartyAnimal())), it will print a list of all the valid attributes and methods 
for the PartyAnimal class.
'''
print(type(PartyAnimal()))
print(dir(PartyAnimal()))

# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

"""

"""
