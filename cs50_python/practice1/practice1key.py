'''
Task:

Write a Python program that prompts the user to enter a string,
and then converts the string to uppercase, lowercase, or title case 
(the first letter of each word is capitalized) based on the user's choice. 
The program should then print the converted string.

Example input/output:

Enter a string: Hello World
Choose a case (1: uppercase, 2: lowercase, 3: title case): 1
HELLO WORLD

Enter a string: tHIS iS a TeSt
Choose a case (1: uppercase, 2: lowercase, 3: title case): 2
this is a test

Enter a string: python is awesome
Choose a case (1: uppercase, 2: lowercase, 3: title case): 3
Python Is Awesome
'''

# Prompt the user to enter a string
string = input("Enter a string: ")

# Prompt the user to choose a case option
case = input("Choose a case (1: uppercase, 2: lowercase, 3: title case): ")

# Define a dictionary that maps user input to string methods
case_map = {
    "1" : str.upper,    # Key "1" maps to the str.upper() method
    "2" : str.lower,    # Key "2" maps to the str.lower() method
    "3" : str.title,    # Key "3" maps to the str.title() method
}

# Check if the user's input is a valid key in the case_map dictionary
if case in case_map:
    # If so, call the corresponding string method on the input string
    result = case_map[case](string)
    # Print the result to the console
    print(result)
else:
    # If the user's input is not a valid key, print an error message
    print("Invalid choice!")