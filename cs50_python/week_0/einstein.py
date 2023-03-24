'''
CS50 Python 2023
Week 0: einstein.py
'''


'''
Task:

This code solves the problem of calculating the energy that can be produced
from a given mass using Einstein's famous equation E=mc².
'''


import sys

# function to calculate energy using E=mc² equation
def calculate_energy(mass):
    c_squared = 300000000 ** 2
    energy = mass * c_squared
    return energy

# main function to prompt user for input and display output
def main():
    try:
        # prompt user to enter mass in kilograms
        mass = int(input("Enter mass in kilograms: "))

        # calculate energy using calculate_energy function
        energy = calculate_energy(mass)

        # display calculated energy to user
        print("The energy that can be produced is:", energy, "joules.")
    except ValueError:
        # display error message if user enters non-numeric input
        print("Invalid input. Mass must be a number.")

# check if program is being run as main script
if __name__ == '__main__':
    # call main function
    main()