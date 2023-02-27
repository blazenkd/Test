# 2/26/2023
# ---SoloLearn---
"""
Files Summary
"""

'''
In this code, the open() function is used to open the file named "newfile.txt" in binary write mode. 
The second argument "wb" specifies the mode in which the file should be opened. 
The "w" indicates that the file should be opened in write mode, and the "b" indicates that the file should 
be opened in binary mode. The combination of "w" and "b" mode allows you to write binary data to the file.
'''
open("newfile.txt", "wb")


'''
In this code, the try statement is used to attempt to open the file named "newfile.txt"" using the open() 
function. The with statement is used to ensure that the file is automatically closed when you are done 
reading from it. The f.read() method is used to read the contents of the file and print them to the console. If an exception occurs while attempting to open or read the file, the except statement is executed, and an error message is printed to the console.
'''

try:
    with open("newfile.txt") as f:
        print(f.read())
except:
    print("Error: could not open or read file.")

'''
In this code, the open() function is used to open the file named "records.txt" in read mode. 
The file object is assigned to the variable f. The f.read() method is used to read the contents of the 
file into the variable cont. The len() function is used to get the number of characters in the contents 
of the file, which is printed to the console using the print() function. Finally, the f.close() method 
is used to close the file when you are finished reading from it.
'''

f = open("newfile.txt", "r")
cont = f.read()
print(len(cont))
f.close()