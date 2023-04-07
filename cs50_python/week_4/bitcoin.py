'''
CS50 Python 2023
Week 4: bitcoin.py

Task :
In a file called bitcoin.py, implement a program that:

    # Expects the user to specify as a command-line argument the number of Bitcoins,
    that they would like to buy. If that argument cannot be converted to a float,
    the program should exit via sys.exit with an error message.

    # Queries the API for the CoinDesk Bitcoin Price Index at
    https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object,
    among whose nested keys is the current price of Bitcoin as a float.
    Be sure to catch any exceptions, as with code like:

        # import requests

        # try:
        #     ...
        # except requests.RequestException:
        #     ...

    # Outputs the current cost of Bitcoins in USD to four decimal places,
    using , as a thousands separator.
'''


# Importing the sys module to access command-line arguments
import sys

# Importing the requests module to make HTTP requests
import requests


# Checking if there is exactly one command-line argument
def main():
    """
    Check if there is exactly one command-line argument, convert it to a float,
    and call btc_price function.

    Args:
        None.

    Returns:
        None.
    """

    if len(sys.argv) == 2:
        try:
            # Converting the command-line argument to a float
            num = float(sys.argv[1])
            # Calling the btc_price function and printing the result
            print(btc_price(num))
        except ValueError:
            # Exiting the program with an error message if the command-line argument is not a number
            sys.exit("Command-line argument is not a number")
    else:
        # Exiting the program with an error message if there is no command-line argument
        sys.exit("Missing command-line argument")


def btc_price(num):
    """
    Make an HTTP GET request to the Coindesk API, extract the current Bitcoin price from the
    response, multiply it by the argument passed to the function, and return the result
    as a formatted string.

    Args:
        num (float): The amount of Bitcoin to convert to USD.

    Returns:
        str or None: The value of the specified amount of Bitcoin in USD as a formatted string,
        or None if there was an error making the HTTP request.
    """
    try:
        # Making an HTTP GET request to the Coindesk API
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json", timeout = 10
        )
        # Parsing the response as JSON
        data = response.json()
        # Extracting the current Bitcoin price from the response
        price = data["bpi"]["USD"]["rate_float"]
        # Multiplying the Bitcoin price by the argument passed to the function
        value = price * num
        # Formatting the result as a string with 4 decimal places and a thousands separator
        return f"${value:,.4f}"
    except requests.RequestException:
        return None


# Calling the main function to start the program
if __name__ == "__main__":
    main()
