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