'''
CS50 Python 2023
Week 2: plates.py
'''

'''
Task :

In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

    # “All vanity plates must start with at least two letters.”
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    # “Numbers cannot be used in the middle of a plate; they must come at the end.
        # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
        # The first number used cannot be a ‘0’.”
    # “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets
all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be
uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements
and False if it does not. Assume that s will be a str. You’re welcome to implement additional
functions for is_valid to call (e.g., one function per requirement).
'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    """
    Check if a string is valid based on the following criteria:
    - Length should be between 2 and 6 (inclusive).
    - All characters should be alphanumeric.
    - The first two characters should be alphabetical.
    - The first numeric character should not be 0 and there should be no alphabetical characters after it.
    """

    # Check if length is between 2 and 6 (inclusive)
    if not 2 <= len(s) <= 6:
        return False

    # Check if all characters are alphanumeric
    if not s.isalnum():
        return False

    # Check if the first two characters are alphabetical
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Find the index of the first numeric character
    first_num_index = None
    for i, c in enumerate(s):
        if c.isnumeric():
            # Check if the first numeric character is 0
            if c == '0':
                return False
            first_num_index = i
            break

    # Check if there are no alphabetical characters after the first numeric character
    if first_num_index is not None:
        for c in s[first_num_index+1:]:
            if c.isalpha():
                return False

    # If all checks passed, return True
    return True

main()