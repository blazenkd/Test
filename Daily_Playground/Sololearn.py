# 2/28/2023
# ---SoloLearn---

'''
String Functions

String have many useful functions:
count(str) returns how many times the str substring appears in the given string.
upper() converts the string to uppercase.
lower() converts the string to lowercase.
replace(old, new) replaces all occurrences of old with new.
len(str) returns the length of the string (number of characters).
'''

x = "This is some text"

print(x.count("s"))
print(x.upper())
print(x.lower())
print(x.replace("some text", "awesome"))
print(len(x)) 

'''
Manipulating Strings

You are making a text editor and need to implement find/replace functionality.
The code declares a text string. You need to take two string inputs, which represent the substring to find and 
what to replace it with in the text.
Your program needs to output the number of replacements made, along with the new text.

For example, for the given text "I weigh 80 kilograms. He weighs 65 kilograms.":

Sample Input
kilograms
kg

Sample Output
2
I weigh 80 kg. He weighs 65 kg.

The program replaced 2 occurrences of the word kilograms with kg.
'''

text = "Amy has 128 dollars, while David has 54 dollars. Amy is going to the zoo. David watches soccer."

# replace_old = input()
# replace_new = input()
# print(text.count(replace_old))
# print(text.replace(replace_old, replace_new))

'''
What is the output of this code?
'''
x = 'abc'
x = x * len(x)
print(x.count('a'))







