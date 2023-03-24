'''
CS50 Python 2023
Week 1: meal.py
'''

'''
Task :

In meal.py, implement a program that prompts the user for a time and outputs whether it’s
breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all.
Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or
anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts
time, a str in 24-hour format, to the corresponding number of hours as a float. For instance,
given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
'''

def main():
    # Prompt the user for a time in 24-hour format
    time_str = input("Enter a time in 24-hour format (e.g., 7:30 or 16:45): ")
    try:
        # Convert the time string to a float value representing the number of hours
        time_float = convert(time_str)

        # Check if the time is within the range for breakfast, lunch, or dinner, and print the corresponding message
        if 7.0 <= time_float <= 8.0:
            print("breakfast time")
        elif 12.0 <= time_float <= 13.0:
            print("lunch time")
        elif 18.0 <= time_float <= 19.0:
            print("dinner time")

    # Catch a ValueError exception if the time string is not in the expected format
    except ValueError:
        pass


def convert(time):
    # Split the time string into hours and minutes, and convert them to integers
    hours, minutes = map(int, time.split(":"))

    # Compute the total number of hours as a float value, by adding the fractional part of the minutes
    return hours + minutes / 60.0


if __name__ == "__main__":
    main()