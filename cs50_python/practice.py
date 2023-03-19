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

string = input("Enter a string: ")
case = int(input("Choose a case (1: uppercase, 2: lowercase, 3: title case): "))

if case == 1:
    print(string.upper())
elif case == 2:
    print(string.lower())
else:
    print(string.title())