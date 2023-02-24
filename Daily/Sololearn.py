# 2/23/2023
# ---SoloLearn---
"""
Raising Exceptions 

You can throw (or raise) exceptions when some condition occurs. 
For example, when you take user input that needs to be in a specific format, you can throw an exception 
when it does not meet the requirements.
This is done using the raise statement.

You need to specify the type of the exception raised. In the code below, we raise a ValueError.
"""

# num = 102
# if num > 100:
#   raise ValueError
'''
How many exceptions will the following code result in?
'''

# try:
#   print(1 / 0)
# except ZeroDivisionError:
#   raise ValueError

'''
Exceptions can be raised with arguments that give detail about them.
This makes it easier for other developers to understand why you raised the exception.
'''
# name = "123"
# raise NameError("Invalid name!")

'''
You are making a program to post tweets. Each tweet must not exceed 42 characters.

Complete the program to raise an exception, in case the length of the tweet is more than 42 characters.
'''
tweet = input()

try:
  #your code goes here
  if len(tweet) > 42:
    raise Exception()
except:
    print("Error")
else:
    print("Posted")



# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

