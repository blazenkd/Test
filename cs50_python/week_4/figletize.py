'''
CS50 Python 2023
Week 4: figlet.py

Task :

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font,
in which case the first of the two should be -f or --font, and
the second of the two should be the name of the font.

Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is
not -f or --font or the second is not the name of a font, the program
should exit via sys.exit with an error message.
'''

import argparse  # Import module for parsing command line arguments
import random  # Import module for generating random numbers
from pyfiglet import Figlet  # Import module for generating ASCII art

def figletize(prompt: str, font: str) -> None:
    """
    Prompt the user for input and print ASCII art using the specified font.

    Args:
        prompt (str): The prompt to display to the user.
        font (str): The name of the font to use for the ASCII art.
    """
    # Prompt user for input and store it in variable 'txt'
    txt = input(prompt)
    # Create a Figlet object with the specified font
    figlet = Figlet(font=font)
    # Print the output of the ASCII art generated with Figlet object
    print(f"Output:\n{figlet.renderText(txt)}")


def main() -> None:
    """
    Parse command line arguments and call figletize with the appropriate font.
    """
    # Create an argument parser object
    parser = argparse.ArgumentParser(description="Generate ASCII art using Figlet.")
    # Add an argument to specify the font
    parser.add_argument("-f", "--font", help="specify the font to use", choices=Figlet().getFonts())
    # Parse the command line arguments
    args = parser.parse_args()

    # If the font argument was provided, call figletize with that font
    if args.font:
        figletize("Input: ", args.font)
    # If the font argument was not provided, call figletize with a random font
    else:
        figletize("Input: ", random.choice(Figlet().getFonts()))


if __name__ == "__main__":
    main()
    