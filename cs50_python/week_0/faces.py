'''
CS50 Python 2023
Week 0: faces.py
'''


'''
Task:

This code solves the problem of replacing textual representations of smiley faces (":)") and frowning faces (":(")
with their corresponding emojis ("🙂" and "🙁", respectively) in an input string. The code uses regular expressions
(regex) to find and replace all occurrences of these textual representations with their corresponding emojis,
and returns the modified string.
'''


import re

def main(input_str):
    # Check if input is empty
    if not input_str:
        return "empty input"

    try:
        # Use regex to find and replace both :) and :(
        pattern = re.compile(r":[()]+")
        result = pattern.sub(lambda m: "🙂" if m.group() == ":)" else "🙁", input_str)
        return result

    except re.error:
        return "regex error"

# Prompt user for input and call main function
x = input("Enter text: ")
print(main(x))