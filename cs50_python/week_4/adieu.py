'''
CS50 Python 2023
Week 4: adieu.py

Task :

In a file called adieu.py, implement a program that prompts the user for names,
one per line, until the user inputs control-d. Assume that the user will input
at least one name. Then bid adieu to those names, separating two names with one
and, three names with two commas and one and, and names with
commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
'''

def get_names():
    """
    Prompt the user to enter names, one per line, until the user inputs control-d.
    Returns a list of the names entered by the user.

    Returns:
        list: A list of strings containing the names entered by the user.
    """
    name_list = []
    while True:
        try:
            # Prompt user for a name and title-case it
            name = input("Enter a name: ").strip().title()
            # Add name to list of names
            name_list.append(name)
        # Catch end-of-file error (e.g., user hits Ctrl-D) and exit loop
        except EOFError:
            return name_list

def bid_adieu(names):
    """
    Prints a farewell message to the given list of names, separating two names with "and",
    three names with two commas and "and", and lists of names with commas and "and".

    Args:
        names (list): A list of strings containing the names to bid farewell to.
    """
    # Get the number of names in the list
    num_names = len(names)
    # If there's only one name in the list
    if num_names == 1:
        # Print a farewell message to that name
        print(f"Adieu, adieu, to {names[0]}")
    # If there are two names in the list
    elif num_names == 2:
        # Print a farewell message with "and" separating the two names
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    # If there are more than two names in the list
    else:
        # Create a string of all but the last name separated by commas
        name_str = ", ".join(names[:-1])
        # Print a farewell message with "and" separating the last name from the rest
        print(f"Adieu, adieu, to {name_str}, and {names[-1]}")

def main():
    """
    Gets a list of names from the user using the `get_names()` function and prints
    a farewell message to the list of names using the `bid_adieu()` function.
    """
    names = get_names()
    # Print a farewell message to the list of names
    bid_adieu(names)

if __name__ == "__main__":
    main()
