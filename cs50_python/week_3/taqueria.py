'''
CS50 Python 2023
Week 3: taqueria.py

Task :

One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, 
which offers a menu of entrees,per the dict below, wherein the value of 
each key is a price in dollars:

{
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
In a file called taqueria.py, implement a program that enables a user to place an order, 
prompting them for items, one per line, until the user inputs control-d (which is a common 
way of ending one’s input to a program). After each inputted item, display the total 
cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted 
to two decimal places. Treat the user’s input case insensitively. Ignore any input 
that isn’t an item. Assume that every item on the menu will be titlecased.
'''

def place_order():
    """
    Prompts the user to enter menu items and calculates the total cost of the order.

    The function defines the menu as a dictionary where the keys are menu items and the values
    are their prices. It then initializes a variable to keep track of the total cost of the order
    and loops indefinitely to prompt the user for menu items. If the user enters an item that is 
    not in the menu, the function skips that item and prompts the user for another item. If the 
    user enters an item that is in the menu, the function adds the item's price to the total 
    cost and displays the updated total. When the user has finished entering items 
    (by typing ctrl+d),the function returns the total cost of the order.

    Returns:
        A string containing the total cost of the order, formatted as "$X.XX".
    """
    
    # Define the menu as a dictionary where the keys are menu items and the values are their prices
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # Initialize a variable to keep track of the total cost of the order
    total_cost = 0.0

    # Loop indefinitely to prompt the user for menu items
    while True:
        try:
            # Prompt the user for an item, convert it to title case,
            # and remove any leading/trailing whitespace
            item = input("Enter an item: ").strip().title()

            # If the item is not in the menu, skip this iteration of
            # the loop and prompt the user for another item
            if item not in menu:
                continue

            # If the item is in the menu, add its price to the
            # total cost and display the updated total
            total_cost += menu[item]
            print(f"Total: ${total_cost:.2f}")

        # If the user has ended their input (by typing ctrl+d), exit the loop
        except EOFError:
            break

    # Return the total cost of the order
    return f"Your order total is ${total_cost:.2f}"

# Call the place_order() function to run the program and prompt the user for input
order_total = place_order()

# Print the value of 'order',
print(order_total)
