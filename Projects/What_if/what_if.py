import random

class Monster:
    def __init__(self, name):
        self.name = name
        self.min_attack = 0
        self.max_attack = 10
        self.attack = random.randint(self.min_attack, self.max_attack)
    
    def battle(self, other):
        if self.attack > other.attack:
            # the self monster wins, so increase its attack range by one
            self.max_attack += 1
            self.min_attack += 1
            
            # No change if lose
            other.max_attack -= 0
            other.min_attack -= 0
            
            # update the self monster's attack to a random value within the new attack range
            self.attack = random.randint(self.min_attack, self.max_attack)
            print("Blue Eyes", self.min_attack, self.max_attack)
            other.attack = random.randint(other.min_attack, other.max_attack)
            print("Dark Magician", other.min_attack, other.max_attack)
            return self
        else:
            # the other monster wins, so increase its attack range by one
            other.max_attack += 1
            other.min_attack += 1   
            
            # decrease the self monster's attack range by one
            self.max_attack -= 0
            self.min_attack -= 0
            
            # update the other monster's attack to a random value within the new attack range
            other.attack = random.randint(other.min_attack, other.max_attack)
            print("Dark Magician", other.min_attack, other.max_attack, other.attack)
            self.attack = random.randint(self.min_attack, self.max_attack)
            print("Blue Eyes", self.min_attack, self.max_attack)
            return other

# create two Monster instances with names
Blue_Eyes = Monster("Blue-Eyes White Dragon")
Dark_Magician = Monster("Dark Magician")

# create a list to hold the battle results
results = []

# run 10 battles between Blue_Eyes and Dark_Magician and store the results
for i in range(10):
    # update the attack values of the monsters before the battle
    Blue_Eyes.attack = random.randint(Blue_Eyes.min_attack, Blue_Eyes.max_attack)
    print(f"Battle {i+1} Blue Eyes Attack", Blue_Eyes.attack)
    Dark_Magician.attack = random.randint(Dark_Magician.min_attack, Dark_Magician.max_attack)
    print(f"Battle {i+1} Dark Magician Attack", Dark_Magician.attack)
    # determine the winner of the battle
    winner = Blue_Eyes.battle(Dark_Magician)
    
    # store the battle results as a tuple
    result = (Blue_Eyes.name, Blue_Eyes.attack, Dark_Magician.name, Dark_Magician.attack, winner.name)
    
    # append the result to the results list
    results.append(result)

# print the results
for i, result in enumerate(results):
    print(f"Battle {i + 1}: {result}")
