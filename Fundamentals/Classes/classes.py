# 2/17/2023
# ---SoloLearn---
"""
The focal point of Object Oriented Programming (OOP) are objects, which are created using classes.

The class describes what the object will be, but is separate from the object itself. In other words, a class can 
be described as an object's blueprint, description, or definition.

You can use the same class as a blueprint for creating multiple different objects. 

Classes are created using the keyword class and an indented block, which contains class methods 
(which are functions). 

Below is an example of a simple class and its objects.

This code defines a class named Cat, which has two attributes: color and legs.
Then the class is used to create 3 separate objects of that class.
Tap Continue to learn more!
"""
class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)
print(felix.color)
'''

The __init__ method is the most important method in a class. 

This is called when an instance (object) of the class is created, using the class name as a function.

All methods must have self as their first parameter, although it isn't explicitly passed, Python adds the self 
argument to the list for you; you do not need to include it when you call the methods. Within a method definition,
self refers to the instance calling the method.

Instances of a class have attributes, which are pieces of data associated with them.

In this example, Cat instances have attributes color and legs. These can be accessed by putting a dot, and the 
attribute name after an instance. 

In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.

In the example above, the __init__ method takes two arguments and assigns them to the object's attributes. 
The __init__ method is called the class constructor.
'''

class Student:
  def __init__(self, name):
    self.name = name
test = Student("Bob")
print(test.name)

'''
Classes can have other methods defined to add functionality to them. 

Remember, that all methods must have self as their first parameter.

These methods are accessed using the same dot syntax as attributes.
'''
class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

'''
You are making a video game! The given code declares a Player class, with its attributes and an intro() method.

Complete the code to take the name and level from user input, create a Player object with the corresponding 
values and call the intro() method of that object.
'''
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

#your code goes here
# name = input("Enter Name: ")
# level = input("Enter Level: ")
# Player_1 = Player(name, level)
# print(Player_1.level)
# print(Player_1.name)
# Player_1.intro()


class Student:
  def __init__(self, name):
    self.name = name
  def sayHi(self):
    print("Hi from "+ self.name)
s1 = Student("Amy")
s1.sayHi()
# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

