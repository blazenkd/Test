# 2/26/2023
# ---SoloLearn---
'''
You need to make a program that counts the number of vowels in a given text.
The vowels are a, e, i, o, and u.

Take a string as input and output the number of vowels.

Sample Input:
this is great

Sample Output:
4
'''

# var = str(input())
# count = 0
# for word in var.split(" "):
#     for letter in word:
#         if letter == "a" or "e" or "i" or "o" or "u":
#             count += 1
# print(count)

'''
There is an issue with the conditional statement inside the inner for loop. 
The condition if letter == "a" or "e" or "i" or "o" or "u": is always evaluating to True because the sub-expressions after each or operator 
are not being compared to letter. This is because the or operator evaluates each sub-expression independently and returns the first 
sub-expression that is truthy. Since all of the sub-expressions in this condition are non-empty strings, they are truthy, and the condition 
always evaluates to True, even if letter is not a vowel.

To fix this issue, you can modify the condition to compare each sub-expression to letter using the == operator, 
like this: if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":. 
Alternatively, you can use the in operator to check if letter is in a list of vowels, 
like this: if letter in ["a", "e", "i", "o", "u"]:.

Here's the corrected code using the in operator:
'''

# var = str(input())
# count = 0
# for word in var:
#     if word in ["a", "e", "i", "o", "u"]:
#         count += 1
# print(count)

'''
Strings can be thought of as a sequence of characters. 
Each character in the string has its unique position (or index).
You can access a character of a string using its index:
'''
x = "Hello"
print(x[2])

'''
You can also use negative indices, which access the characters of the string counting from the end.
'''
print(x[-1])

'''
You can loop through the characters in a string using a for loop:
'''
for c in x:
    print(c)

'''
The in operator can be used to check if a string is part of another string.
'''
x = "I love Python"
if "love" in x:
   print("Yes")

'''
What is the output of this code?
'''
res = 0
s = 'xyz'
if 'x' in s:
   res += 1
elif 'a' in s:
   res += 1
print(res)

'''
Strings can be added together (also called concatenation):
'''
print("Spam" + 'eggs')

'''
Strings can also be multiplied by integers. This produces a repeated version of the original string.
'''
print("spam" * 3)

print(4 * '2')

'''
Let's test your coding skills!
Take a string as input and output each letter of the string on a new line, repeated N times, 
where N is the position of the letter in the string.
'''
word = str(input())
for i, char in enumerate(word):
    print(char * (i+1))

'''
Guess the output
'''
a = "abra"
b = "cad"
x = a+b+a
print(x)

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

print('I\'m learning!')


'''
You are making a program to analyze text.
Take the text as the first input and a letter as the second input, 
and output the frequency of that letter in the text as a whole percentage.

Sample Input:
hello
l

Sample Output:
40

Explanation : The letter l appears 2 times in the text hello, which has 5 letters. 
So, the frequency would be (2/5)*100 = 40.
'''

text = "hello"
letter = "l"
count = text.count("l")
total = len(text)
percentage = (count / total) * 100
