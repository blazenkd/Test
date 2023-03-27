'''
CS50 Python 2023
Week 3: grocery.py
'''

'''
Task :

Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs
control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all
uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user’s input case-insensitively.
'''

def make_grocery_list():
    # Initialize an empty dictionary to store the grocery list
    grocery_items = {}

    # Get input from user
    while True:
        try:
            # Prompt user for input and convert to titlecase
            item = input().strip().title()
            # Skip empty input
            if not item:
                continue
            # If item is already in grocery_list, increment count
            if item in grocery_items:
                grocery_items[item] += 1
            # Otherwise, add item to grocery_list with count 1
            else:
                grocery_items[item] = 1
        # If user inputs Ctrl-D (EOFError), break out of loop
        except EOFError:
            break

    # Return grocery list as a string
    return "\n".join([f"{count} {item.upper()}" for item, count in sorted(grocery_items.items())])

# Call the function and store the output in grocery_list
grocery_list = make_grocery_list()

# Print the grocery list
print(grocery_list)