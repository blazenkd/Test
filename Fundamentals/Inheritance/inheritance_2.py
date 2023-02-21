# 2/19/2023
# ---FreeCodeCamp---
"""
Object Lifecycle

Objects are created, used, and discarded
We have special blocks of code (methods) that get called
    # At the moment of creation (constructor)
    # At the moment of destruction (destructor)
Constructors are used a lot
Destructors are seldom used

"""

"""
This is an example of a class PartyAnimal which has a class variable x and an instance variable name.
The __init__() method is a constructor method that gets called when an instance of the class is created. 
In this case, it takes an argument nam which is used to set the instance variable name for each instance.

The party() method is used to increment the class variable x by 1 and print the current value of x along with 
the name of the instance.

In the example code, two instances of PartyAnimal class are created with names Quincy and Miya. 
Then, the party() method is called on each instance to increment the x value for each instance separately. 
The output shows the current x value for each instance after calling party() method.
"""
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()


'''
Inheritance

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called the "subclass" or "derived class") 
to be based on an existing class (called the "base class" or "parent class"), inheriting some or all of its attributes and behaviors. 
The subclass can then add new attributes and behaviors or override existing ones inherited from the parent class. 
This mechanism enables code reuse and modularity, as well as the creation of more specialized classes that share common features with other classes.
'''
# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

"""

"""
