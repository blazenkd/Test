# 2/16/2023
# ---SoloLearn---

"""
This code does the following:

    1. Create a set nums with the values 1, 2, 3, 4, 5, and 6.
    2. Use the & operator to take the intersection of nums with the set {0, 1, 2, 3}. This leaves the values 1, 2, 
        and 3 in nums.
    3. Use the filter() function with a lambda function that checks if a value is greater than 1. This returns a 
        filter object that contains the values 2 and 3.
    4. Convert the filter object to a list and store it in nums.
    5. Print the list [2, 3].
    6. Print the length of the nums.
"""

nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
print(nums)
nums = filter(lambda x: x > 1, nums)
nums = list(nums)
print(nums)
print(len(nums))

""" 
The lambda function lambda x: x % 2 == 0 takes one argument x and returns True if 
x is even (i.e., if x % 2 == 0) and False otherwise.

The filter function takes a function (in this case, the lambda function) and an 
iterable (in this case, the nums list) as arguments, and returns an iterator that 
yields the elements of the iterable for which the function returns True.

The list function is used to convert the iterator returned by filter into a list.
"""

nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)
