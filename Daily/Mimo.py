# 2/21/2023
# ---Mimo---

'''
Modules

'''
# import math


class FoodDelivery:
    def __init__(self, number, items):
        self.number = number
        self.items = items
    def submit_order(self):
        print(f"Submitting order: {self.number}")
    def make_food(self, item):
        print(f"Made {item}")
    def package_item(self, item):
        print(f"Packaging {item}")
    def complete_order(self):
        self.submit_order()
        for i in self.items:
            self.make_food(i)
            self.package_item(i)
        print(f"Delivering order {self.number}")

chicken = FoodDelivery(1, ["chicken", "rice"])
print(chicken.complete_order())

# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------
