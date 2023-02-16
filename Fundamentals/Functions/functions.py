# 2/15/2023
# ---Mimo---

"""
#1 [Morse Code Encoder]

Let's use our knowledge of returning values to write a function that converts a set of
numbers to morse code.

We'll replace each number of the passed code parameter with its morse correspondent and
return the result.
"""

def convert_to_morse(code):
    code = code.replace("1", ".----")
    code = code.replace("2", "..---")
    code = code.replace("3", "...--")
    code = code.replace("4", "....-")
    code = code.replace("5", ".....")
    code = code.replace("6", "-....")
    code = code.replace("7", "--...")
    code = code.replace("8", "---..")
    code = code.replace("9", "----.")
    code = code.replace("0", "-----")
    return code
lock_code = "1 2 2 5 0"
print(f"Initial code: {lock_code}")

morse = convert_to_morse(lock_code)
print(f"Morse code: {morse}")

"""
#2 [Fare Split Calculator]

Let's use our knowledge of using multiple parameters to create a function that splits a 
Doober fare between several users.

We'll divide the price by the number of passengers first. Then, we'll add a small feature
cost to each passenger's share.
"""

def split_fare(fare, passengers, feature_cost):
    share = fare/passengers
    print(f"Splitting the ${fare} fare between {passengers} passengers...")

    shared_cost = share + feature_cost
    print(f"Adding a ${feature_cost} feature cost...")
    return shared_cost

fare_cost = 36
passengers = 3
feature_cost = 0.5

shared_cost = split_fare(fare_cost, passengers, feature_cost)
print(f"Each pays: ${shared_cost}")




# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------
