# 2/26/2023
# ---SoloLearn---
"""
Reading Files

The contents of a file that has been opened in text mode can be read using the read method. 
We have created a books.txt file on the server which includes titles of books. 
Let's read the file and output the content:
"""

file = open("/usercode/files/books.txt")
cont = file.read()
print(cont)
file.close()

'''
To read only a certain amount of a file, you can provide the number of bytes to read as an argument to the read function. 
Each ASCII character is 1 byte: 
'''
file = open("/usercode/files/books.txt")
print(file.read(5))
print(file.read(7))
print(file.read())
file.close()

'''
To retrieve each line in a file, you can use the readlines() method to return a list in which each element is a line in the file.
'''
file = open("/usercode/files/books.txt")
for line in file.readlines():
    print(line)
file.close()
'''
If you do not need the list for each line, you can simply iterate over the file variable:
'''
file = open("/usercode/files/books.txt")
for line in file:
    print(line)
file.close()

# -----------------------------------------------------------------------------------------
# My Spin
# -----------------------------------------------------------------------------------------

