# 2/22/2023
# ---SoloLearn---
"""
Exceptions

You have already seen exceptions in previous code. They occur when something goes wrong, due to incorrect
code or input. When an exception occurs, the program immediately stops.

The following code produces the ZeroDivisionError exception by trying to divide 7 by 0: 

An exception is an event, which occurs during the execution of a program that disrupts the normal flow of
the program.
"""

num1 = 7
num2 = 0
# print(num1/num2)

'''

Different exceptions are raised for different reasons. 

Common exceptions:

ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly; 
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.

Python has several other built-in exceptions, such as ZeroDivisionError and OSError. 
Third-party libraries also often define their own exceptions.
'''

# print("7" + 4)

'''
Exception Handling 


When an exception occurs, the program stops executing.

To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.

The try block contains code that might throw an exception. If that exception occurs, the code in the try 
block stops being executed, and the code in the except block is run. If no error occurs, the code in the 
except block doesn't run.

As the code produces a ZeroDivisionError exception, the code in the except block is run.
In the code below, the except statement defines the type of exception to handle (in our case, the 
ZeroDivisionError).
'''
# try:
#     num1 = 7
#     num2 = 0
#     print (num1 / num2)
#     print("Done calculation")
# except ZeroDivisionError:
#     print("An error occurred")
#     print("due to zero division")

'''
Example
'''
try:
  variable = 10
  print (10 / 2)
except ZeroDivisionError:
  print("Error")
print("Finished")

'''

A try statement can have multiple different except blocks to handle different exceptions.

Multiple exceptions can also be put into a single except block using parentheses, to have the except 
block handle all of them.

You can handle as many exceptions in the except statement as you need.
'''

try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")

'''
Example
'''

try:
  meaning = 42
  print(meaning / 0)
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")

'''
An except statement without any exception specified will catch all errors. 
These should be used sparingly, as they can catch unexpected errors and hide programming mistakes.
'''
try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred")

'''
Example

An ATM machine takes the amount to be withdrawn as input and calls the corresponding withdrawal method.

In case the input is not a number, the machine should output "Please enter a number".

Use exception handling to take a number as input, call the withdraw() method with the input as its 
argument, and output "Please enter a number", in case the input is not a number.


'''

# def withdraw(amount):
#    print(str(amount) + " withdrawn!")

# # n = input()
# try:
#     int(n)
#     withdraw(n)
# except ValueError:
#     print("Please enter a number")

# withdraw()

'''
Finally

After a try/except statement, a finally block can follow. It will execute after the try/except block, 
no matter if an exception occurred or not.

The finally block is useful, for example, when working with files and resources: it can be used to make 
sure files or resources are closed or released regardless of whether an exception occurs.
'''

try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")

'''
Example

What is the output of this code?
'''

# try:
#   print(1)
# except:
#   print(2)
# finally:
#   print(3)

'''
Else 

The else statement can also be used with try/except statements. 
In this case, the code within it is only executed if no error occurs in the try statement.
'''
# try:
#    print(1)
# except ZeroDivisionError:
#    print(2)
# else:
#    print(3)

# try:
#    print(1/0)
# except ZeroDivisionError:
#    print(4)
# else:
#    print(5)

'''
Example

You are making a digital menu to order food.

The menu is stored as a list of items.

Your program needs to take the index of the item as input and output the item name.
In case the index is not valid, you should output "Item not found".
In case the index is valid and the item name is output successfully, you should output 
"Thanks for your order".

Sample Input:
2

Sample Output:
Cheeseburger
Thanks for your order
'''

# menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']

# try:
#   index = int(input())
#   item = menu[index]
#   print(item)
# except:
#   print("Item not found")
# else:
#   print("Thanks for your order")

'''
Example
'''
try:
  print(1)
  print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)


# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

