# 2/18/2023
# ---SoloLearn---
"""
Data Hiding

A key part of object-oriented programming is encapsulation, which involves packaging of related variables and functions 
into a single easy-to-use object -- an instance of a class.

A related concept is data hiding, which states that implementation details of a class should be hidden, and a clean 
standard interface be presented for those who want to use the class. 

In other programming languages, this is usually done with private methods and attributes, which block external access 
to certain methods and attributes in a class.

The Python philosophy is slightly different. It is often stated as "we are all consenting adults here", meaning that 
you shouldn't put arbitrary restrictions on accessing parts of a class. Hence there are no ways of enforcing that a 
method or attribute be strictly private. 

However, there are ways to discourage people from accessing parts of a class, such as by denoting that it is an 
implementation detail, and should be used at their own risk.
"""

"""
Weakly private methods and attributes have a single underscore at the beginning.

This signals that they are private, and shouldn't be used by external code. However, it is mostly only a convention, 
and does not stop external code from accessing them.

In the code above, the attribute _hiddenlist is marked as private, but it can still be accessed in the 
outside code.

The __repr__ magic method is used for string representation of the instance.
"""
class Queue:
  def __init__(self, contents):
    self._hiddenlist = list(contents)

  def push(self, value):
    self._hiddenlist.insert(0, value)
   
  def pop(self):
    return self._hiddenlist.pop(-1)

  def __repr__(self):
    return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)  

'''
This code defines a Queue class with a private variable _hiddenlist. 
The constructor takes an argument contents and creates a new list from it, which is assigned to the 
private variable _hiddenlist. 
The class has methods to push and pop elements from the queue using the insert() and pop() methods of 
the _hiddenlist.

The __repr__() method is a special method in Python classes that is called when the object needs to be 
represented as a string. In this case, it returns a string that represents the class and its private 
variable _hiddenlist.

In the example code, an instance of the Queue class is created with a list [1, 2, 3]. 
The push() method is called to add a value 0 to the beginning of the queue. 
The pop() method is then called to remove the last element from the queue. 
Finally, the private variable _hiddenlist is printed, which is [0, 1, 2].
'''

'''
Strongly private methods and attributes have a double underscore at the beginning of their names. 
This causes their names to be mangled, which means that they can't be accessed from outside the class. 

The purpose of this isn't to ensure that they are kept private, but to avoid bugs if there are subclasses 
that have methods or attributes with the same names.

Name mangled methods can still be accessed externally, but by a different name. 
The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.

Basically, Python protects those members by internally changing the name to include the class name.
'''

class Spam:
  __egg = 7
  def print_egg(self):
    print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
# print(s.__egg)

'''
The code defines a class Spam with a private class attribute __egg set to 7 and a method print_egg 
that prints the value of __egg. When an instance of Spam is created and print_egg is called, 
it prints the value of __egg, which is 7.

However, the code also tries to access the private attribute __egg outside of the class using 
s._Spam__egg and s.__egg. The first one is the correct way to access private attributes, 
but the second one raises an AttributeError because __egg is a private attribute and cannot be accessed 
directly from outside the class. The double underscore prefix on __egg causes the name to be "mangled" 
by the interpreter, which means it is modified to _Spam__egg to make it harder to access from outside 
the class.

'''

'''

We are working on a game. 
Our Player class has name and private _lives attributes.

The hit() method should decrease the lives of the player by 1. 
In case the lives equal to 0, it should output "Game Over".

Complete the hit() method to make the program work as expected.

The code creates a Player object and calls its hit() method multiple times.
'''

class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        #your code goes here
        self._lives -= 1
        if self._lives == 0:
          print("Game Over")
        

p = Player("Cyberpunk77", 3)
p.hit()
p.hit()
p.hit()

'''
How would the attribute __a of the class b be accessed from outside the class?

  The attribute __a of class b is a private attribute, and it's not intended to be accessed from outside 
  the class. However, if you really need to access it for some reason, you can do it using the name 
  mangling syntax: _classname__attribute. So to access __a of class b from outside the class, you would 
  use _b__a.

  However, it's generally not a good idea to access private attributes from outside the class, as it can 
  break encapsulation and make your code harder to maintain. It's better to use public methods or 
  attributes to access the information you need.

'''

# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

'''
In this example, the MyClass has a private attribute __a which can't be accessed directly from outside 
the class. To access this attribute, a getter method get_a() has been defined which returns the 
value of __a. However, if we try to access the attribute directly using obj.__a, it raises an 
AttributeError as it's not allowed.
'''
class MyClass:
    def __init__(self, a):
        self.__a = a
    
    def get_a(self):
        return self.__a

obj = MyClass(10)
print(obj.get_a()) # outputs 10
print(obj.__a) # raises AttributeError