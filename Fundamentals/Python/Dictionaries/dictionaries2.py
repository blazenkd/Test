'''
Dictionaries

We saw how lists allow us to store elements with their corresponding indices.
The indices in a list are automatically set. But what if we need to set our own index?

Dictionaries are another collection type and allow us to map arbitrary keys to values.
Dictionaries can be indexed in the same way as lists, using square brackets containing keys.

Each element in a dictionary is represented by a key:value pair.
'''
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

# Fill in the blanks to define a valid dictionary with two elements.
cars = {
   "BMW": "blue",
   "Volvo": "red"
   }

'''
You can use strings, integers, booleans, and any other immutable type as dictionary keys.
This means that you cannot use lists or dictionaries as keys:

The code below will generate an error, as it tries to use a list as the key.
'''
# bad_dict = {
#     [1, 2, 3]: "one two three", 
# }