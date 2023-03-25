'''
CS50 Python 2023
Week 2: twttr.py
'''

'''
Task :

When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels,
much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts
the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
'''

# This function takes a string input from the user and removes all vowels (A, E, I, O, U) from it.
# It then returns the modified string with the vowels removed.
def twttr():
    vowels = "AEIOUaeiou"  # define a string of vowels in uppercase and lowercase
    text = input("Enter some text: ")  # prompt the user for input
    result = ""  # initialize an empty string to hold the modified text
    for char in text:  # iterate over each character in the input text
        if char not in vowels:  # if the character is not a vowel, append it to the result string
            result += char
    print(result)  # output the modified text
# Call twttr function
twttr()