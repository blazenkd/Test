# 2/14/2023
# ---Mimo---

"""
The headquarter of this brand is in New York and the flasgship store in Paris, but we can't
tell just by looking at the locations_list.

To associate a meaning to each value in a collection of values, we use a data structure
called a dictionary, like locations here.

To create a dictionary, we start by coding a pair of curly braces {} to hold the values.

Dictionaries are made up of pairs of keys, like "headquarters", and values like "New York",
separated by a colon ":" .

Keys are like labeled indices. We use them because they help us retrieve values like "Paris"
based on their meaning.

Keys like "headquarters" and "flagship" are unique within the dictionary, so we can only
use a key once.

Each key is associated with exactly one value, like "New York" here.

Inside the dictionary, we separate key-value pairs using commas ",".

"""
locations = {
    "headquarters" : "New York",
    "flagship" : "Paris"
}
print(locations)
locations_list = ["New York", "Paris"]
print(locations_list)

"""
A dictionary's key can be numbers, booleans, or tuples, but the most commonly used type
is a string, like "brand" here.

The values can be of any type, including lists, like the restoration dates.

We can store as many key-value pairs as we want inside a dictionary. Add another pair,
"rented" : False.

"""
car_data = {"brand" : "Cadillac",
            "year" : 1960,
            "restoration" : ["1990", "2018"],
            "rented" : False}
print(car_data)

"""
Why do we need dictionaries?
    - To associate each value of a collection with a meaningful "label", instead of an index

What do we use to surround the key-value pairs stored in a dictionary?
    - Curly braces {}

How do we call pairs like "name" : "Gilles"?
    - Key-value pairs

Why do we need keys?
    - To identify the values

How many times can we use the same key within a dictionary?
    - Only once

How many values can a key be associated with?
    - Only one value

How do we separate different key-value pairs insdie a dictionary?
    - Using commas "," 

What types can a dictionary's keys be?
    - Strings, numbers, booleans, or tuples

What type can the values associated with keys have?
    - Any type

How many key-value pairs can we store in a dictionary?
    - As many as we want
"""

"""
Code the variable "contents" to store this dictionary, as well as the curly braces around it.
"""
contents = {
    "ch. 1": "A long-expected party",
    "ch. 2": "The shadow of the past",
    "ch. 3": "Three is company"
}
print(contents)
"""
Separate the key "name" from the value "Gilles" using a colon ":",
"""
user = {
    "name" : "Gilles",
    "surname" : "Deleuze"
}
print(user)

"""
Add another key pair for the answer of a colleague that's also called Luis.

Code the key-value pair "Meg" : True, followed by a comma to separate it from the next pair.
"""
participants = {
    "Meg" : True,
    "Kim" : False,
    "Luis" : True,
    "Luis M." : False
}
print(participants)

"""
Code a key that has a valid type: either a string, tuple, boolean, or a number.
"""
members_count = {
    ("Sai", "Chloe", "Yumi"): 3}
print(members_count)

"""
Code the tuple ("Ted", 50) as the value associated with the key "first".
"""
winner_scores = {
    "first" : ("Ted", 50),
    "second" : ("Jess", 47)
}
print(winner_scores)

"""
Code a key-value pair "other" : "0.03%" for the mix of other elements in air's composition
"""
air_composition = {
    "nitrogen" : "78%",
    "oxygen" : "21%",
    "argon" : "0.93%",
    "carbon dioxide" : "0.04%",
    "other" : "0.03%"
}
print(air_composition)


# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

"""
To learn, I will create my own version and look for errors.
"""
locations_kd = {
    "KD" : "Sacramento",
    "SS" : "Manila"
}
print(locations_kd)
locations_list_kd = ["Sacramento", "Manila"]
print(locations_list_kd)

"""
A dictionary's key can be numbers, booleans, or tuples, but the most commonly used type
is a string, like "breed" here.

The values can be of any type, including lists, like "friends".

We can store as many key-value pairs as we want inside a dictionary. Add another pair,
"Sleeping" : True.
"""

dog_data = {"breed" : "Jack Russell",
            "year" : 2015,
            "friends" : ["Angel", "Moka"],
            "sleeping" : True}
            
print(dog_data)

"""
Code the variable "k_dramas" to store this dictionary, as well as the curly braces around it.
"""
k_dramas = {
    1: "The Glory",
    2: "W",
    3: "Hotel del Luna"
}
print(k_dramas)
"""
Separate the key "name" from the value "Jong-suk" using a colon ":",
"""
w = {
    "name" : "Jong-suk",
    "surname" : "Lee"
}
print(w)

"""
Add another key pair for the answer of a colleague that's also called Hyo-joo.

Code the key-value pair "Ji-eun" : True, followed by a comma to separate it from the next pair.

"""
hotel_del_luna_cast = {
    "Ji-eun" : True,
    "Jin-goo" : True,
    "Jong-suk" : False,
    "Hyo-joo" : False
}
print(hotel_del_luna_cast)	

"""
Code a key that has a valid type: either a string, tuple, boolean, or a number.
"""
genre = {
    ("The Glory", "W", "Hotel del Luna"): "K Drama"}
print(genre)

"""
Code the tuple ("Ted", 50) as the value associated with the key "first".
"""
k_drama_ratings = {
    "first" : ("Hotel del Luna", 8.2),
    "second" : ("W", 8),
    "third" : ("Glory", 7.9)
}
print(k_drama_ratings)

"""
Code a key-value pair "Pyo Ji-Hoon" : "Ji Hyun-Joong" as an additional character
in Hotel del Luna
"""
hotel_del_luna_characters = {
    "Lee Ji-Eun" : "Jang Man-Wol",
    "Yeo Jin-Goo" : "Koo Chan-Sung",
    "Shin Jung-Keun" : "Kim Sun-Bi",
    "Bae Hae-Sun" : "Choi Seo-Hee",
    "Pyo Ji-Hoon" : "Ji Hyun-Joong"
}
print(hotel_del_luna_characters)