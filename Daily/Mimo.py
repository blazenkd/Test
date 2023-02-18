# 2/17/2023
# ---Mimo---

''''''
trials = 5
data_points = 160
peer_reviewed = True

if trials >= 5 and data_points > 100 and peer_reviewed:
    print("Experiment finished!")
else:
    print("There's more work to do.")
''''''
moon_count = [("earth", 1), ("jupiter", 79)]
del moon_count[-1]
print(moon_count)
''''''
answers = ["C", "B", "C", "A", "D", "A", "B", "D", "D", "C"]
responses = ["C", "B", "C", "A", "D", "A", "B", "D", "D", "C"]

if responses[-1] == answers[len(responses)-1]:
    correct = True
else:
    correct = False

if not correct:
    del responses[-1]
    print("sorry, please try the last question again!")

elif len(responses) < len(answers):
    print("Quiz not copmlete.")
    correct = string(len(responses))
    print("You've got " + correct + "answers correct so far, please add an answer for the next question.")

else:
    print("Well done, you have complete the quiz!")

''''''
hobbies = ["Archery", "Bowling", "Canoeing", "Dance", "Embroidery", "Flute", "Gymnastics"]
while hobbies[-1] != "Dance":
    del hobbies[-1]
number = str(len(hobbies))
print("These are your " + number + " favorite hobbies:")
print(hobbies)

extras = ["Gym", "Cinema", "Restaurants", "Jewelry", "Coffee", "Netflix", "Bingo"]

costs = [50, 20, 80, 30, 40, 10, 25]
to_save = 100
savings = 0

while to_save > 0:
    to_save -= costs[-1]
    savings += costs[-1]
    del costs[-1]
    del extras[-1]
savings = str(savings)
print("You'll save " + savings + " euros by sticking to these extras:")
print(extras)

next_saving = extras[-1]
print("If you need to save more money, take some time off " + next_saving + ".")
# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------
