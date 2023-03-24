'''
CS50 Python 2023
Week 0: tip.py
'''


'''
Task:

dollars_to_float, which should accept a str as input
(formatted as $##.##, wherein each # is a decimal digit),
remove the leading $, and return the amount as a float.
For instance, given $50.00 as input, it should return 50.0.


percent_to_float, which should accept a str as input
(formatted as ##%, wherein each # is a decimal digit),
remove the trailing %, and return the percentage as a float.
For instance, given 15% as input, it should return 0.15.
'''


# Define the main function
def main():
    # Get the cost of the meal as input, and convert to a float
    dollars = dollars_to_float(input("How much was the meal? "))
    
    # Get the tip percentage as input, and convert to a float
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Calculate the tip as a fraction of the meal cost
    tip = dollars * percent
    
    # Print the recommended tip amount
    print(f"Leave ${tip:.2f}")

# Define a function to convert a string formatted as $##.## to a float
def dollars_to_float(d):
    # Remove leading dollar sign and convert to float
    return float(d[1:])

# Define a function to convert a string formatted as ##% to a float
def percent_to_float(p):
    # Remove trailing percent sign, divide by 100, and convert to float
    return float(p[:-1]) / 100

# Call the main function
main()