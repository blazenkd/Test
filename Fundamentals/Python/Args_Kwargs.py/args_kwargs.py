# 2/16/2023
# ---SoloLearn---
"""
Python allows you to have functions with varying numbers of arguments.

Using *args as a function parameter enables you to pass an arbitrary number of 
arguments to that function. The arguments are then accessible as the tuple args 
in the body of the function.
"""

def function(named_arg, named_arg_2, *args):
  print((named_arg))
  print((named_arg_2))
  print((args))
function(1,2,3,4,5, "six")

"""
**kwargs (standing for keyword arguments) allows you to handle named arguments that 
you have not defined in advance.

The keyword arguments return a dictionary in which the keys are the argument names, 
and the values are the argument values.

The function my_func takes 2 required parameters x and y, as well as any number of 
additional positional and keyword arguments (*args and **kwargs).

When you call my_func(2, 3, 4, 5, 6, a=7, b=8), x is assigned to 2, y is assigned 
to 3, and the rest of the positional arguments 4, 5, 6 are packed into the args 
tuple.
The keyword arguments a=7 and b=8 are packed into the kwargs dictionary.

Then the function prints the values of args and kwargs.
"""

def my_func(x, y=7, *args, **kwargs):
  print(x)
  print(y)
  print(args)
  print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

"""
The given code defined a function called my_min(), which takes two arguments and 
returns the smaller one.

You need to improve the function, so that it can take any number of variables, 
so that the function call works.
"""
def my_min(x, y, *args):
  for arg in args:  
    if x < y and x < arg:
      return x
    elif y < x and y < arg:
      return y
    else:
      return arg

print(my_min(8, 13, 4, 42, 120, 7))

# Solution
def my_min_solution(*args):
  return min(args)
print(my_min_solution(8, 13, 4, 42, 120, 7))

# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

"""
In a Python function, the *args syntax is used to pass a variable number of 
arguments to the function. Inside the function, *args is treated as a tuple of the 
arguments, which can be accessed by indexing just like any other tuple.
"""

def my_function(*args):
    for arg in args:
        print(arg)
        
my_function(1, 2, 3)

"""
In the above example, *args is used to define a function that takes any number of 
arguments, which are then printed one at a time using a for loop.

When my_function is called with my_function(1, 2, 3), args is a tuple containing 
the values (1, 2, 3). The for loop in the function then iterates over the tuple 
and prints each argument.
"""

"""
kwargs

This function func() takes keyword arguments and prints the values corresponding to 
the "zero" and "a" keys of the kwargs dictionary passed to it.

This is because kwargs["zero"] is accessing the value of the "zero" key which is 8, 
kwargs["a"] is accessing the value of the "a" key which is 0, and kwargs is the 
dictionary containing all the keyword arguments passed to the function.

"""
def func(**kwargs):
  print(kwargs["zero"])
  print(kwargs["a"])
  print(kwargs)

func(a = 0, zero = 8)
"""
In this example, we've added a for loop to iterate over all the key-value pairs in 
kwargs and print out a message about each one. This can be useful for debugging and
for getting a better understanding of what's in kwargs.
"""
def func(**kwargs):
  print(kwargs["zero"])
  print(kwargs["a"])
  for key, value in kwargs.items():
    print(f"The value of {key} is {value}")

func(a=0, zero=8, foo="bar")