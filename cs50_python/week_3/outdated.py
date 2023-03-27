'''
CS50 Python 2023
Week 3: outdated.py
'''

'''
Task :

In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order,
which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first.
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet).
Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day
(YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding”
each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or
September 8, 1636, wherein the month in the latter might be any of the values in the list below:
'''

# Define a list of valid month names
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Enter an infinite loop
while True:
    # Prompt the user for a date
    date_string = input("Date: ")

    try:
        # Try to parse the date string into month, day, and year components
        if "/" in date_string:
            # If the date string is in the format "MM/DD/YYYY", split it into month, day, and year components
            month_string, day_string, year_string = date_string.split("/")
        elif "," in date_string:
            # If the date string is in the format "Month DD, YYYY", split it into month, day, and year components
            month_day_string, year_string = date_string.split(", ")
            month_string, day_string = month_day_string.split(" ")
            # Convert the month string to an integer by finding its index in the MONTHS list and adding 1, since lists are 0-indexed
            month_index = MONTHS.index(month_string) + 1
            month_string = str(month_index)

        # Convert the month, day, and year strings to integers
        month = int(month_string)
        day = int(day_string)
        year = int(year_string)

        # Check that the month and day values are valid (1-12 for month, 1-31 for day)
        if month < 1 or month > 12 or day < 1 or day > 31:
            # If either value is out of range, raise a ValueError
            raise ValueError

    except (AttributeError, ValueError, NameError, KeyError):
        # If there is an error parsing the date or the month/day values are invalid, continue to the next iteration of the loop
        pass

    else:
        # If the date is successfully parsed and passes the validity check, print it in the desired format (YYYY-MM-DD)
        formatted_date = f"{year}-{month:02}-{day:02}"
        print(formatted_date)
        # Exit the loop
        break