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

"""
#3 [Calculator]

Let's create a simple calculator that can add, subtract, and multiply numbers.

We'll create a function that takes two numbers and an operator as its parameters.

Then we'll use if and elif statements to perform the correct calculation. Here's a look
at the finished code.
"""

def calculator(num_1, num_2, op):
    result = 0

    if op == "+":
        result = num_1 + num_2
    elif op == "-":
        result = num_1 - num_2
    elif op == "*":
        result = num_1 * num_2
    
    print(f"{num_1} {op} {num_2} = {result}")

calculator(5, 10, "*")

"""
#4 [Common Friend Checker]

Let's use our knowledge of using lists with functions to find out if a user is a common
friend amongst two other users.

We'll check if the user is in each of the friend's list and then use the & operator
to check the resulting booleans.
"""

def is_common_friend(user, friends_a, friends_b):
    is_friend_a = friends_a.count(user) >= 1
    is_friend_b = friends_b.count(user) >= 1
    is_common = is_friend_a & is_friend_b
    return is_common

friends_joe = ["Sam", "Alex", "Zoe"]
friends_may = ["Kim", "Alex", "Cy", "Ted"]
common_alex = is_common_friend("Alex", friends_joe, friends_may)
print(f"Alex is a common friend {common_alex}")

"""
#5 [Classes Scheduler]

Let's use our knowledge of functions and loops to match a list of classes to available
time slots.

We'll create a loop that runs once for each class, joins it with a time slot at the same 
index, and saves the schedule in a new list.
"""

def schedule_classes(classes, times):
    schedule = []

    index = 0
    while index < len(classes):
        schedule_class = classes[index] + ": " + times[index]
        schedule.append(schedule_class)
        index += 1
    return schedule

classes = ["Algebra", "History", "Biology", "Swimming"]
times = ["9a.m.", "11a.m.", "1p.m.", "3p.m."]
schedule = schedule_classes(classes, times)
print(f"Monday's schedule {schedule}")

# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------
