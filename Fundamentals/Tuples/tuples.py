# 2/13/2023
# ---Mimo---

# Create function
def get_scores_data(scores_list):
    highest_score = max(scores_list)
    lowest_score = min(scores_list)
    return (highest_score, lowest_score)

# Input
scores = [31, 17, 80]

# Display Return (Output)
data = get_scores_data(scores)
print(data)

# Indices
highest = data[0]
smallest = data[1]

# Display Return (Output)
print(f"smallest score: {smallest}")
print(f"highest score: {highest}")


# Create function
def get_top_three(players):
    return players[0], players[1], players[2]

# Create Input
players = ["Sue", "Ed", "Ann", "Ty"]

# Create Call Function Variable
top_three = get_top_three(players)

# Create Output Display
print(f" First: {top_three[0]}")
print(f" Second: {top_three[1]}")
print(f" Third: {top_three[2]}")

# Create Function
def form_team(players):
  team = []
  team.append(players[0])
  team.append(players[2])
  return team

# Create Call Function Variable
team = form_team(players)

# Make Changes to list
team[0] = "Chloe"

# DIsplay Output
print(team)

"""
What is one of the main uses of tuples?
    Returning multiple values inside functions.

How do we separate the different values when returning multiple values from a function?
    Using commas.

Do we need parentheses when returning multiple values?
    No, just the return keyword followed by the values.

How can we save a tuple returned by a function?
    By storing it in a variable, like any other variable.

How do we retrieve the individual values from the tuple returned by a function?
    By their index.

When should we return a tuple?
    When we're only interested in the individual values or don't intend to modify the tuple.

When should we return a list instead of a tuple?
    When we're interested in the values as a collection, and intend to modify the list.



"""

# Create Function
def check_age(age):
    can_drive = age >= 18
    return age, can_drive

# Create input
age = 17

# Create Call Function Variable
driving_age = check_age(age)

# Display output
print(driving_age)

# Create Function
def analyze_profit(gains, expenses):
    profit = gains - expenses
    after_taxes = 0.85 * profit
    above_mean = profit > 1000
    return profit, after_taxes, above_mean

# Create Input
gains = 3000
expenses = 1200

insights = analyze_profit(gains, expenses)
print(f"profit: {insights[0]}")
print(f"above mean: {insights[2]}")