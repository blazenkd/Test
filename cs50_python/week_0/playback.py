'''
CS50 Python 2023
Week 0: playback.py
'''


'''
Task:

The problem that this code solves is to take a string input from the user and replace all spaces in the input
string with three dots ("..."). If the input string is empty or contains only whitespace characters, the program
returns the string "Empty". The code uses regular expressions (re module) to perform the substitution of spaces with dots
'''

import re   # import the regular expressions module

def playback(input_str):    # define a function called "playback" that takes a string argument called "input_str"
    if not input_str.strip():   # check if the input string is empty or contains only whitespace characters using the "strip" method
        return "Empty"    # if the input string is empty or contains only whitespace characters, return the string "Empty"
    return re.sub(" ", "...", input_str)   # use the "sub" method from the "re" module to replace all spaces in the input string with three dots

print(playback(input()))   # call the "playback" function with the user input and print the result to the console