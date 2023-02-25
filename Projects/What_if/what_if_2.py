import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

class Monster:
    def __init__(self, name):
        self.name = name
        self.min_attack = 0
        self.max_attack = 10
        self.attack = random.randint(self.min_attack, self.max_attack)

    def battle(self, other):
        if self.attack > other.attack:
            self.max_attack += 2
            self.min_attack += 0
            other.max_attack += 0
            other.min_attack += 1
            return self

        elif self.attack < other.attack:
            self.max_attack += 0
            self.min_attack += 1
            other.max_attack += 2
            other.min_attack += 0
            return other
        else:
            self.max_attack += 0
            self.min_attack += 0
            other.max_attack += 0
            other.min_attack += 0
            return "Draw"





results = []

Dark_Magician = Monster("Dark Magician")
Blue_Eyes_White_Dragon = Monster("Blue Eyes White Dragon")
for i in range(100):
    # Create two monsters


 

    # battle and store the winner in the results list
    
    print()
    print(f"{Dark_Magician.name} min attack: {Dark_Magician.min_attack}")
    print(f"{Dark_Magician.name} max attack: {Dark_Magician.max_attack}")
    print(f"{Dark_Magician.name} attack: {Dark_Magician.attack}")


    print(f"{Blue_Eyes_White_Dragon.name} min attack: {Blue_Eyes_White_Dragon.min_attack}")
    print(f"{Blue_Eyes_White_Dragon.name} max attack: {Blue_Eyes_White_Dragon.max_attack}")
    print(f"{Blue_Eyes_White_Dragon.name} attack: {Blue_Eyes_White_Dragon.attack}")


    result = Dark_Magician.battle(Blue_Eyes_White_Dragon)

    Dark_Magician.attack = random.randint(Dark_Magician.min_attack, Dark_Magician.max_attack)
    Blue_Eyes_White_Dragon.attack = random.randint(Blue_Eyes_White_Dragon.min_attack, Blue_Eyes_White_Dragon.max_attack)


    if isinstance(result, str):
        results.append(result)
        print(result)
    else:
        results.append(result.name)
        print(result.name)

print()
print(results)




# Calculate the number of wins for each monster
Dark_Magician_wins = results.count("Dark Magician")
Blue_Eyes_White_Dragon_wins = results.count("Blue Eyes White Dragon")
draws = results.count("Draw")

# Create the bar chart
fig, ax = plt.subplots()
bar_width = 0.35
x = np.arange(3)
ax.bar(x, [Dark_Magician_wins, Blue_Eyes_White_Dragon_wins, draws], width=bar_width, label='Wins')
ax.set_xticks(x)
ax.set_xticklabels(['Dark Magician', 'Blue Eyes White Dragon', 'Draw'])
ax.legend()

# Show the chart
plt.show()

# Count the number of wins for each monster
win_counts = Counter(results)


# Create a bar chart
plt.bar(win_counts.keys(), win_counts.values())

# Add labels and title
plt.xlabel('Monster')
plt.ylabel('Wins')
plt.title('Results of 10 Battles')

# Display the chart
plt.show()

# Display the win counts
for monster, wins in win_counts.items():
    print(f"{monster}: {wins} wins")












