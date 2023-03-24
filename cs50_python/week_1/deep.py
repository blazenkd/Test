'''
CS50 Python 2023
Week 1: deep.py
'''


'''
Task:

In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
Otherwise output No.
'''


# get input from user and remove whitespace
user = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()

# check if user input is 42, FORTY-TWO, or FORTY TWO (case-insensitive)
if user.upper() in ["42", "FORTY-TWO", "FORTY TWO"]:
    print("Yes")
else:
    print("No")                             