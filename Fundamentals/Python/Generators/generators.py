# 2/13/2023
# ---SoloLearn---
"""
Generators are a type of iterable, like lists or tuples.
Unlike lists, they don't allow indexing with arbitrary indices, but they can still
be iterated through with for loops.
They can be created using functions and the yield statement.

The yield statement is used to define a generator, replacing the return of a 
function to provide a result to its caller without destroying local variables.

"""

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

"""
Due to the fact that they 'yield' one item at a time, generators don't have the
memory restrictions of lists.
In fact, they can be infinite!
"""

# def infinite_sevens():
#     while True:
#         yield 7

# for i in infinite_sevens():
#     print(i)

"""
Fill in the blanks to create a prime number generator that yields all prime 
numbers in a loop. (Consider having an is_prime function already defined)
"""

def is_prime():
    return num

def get_prime():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
print(get_prime())

"""
Finite generators can be converted into lists by passing them as arguments
to the list function.

Using generators results in improved performance, which is the result of the
lazy (on demand) generation of values, which translates to lower memory usage.
Furthermore, we do not need to wait until all the elements have been generated
before we start to use them.
"""
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(numbers(11)))

"""
Finding prime numbers is a common coding interview task. The given code defines
a function isPrime(x), which returns True if x is prime. You need to create a
generator function isGenerator(), that will take two numbers as arguments, and
use the isPrime() function to output the prime numbers in the given range
(between the two arguments).

Sample Input:
10
20

Sample Output:
[11, 13, 17, 19]
"""

def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    num = f
    for num in range(num, t):
        if isPrime(num):
            yield num
    
# f = int(input("Enter first number: "))
# t = int(input("Enter last number: "))

# print(list(primeGenerator(f, t)))

"""
What is the result of this code?
"""
def make_word():
  word = ""
  for a in "spam":
    word += a
    yield word

print(list(make_word()))

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