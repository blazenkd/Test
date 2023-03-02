'''
Lists are used to store multiple elements, each corresponding to an index.

They are created using square brackets.
For example:
The names list contains three strings. Each element of the list can be accessed using its index:
This will output the 2nd element of the list.
'''
names = ["James", "Tom", "Amy"] 
print(names[1])

'''
Lists can be used to represent a collection of data, for example ages of people, monthly growth rates of stocks, etc.

Lists can also be nested to represent 2D grids, such as matrices:
The code below outputs the 3rd item of the 2nd row.
A matrix-like structure can be used in cases where you need to store data in row-column format.
'''
m = [
    [1,2,3],
    [4,5,6]
    ]
    
print(m[1][2]) 

x = [
  [2, 4, 6],
  [8, 6, 4]
]
print(x[0][2]+x[1][2])