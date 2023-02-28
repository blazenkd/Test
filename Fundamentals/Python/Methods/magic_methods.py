# 2/17/2023
# ---SoloLearn---
"""
Magic methods are special methods which have double underscores at the beginning and end of their names. 
They are also known as dunders. 
So far, the only one we have encountered is __init__, but there are several others. 
They are used to create functionality that can't be represented as a normal method. 
One common use of them is operator overloading. 
This means defining operators for custom classes that allow operators such as + and * to be used on them.
An example magic method is __add__ for +. 

The __add__ method allows for the definition of a custom behavior for the + operator in our class.
As you can see, it adds the corresponding attributes of the objects and returns a new object, 
containing the result.
Once it's defined, we can add two objects of the class together.
"""
class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
third = Vector2D(8, 16)
result_1 = result + third
print(result_1.x)
print(result_1.y)

'''

More magic methods for common operators:

__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

The expression x + y is translated into x.__add__(y). 
However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called. 
There are equivalent r methods for all magic methods just mentioned.
'''

class SpecialString:
  def __init__(self, cont):
    self.cont = cont
    print(self.cont)

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
bye = SpecialString("Bye")
print(spam / hello)
print(spam / bye)

'''
Python also provides magic methods for comparisons.

__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

 If __ne__ is not implemented, it returns the opposite of __eq__. 

There are no other relationships between the other operators.

As you can see, you can define any custom behavior for the overloaded operators.
'''
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __gt__(self, other):
    for index in range(len(other.cont)+1):
      print(index)
      print(range(len(other.cont)+1))
      result = other.cont[:index] + ">" + self.cont
      print(other.cont[:index])
      print(self.cont)
      print(result)
      result += ">" + other.cont[index:]
      print(result)

spam = SpecialString("spam")
egg = SpecialString("egg")
spam > egg

'''
There are several magic methods for making classes act like containers.

__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions, 
and __int__, __str__, and the like, for converting objects to built-in types.


We have overridden the len() function for the class VagueList to return a random number.
The indexing function also returns a random item in a range from the list, based on the expression.
'''
import random

class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]

  def __len__(self):
    return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

'''
We are improving our drawing application.
Our application needs to support adding and comparing two Shape objects. 
Add the corresponding methods to enable addition + and comparison using the greater than > operator for the 
Shape class.

The addition should return a new object with the sum of the widths and heights of the operands, 
while the comparison should return the result of comparing the areas of the objects.

'''
class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width*self.height

    #your code goes here
    def __add__(self, other):
      new_width = self.width + other.width
      new_height = self.height + other.height
      return Shape(new_width, new_height)
      
    def __gt__(self, other):
      return self.area() > other.area()


w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)

   


# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

'''
In Python, __gt__ is a magic method used to define the behavior of the > (greater than) operator. 
When this method is implemented in a class, it is called when the > operator is used with an instance of that class.

The __gt__ method should take two arguments, self and other, and return a boolean value indicating whether self 
is greater than other. The __gt__ method is used to implement the comparison operations >, >=, <, and <=.

For example, let's say we have a class Rectangle that has length and width attributes, and we want to define the
behavior of the > operator for two rectangles. We could implement the __gt__ method in the following way:
'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __gt__(self, other):
        return (self.length * self.width) > (other.length * other.width)

rectangle = Rectangle(4, 5)
rectangle_2 = Rectangle(5, 6)
print(rectangle < rectangle_2)