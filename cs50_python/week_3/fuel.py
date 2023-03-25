'''
CS50 Python 2023
Week 3: fuel.py
'''

'''
Task :

In a file called fuel.py, implement a program that prompts the user for a fraction,
formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage
rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains,
output E instead to indicate that the tank is essentially empty. And if 99% or more remains,
output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
'''


# Prompts the user for a fraction X/Y, calculates the fuel percentage,
# and returns 'E' if 1% or less fuel remains, 'F' if 99% or more fuel remains,
# or the fuel percentage as a string with a percent sign.
# If X or Y is not an integer, X is greater than Y, or Y is 0, prompts the user again.
# Raises ValueError if the input is invalid.


def calculate_fuel_percentage():
    # Start a loop that will continue until valid input is entered
    while True:
        try:
            # Prompt the user for input and split the input into two integers
            x, y = input("Enter fraction (X/Y): ").split("/")
            x = int(x)
            y = int(y)
            # Check if the denominator is 0 or the numerator is greater than the denominator
            if y == 0 or x > y:
                # If so, raise a ValueError to signal that the input is invalid
                raise ValueError
            # If the input is valid, break out of the loop
            break
        except (ValueError, ZeroDivisionError):
            # If the input is invalid, print an error message and continue the loop
            print("Invalid input. Try again.")

    # Calculate the fuel percentage as a rounded integer
    fuel_percent = round(x / y * 100)

    # Check if the fuel percentage is less than or equal to 1%
    if fuel_percent <= 1:
        # If so, return "E" to indicate the tank is essentially empty
        return "E"
    # Check if the fuel percentage is greater than or equal to 99%
    elif fuel_percent >= 99:
        # If so, return "F" to indicate the tank is essentially full
        return "F"
    else:
        # If the fuel percentage is between 1% and 99%, return it as a string with a percent sign
        return f"{fuel_percent}%"

# Call the calculate_fuel_percentage() function and store the result in a variable
percentage = calculate_fuel_percentage()

# Print the result
print(percentage)