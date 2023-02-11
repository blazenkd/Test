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