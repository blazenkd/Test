import copy
import random

class Hat:

    def __init__(self, **kwargs):
        self.contents = [key for key, value in kwargs.items() for _ in range(value)]

    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        balls = [self.contents.pop(random.randrange(len(self.contents))) for _ in range(number)]
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        successes += 1 if balls_req == len(expected_balls) else 0

    return successes / num_experiments



# Testing Area
# Can we initialize hat1?
# hat1 = Hat(yellow = 10, red = 3, green = 3)
# # What are the contents of hat1?
# print("Contents of hat1:", hat1.contents)
# # How many balls are in hat1?
# print("Balls in hat1:", len(hat1.contents))
# # # Can we draw balls from the hat?
# print("Balls drawn:", hat1.draw(2))
# # What is the contents after the draw?
# print("Contents of hat1 after draw:", hat1.contents)

# run = experiment(hat=hat1, 
#                 expected_balls={"red":2,"green":1},
#                 num_balls_drawn=5,
#                 num_experiments=100)
# print(run)


