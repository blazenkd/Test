# 2/11/2023
# ---SoloLearn---
def foo(x,y):
    if x > y:
        return x
    else:
        return y
x = foo(4,7)
print(x)

def max(x, y):
    if x >= y:
        return x
    else:
        return y

if max(6,4) > 10:
    print("Yes")
else:
    print("Nope")

def shortest_string(x, y):
    if len(x) <= len(y):
        return x
    else:
        return y
result_1 = shortest_string("cat", "doggy")
print(result_1)

def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")
print(add_numbers(4, 5))

def double(a, b):
    return [a*2, b*2]
x = double(6, 9)
print(x)

def area(x, y):
    return x * y

def sum(x):
    res = 0
    for i in range(x):
        res += i
    return res
print(sum(4))

def print_num(x):
    for i in range(x):
        print(i)
        return
print_num(10)

n = [2, 4, 6, 8]
res = 1
for x in n[1:3]:
    res *= x
print(res)

car = {
    'brand' : 'BMW',
    'year' : 2018,
    'color' : 'red',
    'mileage' : 15000
}
# car_data = input("give attribute: ")
# print(car[car_data])
print(1500 in car)
print("red" in car)
print(2018 not in car)

fib = {
    1: 1,
    2: 1,
    3: 2,
    4: 3
}

print(fib.get(4,0))
print(fib.get(7,5))
# ------------------------
# contacts = [
#     ('James', 42),
#     ('Amy', 21),
#     ('John', 31),
#     ('Amanda', 63),
#     ('Bob', 19)
# ]

# def get_value(contacts, key):
#     for k, v in contacts:
#         if k == key:
#             return f"{key} is {v}"
#     return f"Not Found"

# input_key = input()
# print(get_value(contacts, input_key))

# data = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]

# def get_value(data, key):
#     for k, v in data:
#         if k == key:
#             return f"{key} is {v}"
#     return f"{key} not found"

# input_key = input("Enter key: ")
# print(get_value(data, input_key))

x, y = [1, 2]
x,y = y,x
print(x,y)

def calc(x):
    #your code goes here
    p = 4*side
    a = side**2
    return p, a
    

# # side = int(input())
# p, a = calc(side)

# print("Perimeter: " + str(p))
# print("Area: " + str(a))

a, b, c, d, *e, f, g = range(20)
print(len(e))

a = {1, 2, 3}
b = {0, 3, 4, 5}
print(a & b)

nums = [i*2 for i in range(10)]
print(nums)

# def non_vowels(word):
#     vowels = "aeiou"
#     return [letter for letter in word if letter.lower() not in vowels]

# word = input("Enter a word: ")
# result = non_vowels(word)
# print(result)

# word = input()

# vowels = ["a", "e", "i", "o", "u"]

# a = [i for i in word if i not in vowels]
# print(a)

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))

def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))

def my_func(f, arg):
  return f(arg)

print(my_func(lambda x: 2*x*x, 5))

nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)