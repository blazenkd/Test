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