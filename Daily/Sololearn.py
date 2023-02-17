# 2/16/2023
# ---SoloLearn---
"""
Python allows you to have functions with varying numbers of arguments.

Using *args as a function parameter enables you to pass an arbitrary number of 
arguments to that function. The arguments are then accessible as the tuple args 
in the body of the function.
"""

nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
print(nums)
nums = filter(lambda x: x > 1, nums)
nums = list(nums)
print(nums)
print(len(list(nums)))

"""
This code defines a function called power that takes two arguments, x and y. 
The function calculates the value of x raised to the power of y using a recursive 
approach.

The function first checks if y is equal to 0. If it is, the function returns 1, 
since any number raised to the power of 0 is 1. If y is not equal to 0, the 
function recursively calls itself with the same value of x and y-1.

Each time the function is called recursively, the value of y is decreased by 1, 
so eventually y will be equal to 0, and the function will return 1. In the meantime, 
each recursive call multiplies the current value of x with the result of the 
previous call.

Finally, the code calls the power function with arguments 2 and 3, which returns 
the result of 2 raised to the power of 3, which is 8. The result is printed to the 
console using the print function.
"""

def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
		
print(power(2, 3))

""" lambda """

a = (lambda x: x*(x+1))(6)
print(a)

""" 
The lambda function lambda x: x % 2 == 0 takes one argument x and returns True if 
x is even (i.e., if x % 2 == 0) and False otherwise.

The filter function takes a function (in this case, the lambda function) and an 
iterable (in this case, the nums list) as arguments, and returns an iterator that 
yields the elements of the iterable for which the function returns True.

The list function is used to convert the iterator returned by filter into a list.
"""

nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)

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

# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

