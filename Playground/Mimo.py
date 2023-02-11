# 2/11/2023
# ---Mimo---

def add_bonus(salary):
    bonus = 100
    print(salary + bonus)

add_bonus(1900)

def apply_discount(price):
    discount = 20
    discount = 10
    return price - discount

final_price = apply_discount(50)
print(final_price)

user = "Amy"
def greet_user(name):
    greeting = "Hi"
    print(f"{greeting} {user}!")
greet_user("Amy")

shipping = 10
def calculate_total(cart):
    print(cart + shipping)

calculate_total(54)

single_player = True
if single_player:
    player_1 = "Mario"
print(f"Player 1: {player_1}")

rent = 1000

def calculate_spendings(groceries):
    print(f"Total {rent + groceries}")

print(f"Rent {rent}")
calculate_spendings(300)

price = 100
for i in range(2):
    discount = 10
    price = price - discount
print(f"Discount: {discount}")

def print_double(x):
    print(2*x)
print_double(3)

def exclamation(word):
    print(word + "!")
exclamation("spam")

def printBill(text):
    print("======")
    print(text)
    print("======")