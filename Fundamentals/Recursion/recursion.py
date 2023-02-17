# 2/15/2023
# ---SoloLearn---
"""
Recursion is a very important concept in functional programming. 

The fundamental part of recursion is self-reference -- functions calling themselves. 
It is used to solve problems that can be broken up into easier sub-problems of the same type.

A classic example of a function that is implemented recursively is the 
factorial function, which finds the product of all positive integers below a specified number. 

For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). To implement this recursively, 
notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. Generally, n! = n * (n-1)!. 

Furthermore, 1! = 1. This is known as the base case, as it can be calculated without 
performing any more factorials. 

Below is a recursive implementation of the factorial function.
"""

def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)

print(factorial(5))

"""
The base case acts as the exit condition of the recursion.
Not adding a base case results in infinite function calls, crashing the program.
"""

"""
Recursion can also be indirect. One function can call a second, which calls the first, 
which calls the second, and so on. This can occur with any number of functions.
"""
def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)

print(is_odd(17))
print(is_even(2))

"""
The given code defines a recursive function convert(), which needs to convert its argument 
from decimal to binary.

However, the code has an error. 
Fix the code by adding the base case for the recursion, then take a number from user input and 
call the convert() function, to output the result.

Sample Input:
8

Sample Output:
1000
"""

num = int(input())
def convert(num):
    if num == 0:
        return 0
    else:
        return (num % 2 + 10 * convert(num // 2)) 

print(convert(num))

"""
What is the result of this code?
"""

def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))

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
# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

