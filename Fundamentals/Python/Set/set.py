'''
Sets are collections of unordered items that are unique.

They are created using curly braces, and, due to the way they're stored, 
it's faster to check whether an item is part of a set using the in operator, rather than part of a list.
'''
num_set = {1, 2, 3, 4, 5}

print(3 in num_set)

# What is the output of this code?
letters = {"a", "b", "c", "d"}
if "e" not in letters:
  print(1)
else: 
  print(2)

'''
You can use the add() function to add new items to the set, 
and remove() to delete a specific element:
'''
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

'''
Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set but not in the second.
The symmetric difference operator ^ gets items in either set, but not both.
'''
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

'''
Given two sentences, you need to find and output the number of the common words (words that are present in both sentences).

Sample Input:
this is some text
I would like this tea and some cookies

Sample Output:
2

The words 'some' and 'this' appear in both sentences.
'''
# s1 = input()
# s2 = input()
list1 = s1.split()
list2 = s2.split()
print(len(set(list1)&set(list2)))

print(len(set(list1).intersection(set(list2))))

# What is the output of this code?
a = {1, 2, 3}
b = {0, 3, 4, 5}
print(a & b)