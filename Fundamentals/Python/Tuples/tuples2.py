'''
Tuples

Tuples are very similar to lists, except that they are immutable (they cannot be changed).
Also, they are created using parentheses, rather than square brackets.

You can access the values in the tuple with their index, just as you did with lists:

Like lists and dictionaries, tuples can be nested within each other.
'''
words = ("spam", "eggs", "sausages",)
print(words[0])
'''
An advantage of tuples over lists is that they can be used as keys for dictionaries 
(because they are immutable):

Tuples are faster than lists, but they cannot be changed.
'''
dict = {
    ("David", 42): "red",
    ("Bob", 24): "green"
}

print(dict[("Bob", 24)]) 

# What is the result of this code
tuple = (1, (1, 2, 3))
print(tuple[1])

'''
Tuple Unpacking

Tuple unpacking allows you to assign each item in a collection to a variable.

This can be also used to swap variables by doing a, b = b, a , 
since b, a on the right hand side forms the tuple (b, a) which is then unpacked.
'''
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

# What is the value of y after this code runs?
x, y = [1, 2]
x, y = y, x
print(y)

'''
A variable that is prefaced with an asterisk (*) takes all values from the collection 
that are left over from the other variables.
'''
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

'''
You are working on a mapping software. The map is stored as a list of points, where each item is 
represented as a tuple, containing the X and Y coordinates of the point.
You need to calculate and output the distance to the closest point from the point (0, 0).
To calculate the distance of the point (x, y) from (0, 0), use the following formula: √x²+y²

You can iterate over the list and use tuple unpacking to get the x and y coordinates of each point: for (x, y) in points: and output the smallest value.
'''
# import math
# points = [
#     (12, 55),
#     (880, 123),
#     (64, 64),
#     (190, 1024),
#     (77, 33),
#     (42, 11),
#     (0, 90)
# ]
# #your code goes here
# distance = list(range(len(points)))

# z = 0
# for (x,y) in points:
#     distance[z] = math.sqrt((x**2) + (y**2))
#     z += 1
# print(min(distance))

import math
points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]

# create a list of distances using a list comprehension
distance = [math.sqrt(x**2 + y**2) for x, y in points]

# print the minimum distance
print(min(distance))

# What is the output of this code?
a, b, c, d, *e, f, g = range(20)
print(len(e))