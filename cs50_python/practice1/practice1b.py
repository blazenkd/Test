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

# Fill in Skeleton



string = input("Enter a string: ")


case = input("Choose a case (1: uppercase, 2: lowercase, 3: title case): ")


case_map = {
    "1" : str.upper,    
    "2" : str.lower,    
    "3" : str.title,    
}


if case in case_map:

    result = case_map[case](string)

    print(result)
else:

    print("Invalid choice!")