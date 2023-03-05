'''
List Comprehensions

List comprehensions are a useful way of quickly creating lists whose contents obey a rule.
For example, we can do the following:

List comprehensions are inspired by set-builder notation in mathematics.
'''
# a list comprehension
cubes = [i**3 for i in range(5)]

print(cubes)

'''
What does this list comprehension create?
'''
nums = [i*2 for i in range(10)]
print(nums)

'''
A list comprehension can also contain an if statement to enforce a condition on values in the list.
Example:
'''
evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)

'''
The number of insects in a lab doubles in size every month.
Take the initial number of insects as input and output a list, showing the number of insects for each of the next 12 months, starting with 0, which is the initial value.
So, the resulting list should contain 12 items, each showing the number of insects at the beginning of that month.

Sample Input:
10

Sample Output:
[10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480]

Create a list comprehension to generate the required list.
The formula to calculate the number of insects after N months will be: count*2ᴺ, where count is the initial number of insects.
'''

x = int(input())
pop = [x * 2 ** i for i in range(12)]
print(pop)

'''
Create a list of multiples of 3 from 0 to 20.
'''
a = [i for i in range(20) if i % 3 == 0]
print(a)