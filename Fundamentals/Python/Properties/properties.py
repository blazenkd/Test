# 2/20/2023
# ---SoloLearn---
"""
Properties

# What are properties?

Properties provide a way of customizing access to instance attributes. They are created by putting the property
decorator above a method, which means when the instance attribute with the same name as the method is accessed,
the method will be called instead.

One common use of a property is to make an attribute read-only

# What are getters and setters?

Properties can also be set by defining setter/getter functions. The setter function sets the corresponding
property value. The getter gets the value. To define a setter, you need to use a decorator of the same name
as the property, followed by a dot and the setter keyword. The same applies to defining getter functions.
"""

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False
  
  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed
  
  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    if value:
      password = input("Enter the password: ")
      if password == "Sw0rdf1sh!":
        self._pineapple_allowed = value
      else:
        raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
'''
# Fill in the blanks to create an "isAdult" property.

This creates a "Person" class with an "age" attribute, and a read-only "isAdult" property that returns "True"
if the person is older than 18, and "False" otherwise. The "@property" decorator indicates that "isAdult" is
a property, rather than a method. Note that we don't need to call the "isAdult" method with parentheses,
like we would with a regular method - we can just access it as if it were an attribute of the object.

# Why does the getter method not need parentheses?

In Python, when you define a method in a class and decorate it with "@property", it is transformed into a 
getter method for a read-only attribute of the same name. When you access this attribute on an instance
of the class, you can do so without parentheses, because it behaves like a proeprty or a field, rather
than like a method that requires arguments.

This is a common design pattern in Python that allows you to expose class attributes to the outside world
in a way that looks like normal attribute access, while still allowing you to compute the attribute value
on the fly or perform additional logic whn the attribute is accessed.

# Why should we use different names for attributes and methods?

There is an issue with the code. The 'age' attribute and the 'age' property have the same name, which causes
an infinite recursion error when trying to get or set the 'age' property. This can be fixed by renaming one
of them.

'''

class Person:
  def __init__(self, age):
    self._age = int(age)

  @property
  def isAdult(self):
    if self._age > 18:
      return True
    else: 
      return False

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, value):
    if value:
      password = input("Enter the password: ")
      if password == "Ax13":
        self._age = value
      else:
        raise ValueError("Alert! Intruder!")

adult = Person(19)
print("Are you an adult? ", adult.isAdult)
# adult.isAdult = False
person = Person(30)
print(person.age)
# person.age = 28
print(person.age)

'''
We are improving our game and need to add an isAlive property, which returns True if the lives count is greater 
than 0.

Complete the code by adding the isAlive property.
'''
class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
    
    #your code goes here
    @property
    def isAlive(self):
      if self._lives > 0:
        return True
      else:
        return False

p = Player("Cyberpunk77", int(input()))
i = 1
while True:
    p.hit()
    print("Hit # " + str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
        break



# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

"""
In this example, the BankAccount class has a read-only property can_withdraw which returns a boolean value 
indicating whether the account balance is greater than 0. Once the BankAccount object is created, 
the can_withdraw property can be accessed like a regular attribute, but it cannot be set directly.
"""

class BankAccount:
  def __init__(self, balance):
    self._balance = balance

  @property
  def can_withdraw(self):
    return self._balance > 0

  @can_withdraw.setter
  def can_withdraw(self, balance):

    if balance:
      password = input("Enter the password: ")
      if password == "My_bank123":
        self._balance = balance
      else:
        raise ValueError("Alert! Intruder!")
  

account = BankAccount(100)
print(account.can_withdraw)  # Output: True
account.can_withdraw = 200
print(account.can_withdraw)
print(account._balance)

