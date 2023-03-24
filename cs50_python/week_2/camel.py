'''
CS50 Python 2023
Week 2: camel.py
'''

'''
Task :

In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the
corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
'''

# Prompt the user for input
camel_case = input("Enter a variable name in camel case: ")

# Initialize an empty string to store the snake case version of the variable name
snake_case = ""

# Loop through each character in the camel case name
for i, char in enumerate(camel_case):
    # If the character is uppercase and not the first character, add an underscore before it
    if char.isupper() and i != 0:
        snake_case += "_"
    # Add the lowercase version of the character to the snake case name
    snake_case += char.lower()

# Output the snake case name
print("Snake case version: " + snake_case)