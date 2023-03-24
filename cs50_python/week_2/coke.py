'''
CS50 Python 2023
Week 2: coke.py
'''

'''
Task :

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time,
each time informing the user of the amount due. Once the user has inputted at least 50 cents,
output how many cents in change the user is owed.
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
'''

# Define a function called coke that prompts the user to insert coins until at least 50 cents have been inserted,
# and then outputs the amount of change owed in cents.
def coke():

    # Initialize the total amount of coins inserted to zero
    total_inserted = 0

    # Continue prompting until at least 50 cents have been inserted
    while total_inserted < 50:
        # Prompt the user to insert a coin
        coin = int(input("Insert a coin: "))

        # Ignore any coin that isn't an accepted denomination
        if coin not in [1, 5, 10, 25]:
            # Calculate the amount of money still owed
            amount_due = 50 - total_inserted

            # Inform the user of the amount due
            print("Amount Due: {}".format(amount_due))

            # Continue to next iteration of while loop
            continue

        # Add the coin value to the total amount inserted
        total_inserted += coin

        # Calculate the amount of money still owed
        amount_due = 50 - total_inserted

        # Inform the user of the amount due
        print("Amount Due: {}".format(amount_due))

    # Calculate the amount of change owed
    change_owed = total_inserted - 50

    # Output the amount of change owed
    print("Change Owed: {}".format(change_owed))

# Call the coke function
coke()