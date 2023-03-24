'''
CS50 Python 2023
Week 1: bank.py
'''


'''
Task:

In a file called bank.py, implement a program that prompts the user for a greeting.
If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”),
output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
and treat the user’s greeting case-insensitively.
'''


user = input("Greeting: ").strip().lower()  # Get user input, strip whitespace, and convert to lowercase

# Use a nested ternary operator to check the user's input and output the corresponding result
# The operator works like an if-else statement, but can be written more concisely
# The first condition checks if the input starts with the string "hello". If it does, the result is "$0"
# If the first condition is false, the second condition checks if the input starts with "h". If it does, the result is "$20"
# If both conditions are false, the default result is "$100"
print("$0" if user.startswith("hello") else "$20" if user.startswith("h") else "$100")