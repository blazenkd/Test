'''
CS50 Python 2023
Week 4: game.py

Task :

Prompts the user for a level,
    # If the user does not input a positive integer, the program should prompt again.
    # Randomly generates an integer between 1 and, inclusive, using the random module.
    # Prompts the user to guess that integer. If the guess is not a positive integer,
        the program should prompt the user again.
        # If the guess is smaller than that integer, the program should output Too small!
            and prompt the user again.
        # If the guess is larger than that integer, the program should output Too large!
            and prompt the user again.
        # If the guess is the same as that integer, the program should output Just right!
        and exit.
'''

# Import the random module to generate random numbers
import random

# Prompt user for level
while True:
    level = input("Enter a level (positive integer): ")
    if level.isdigit() and int(level) > 0:
        # Convert the input to an integer if it's a positive integer
        level = int(level)
        # Break out of the loop if the input is valid
        break
    # Prompt the user again if the input is invalid
    print("Invalid input. Please enter a positive integer.")

# Generate random number
number = random.randint(1, level)

# Prompt user to guess the number
while True:
    guess = input("Guess a number between 1 and " + str(level) + ": ")
    if guess.isdigit() and int(guess) > 0:
        # Convert the input to an integer if it's a positive integer
        guess = int(guess)
        if guess < number:
            # Prompt the user again if the guess is too small
            print("Too small!")
        elif guess > number:
            # Prompt the user again if the guess is too large
            print("Too large!")
        else:
            # Exit the loop if the guess is correct
            print("Just right!")
            break
    else:
        # Prompt the user again if the input is invalid
        print("Invalid input. Please enter a positive integer.")
