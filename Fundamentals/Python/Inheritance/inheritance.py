# 2/17/2023
# ---SoloLearn---
"""
Inheritance provides a way to share functionality between classes. 

Imagine several classes, Cat, Dog, Rabbit and so on. Although they may differ in some ways 
(only Dog might have the method bark), they are likely to be similar in others 
(all having the attributes color and name). 

This similarity can be expressed by making them all inherit from a superclass Animal, 
which contains the shared functionality. 

To inherit a class from another class, put the superclass name in parentheses after the class name.
"""
class Animal: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

class Cat(Animal):
  def purr(self):
    print("Purr...")
        
class Dog(Animal):
  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

'''
A class that inherits from another class is called a subclass.

A class that is inherited from is called a superclass.

If a class inherits from another with the same attributes or methods, it overrides them. 
'''

class Wolf: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Grr...")

class Dog(Wolf):
  def bark(self):
    print("Woof")
        
husky = Dog("Max", "grey")
husky.bark()

''''''
class A:
  def method(self):
    print(1)

class B(A):
  def method(self):
    print(2)

B().method()

'''
The function super is a useful inheritance-related function that refers to the parent class. 
It can be used to find the method with a certain name in an object's superclass.
'''

class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)
    super().spam()
            
B().spam()

'''
You are making a drawing application, which has a Shape base class.

The given code defines a Rectangle class, creates a Rectangle object and calls its area() and perimeter() methods. 

Do the following to complete the program:
  1. Inherit the Rectangle class from Shape.
  2. Define the perimeter() method in the Rectangle class, printing the perimeter of the rectangle. 
'''

class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width*self.height)

class Rectangle(Shape):
    #your code goes here
    def perimeter(self):
      print(2*self.width + 2*self.height)
    

w = int(input())
h = int(input())

r = Rectangle(w, h)
r.area()
r.perimeter()

# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

