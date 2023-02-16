# 2/13/2023
# ---ChatGPT---
"""
In this example, the generator function 'generate_tuples' generates 10 tuples,
each consisting of a number from 0 to 9 and its double. The generator is called
in a for loop, and each generated tuple is printed.

Here's a generator function that outpus a tuple:
"""
def generate_tuples():
    for i in range(10):
        yield (i, i**2)

for x in generate_tuples():
    print(x)
    print(type(x))
"""
A practical example of using generator functions is when you want to generate a 
sequence of values but you don't want to store all of them in memory at once. 
For example, if you have a large dataset and you want to iterate through it, it 
might not be feasible to store the entire dataset in memory. In this case, you 
can use a generator function to generate values one at a time as they are 
requested, instead of generating all of them at once and storing them in memory. 
This can greatly reduce memory usage, which can be important in large scale data 
processing.
"""
def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_sequence()
for i in range(10):
    print(next(fib_gen))
print(type(fib_gen))    

#---------------------------------------------

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Create the plot
plt.plot(x, y)

# Set the axis labels
plt.xlabel('X axis label')
plt.ylabel('Y axis label')

# Set the title of the plot
plt.title('Title of the plot')

# Show the plot
plt.show()
