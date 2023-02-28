# 2/14/2023
# ---SoloLearn---

"""
Decorators provide a way to modify functions using other functions. This is ideal when you 
need to extend the functionality of functions that you don't want to modify.
"""

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello World!")

decorated = decor(print_text)
decorated()

"""
We defined a function named decor that has a single parameter func. Inside decor, we
defined a nested function named wrap. The wrap function will print a string, then call func(),
and print another string.

The decor function returns the wrap function as its result.

We could say that the variable decorated is a decorated version of print_text -- it's 
print_text plus something

In fact, if we wrote a useful decorator we might want to replace print_text with the decorated
version altogether so we always get our "plus something" version of print_text.

This is done by re-assigning the variable that contains our function.
"""

print_text = decor(print_text)
print_text()

"""
What are decorators?
    - Functions that modify other functions.
"""

"""
In our previous example, we decorated our function by replacing the variable containing
the function with a wrapped version.
"""

def print_text():
    print("Hello World!!")
print_text = decor(print_text)
print_text()

"""
This pattern can be used at any time, to wrap any function. Python provides support to wrap
a function in a decorator by pre-pending the function definition with a decorator name and
the @ symbol. 

If we are defining a function we can "decorate" it with the @ symbol like:
"""

@decor
def print_text():
    print("Hello World!!!")
print_text()

"""
This will have the same result as the above code.

A single function can have multiple decorators.
"""

"""
Practice Problem:

You are working on an invoicing system. The system has an already defined invoice() function,
which takes the invoice nunber as argument and outputs it

You need to add a decorator for the invoice() function, that will print the invoice in the
following format:

Sample Input:
42

Sample Output:
***
INVOICE #42
***
END OF PAGE

The given code takes the invoice number as input and passes it to the invoice() function.

"""

def decor1(func):
    def wrap(num):
        print("***")
        func(num)
        print("***")
        print("END OF PAGE")
    return wrap

@decor1 
def invoice(num):
    print("INVOICE # +num")

invoice(input("Enter a number: "));

"""
Which statement can be used to achieve the same behavior as:

my_func = my_dec(my_func)

@my_dec
"""

# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

"""
To learn, I will create my own version and look for errors.
"""

def fancy(func):
    def glam():
        print("***")
        func()
        print("***")
    return glam

def kDrama():
    print("*W*")

fancified = fancy(kDrama)
fancified()

""" We can replace our old kDrama function with this new one. """

kDrama = fancy(kDrama)
kDrama()

""" So, we replaced our function (kDrama) with the variable containing the function with a 
wrapped version. """

def kDrama():
    print("*W*")
kDrama = fancy(kDrama)

""" So, I can use the @ symbol to easily "decorate" the kDrama function. """

@fancy
def kDrama():
    print("*W*")
kDrama()

""" """

def decor2(func):
    def wrap(favorite_kdrama):
        print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
        func(favorite_kdrama)
        print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
        print("Fighting!")
    return wrap

@decor2
def fav_kdrama(favorite_kdrama):
    print(f" {favorite_kdrama} is the best!")

fav_kdrama(input("Enter favorite K Drama: "));