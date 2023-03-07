'''
List Recap
'''
# What is the result of this code?
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
  print(nums[3])
else:
  print(nums[4])

# Fill in the blanks to iterate over the list using a for loop and print its values.
list = [1, 2, 3]

for var in list:
    print(var)

# Drag and drop from the options below to add 'z' to the end of the list and print the list's length.
list.append('z')

print(len(list))

# What is the result of this code?
letters = ["a", "b", "c"]
letters.append("d")
print(len(letters))

# Fill in the blanks to create a list of numbers multiplied by 10 in the range of 5 to 9.

a = [x*10 for x in range(5, 9)]
print(a)

# What is the result of this code?

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))

'''
Average Word Length

Given a sentence as input, calculate and output the average word length of that sentence.
To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence.

Sample Input:
this is some text

Sample Output:
3.5

Explanation: There are 4 words in the given input, with a total of 14 letters, so the average length will be: 14/4 = 3.5
'''

text = input()

words = text.split()
average_length = sum(len(word) for word in words) / len(words)
print(round(average_length, 2))