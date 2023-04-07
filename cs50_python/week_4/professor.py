'''
CS50 Python 2023
Week 4: professor.py

Task :

In a file called professor.py, implement a program that:

    # Prompts the user for a level, If the user does not input 1, 2, or 3, the program should
        prompt again.
    # Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X
        and Y is a non-negative integer with digits. No need to support operations other
        than addition (+).
    # Prompts the user to solve each of those problems. If an answer is not correct (or not even a
        number), the program should output EEE and prompt the user again, allowing the user up to
        three tries in total for that problem. If the user has still not answered correctly after
        three tries, the program should output the correct answer.
    # The program should ultimately output the user’s score: the number of correct answers out of 10

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user
for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative
integer with level digits or raises a ValueError if level is not 1, 2, or 3:
'''

import random


def main():
    '''
    This function runs a math game where the user solves addition problems of
    varying difficulty levels. The user has 3 chances to answer each equation,
    earning a point for each correct answer, and the game ends after all equations
    have been solved or the user quits. The final score is printed at the end.
    '''
    eqn_count = 10  # number of equations to solve
    score = 0  # number of correct answers
    chances = 3  # number of chances to answer each equation
    level = get_level()  # user-selected difficulty level

    # loop through equations until count is 0
    while eqn_count != 0:
        if chances == 3:  # generate a new equation only if chances == 3
            operand1, operand2 = generate_operands(level)

        try:
            user_answer = int(input(f"{operand1} + {operand2} = "))
            correct_answer = operand1 + operand2

            if user_answer == correct_answer:
                eqn_count -= 1
                score += 1
                chances = 3  # reset chances for new equation
                continue
            raise ValueError

        except (ValueError, NameError):
            print("EEE")
            chances -= 1

        if chances == 0:
            print(f"{operand1} + {operand2} = {correct_answer}")
            chances = 3  # reset chances for new equation
            eqn_count -= 1
            continue

    print(f"Score: {score}")


def get_level():
    """
    This function prompts the user to select a difficulty level (1-3) for the math game.
    If the user enters an invalid input, they will be prompted again until a valid input
    is provided. The function returns the selected difficulty level as an integer.
    """
    # loop until user inputs a valid level between 1 and 3
    while True:
        try:
            level = int(input("Select difficulty level (1-3): "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass

def generate_operands(level):
    """
    This function generates two random integers within a specified range based on the
    selected difficulty level (1-3) for the math game. If level 1 is selected, the
    integers will be between 0 and 9. If level 2 is selected, the integers will be
    between 10 and 99. If level 3 is selected, the integers will be between 100 and
    999. The function returns the two randomly generated integers as a tuple.
    """
    # generate random integers based on the user-selected difficulty level
    if level == 1:
        operand1 = random.randint(0, 9)
        operand2 = random.randint(0, 9)
    elif level == 2:
        operand1 = random.randint(10, 99)
        operand2 = random.randint(10, 99)
    elif level == 3:
        operand1 = random.randint(100, 999)
        operand2 = random.randint(100, 999)

    return operand1, operand2


if __name__ == "__main__":
    main()
