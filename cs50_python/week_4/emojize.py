'''
CS50 Python 2023
Week 4: emojize.py

Task :

Because emoji aren’t quite as easy to type as text, at least on laptops and desktops,
some programs support “codes,” whereby you can type, for instance, :thumbs_up:,
which will be automatically converted to 👍. Some programs additionally support
aliases, whereby you can more succinctly type, for instance, :thumbsup:, which
will also be automatically converted to 👍.

See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list
of codes with aliases.

In a file called emojize.py, implement a program that prompts the user for a str
in English and then outputs the “emojized” version of that str, converting any
codes (or aliases) therein to their corresponding emoji.
'''

import emoji

def emojize_str(input_str):
    """
    Emojizes a given string by replacing any emoji codes or aliases with their
    corresponding emoji characters.

    Args:
        input_str (str): The input string to be emojized.

    Returns:
        str: The emojized version of the input string.
    """
    # Convert any emoji codes or aliases in the input string to their
    # Corresponding emoji characters
    emojized_str = emoji.emojize(input_str)

    # Return the emojized version of the input string
    return emojized_str

# Prompt the user for an input string
user_str = input("Input: ")

# Emojize the input string
output_str = emojize_str(user_str)

# Print the emojized string to the console
print("Output:", output_str)
