# 2/18/2023
# ---SoloLearn---
"""
Class Methods

Methods of objects we've looked at so far are called by an instance of a class, 
which is then passed to the self parameter of the method.

Class methods are different -- they are called by a class, which is passed to the cls parameter of the method. 

A common use of these are factory methods, which instantiate an instance of a class, using different parameters 
than those usually passed to the class constructor. 

Class methods are marked with a classmethod decorator.
"""

'''
new_square is a class method and is called on the class, rather than on an instance of the class. 
It returns a new object of the class cls.

Technically, the parameters self and cls are just conventions; 
they could be changed to anything else. However, they are universally followed, 
so it is wise to stick to using them.

This code defines a Rectangle class with an __init__ method to initialize the width and height of the rectangle,
 a calculate_area method to calculate the area of the rectangle, and a class method called new_square.

 The new_square method is a special type of method that is decorated with the @classmethod decorator, 
 which allows the method to be called on the class itself rather than on an instance of the class. 
 This method takes a side_length parameter, which represents the length of each side of the square, 
 and creates a new instance of the Rectangle class with side_length as both the width and height of the 
 rectangle.

 In the main code, the new_square method is called on the Rectangle class with an argument of 5, 
 which creates a new square with side length 5. The calculate_area method is then called on this square to 
calculate and print the area of the square.
'''

'''How do we create a class Rectangle?'''
class Rectangle:
  '''How do we initialize the class Rectangle with the parameters width and height?'''
  def __init__(self, width, height):
    self.width = width
    self.height = height
  '''How do we create a method that calculates the Rectangle's area?'''
  def calculate_area(self):
    return self.width * self.height
  '''How do we create a class method that makes a square?'''
  @classmethod
  def new_square(cls, side_length):
    return cls(side_length, side_length)

rectangle = Rectangle(5, 10)
print("Rectangle Area: ", rectangle.calculate_area())
square = Rectangle.new_square(5)
print("Square Area: ", square.calculate_area())

'''
Static Methods 
Static methods are similar to class methods, except they don't receive any additional arguments; 
they are identical to normal functions that belong to a class. 

They are marked with the staticmethod decorator.


In this code, we define a Pizza class with an __init__ method that takes a list of toppings as an argument 
and assigns it to the toppings attribute of the object.

We also define a staticmethod called validate_topping that takes a topping argument and raises a ValueError 
if it is equal to "pineapple", or returns True otherwise.

In the main code, we create a list of ingredients and use the built-in all function to check if all the 
ingredients are valid by calling the validate_topping method for each ingredient. If all the toppings are valid, 
we create a new Pizza object with the ingredients list. If not, the ValueError raised by the validate_topping 
method will propagate up and the Pizza object will not be created.
'''
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True

ingredients = ["cheese", "onions", "spam"]
ingredients_2 = "pineapple"
if all(Pizza.validate_topping(i) for i in ingredients):
  pizza = Pizza(ingredients) 

pizza = Pizza(ingredients)
print(pizza.validate_topping(ingredients))
# print(pizza.validate_topping(ingredients_2))

'''
The given code takes 2 numbers as input and calls the static area() method of the Shape class, 
to output the area of the shape, which is equal to the height multiplied by the width.

To make the code work, you need to define the Shape class, and the static area() method, which should return
the multiplication of its two arguments.

Use the @staticmethod decorator to define a static method.
'''

#your code goes here
class Shape:
  def __init__(self, w, h):
    self.width = w
    self.height = h

  @staticmethod
  def area(w, h):
    return w * h

w = int(input())
h = int(input())

print(Shape.area(w, h))


# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

