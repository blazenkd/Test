'''
CS50 Python 2023
Week 1: interpreter.py
'''

'''
Task :

In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and
then calculates and outputs the result as a floating-point value formatted to one decimal place.
Assume that the user’s input will be formatted as x y z, with one space between x and y
and one space between y and z, wherein:

    # x is an integer
    # y is +, -, *, or /
    # z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.
'''


# Prompt the user for an expression
user_input = input("Expression: ")

# Split the expression into three variables: x, y (operator), z
x, y, z = user_input.split()

# Define a dictionary to map operators to functions
# The keys are the operators, and the values are lambda functions that
# take two arguments and return the result of the corresponding operation
operator_dict = {
    '+': lambda x, z: x + z,  # Addition
    '-': lambda x, z: x - z,  # Subtraction
    '*': lambda x, z: x * z,  # Multiplication
    '/': lambda x, z: x / z,  # Division
}

# Evaluate the expression using the operator_dict
result = operator_dict[y](int(x), int(z))

# Print the result to one decimal place
print('{:.1f}'.format(result))