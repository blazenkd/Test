# ---SoloLearn---
'''
Lists Functions:

Lists support the following functions:

  # append(item) adds an item to the end of the list.
  # insert(index, item) adds an item at the given index in the list.
  # remove(item) removes an item from the list.
  # pop(index) removes the item at the given index.
  # count(item) returns a count of how many times an item occurs in the list.

Elements that are after the inserted item are shifted to the right.
'''

x = [2, 4, 6]
x.append(8)
x.remove(4)
x.insert(0, 8)

print(x)

print(x.count(8)) 

# What is the output of this code?
x = [3, 1, 2, 5, 3, 1]
x.append(8)
x.insert(2, 6)
x.remove(2)
print(len(x))

'''
# reverse() reverses items in the list.
# sort() sorts the list. By default, the list is sorted ascending. You can specify reverse=True as the parameter, to sort descending.
# max(list) returns the maximum value.
# min(list) returns the minimum value.

Note, that the reverse() and sort() functions change the list they are called on.
'''
x = [2, 4, 6, 8]
x.reverse()
print(x)

x.sort()
print(x)

print(min(x))
print(max(x))

'''
You are analyzing house prices. The given code declares a list with house prices in the neighborhood.
You need to calculate and output the number of houses that have a price that is above the average.

To calculate the average price of the houses, you need to divide the sum of all prices by the number of houses.
Use sum(list) to calculate the sum of all items in the list and len(list) to get the number of items.
'''
prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]

count = 0
total = sum(prices)
houses = len(prices)
avg = total / houses
for i in prices:
  if i > avg:
    count += 1
print("Houses above avg price: ", count)

# What is the output of this code?
x = [8, 5, 42, 11, 20, 4]
x.sort()
print(max(x)-min(x)+x[2])