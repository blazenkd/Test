# 2/26/2023
# ---FreeCodeCamp---
"""
Numpy
"""
import numpy as np

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(np.full_like(a, 100))



arr = np.zeros((7,7))  # create a 7x7 array of zeros

# fill the middle part of the array with ones
arr[1:-1, 1:-1] = np.ones((5,5))

# set the element at (3,3) to 5
arr[3,3] = 5

print(arr)



output = np.zeros((7,7))

z = np.ones((5, 5))
z[2, 2] = 5

output[1:-1, 1:-1] = z
print(output)
# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

"""

"""
