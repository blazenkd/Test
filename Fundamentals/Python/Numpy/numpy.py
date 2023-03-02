"""
Numpy
"""
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = a
b[2] = 20
print(a)

'''
Explanation:

A numpy array a is created with values [1, 2, 3, 4, 5].
The variable b is assigned to the same array as a, meaning both a and b refer to the same numpy array object in memory.
The third element of b (which is also the third element of a) is changed to 20.
The array a is printed, which shows the modified values of [1, 2, 20, 4, 5].
Therefore, changing the value of an element in b also changes the corresponding element in a because both 
variables refer to the same numpy array object in memory.
'''

a = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
b = np.max(a, axis=1).sum()
print(b)

'''
Explanation:

A numpy array a is created with two rows and five columns using the np.array() function.
The np.max() function is used to find the maximum value in each row of a along the axis=1 direction (i.e., horizontally). This returns an array [5, 10].
The sum() function is used to find the sum of the two values in the array [5, 10], which is 15.
The variable b is assigned the value of 15.
Finally, the value of b is printed using the print() function.
Therefore, the code finds the maximum value in each row of a numpy array, sums them up, and assigns the result to b. The output is 15.
'''

'''
What code would produce the following array?

[[1. 1.]
[1. 1.]
[1. 1.]
[1. 1.]]
'''

a = np.ones((2,4))
print(a)
b = a.reshape((4,2))
print(b)