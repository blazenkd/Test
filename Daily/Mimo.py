# 2/19/2023
# ---Mimo---

''''''
class Book:
    title = "Harry Potter and the Deathly Hallows"
    pages = 607
    number = "7th"
    genre = "fantasy"
    print(f"{title} has {pages} pages")
    print(f"It is the {number} in the series.")

class Movie:
    name = "Toy Story 3"
    start_time = "4:45pm"
    end_time = "6:32pm"

movie = Movie()
print("Movie: " + movie.name)
print("Start: " + movie.start_time)
print("End: " + movie.end_time)

class Grocery_Item:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.has_discount = discount

    def display_info(self):
        print(self.name, "is $", self.price)
    
apple = Grocery_Item("apple", 1, False)
cheerios = Grocery_Item("cheerios", 4, True)

apple.display_info()
cheerios.display_info()
print("does", apple.name, "have a discount?", apple.has_discount)




# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------
