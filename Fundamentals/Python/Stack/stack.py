'''
Stack:
A stack is a simple data structure that adds and removes elements in a particular order.
Every time an element is added, it goes on the "top" of the stack. Only an element at the top of the stack 
can be removed, just like a stack of plates. This behavior is called LIFO (Last In, First Out).

Terminology:
Adding a new element onto the stack is called push.
Removing an element from the stack is called pop.

Applications:
Stacks can be used to create undo-redo functionalities, 
parsing expressions (infix to postfix/prefix conversion), and much more.
'''

# The numbers 1, 2, 3 are pushed to the stack in the given order. Which number will be on top of the stack?
# 3

'''
Let's define and implement the Stack class with its corresponding push, pop, is_empty and print_stack methods.

We will use a list to store the data.

As you can see, it's easy to create a stack using a list.
We use a list called items to store our elements.
The push method adds an element at the beginning of the list, 
while the pop method removes the first element of the list.
Play around with the code and see the Stack working in action!
'''

class Stack:
    def __init__(self):
        self.items = []  
  
    def is_empty(self):
        return self.items == []
  
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def print_stack(self):
        print(self.items)
    
s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.print_stack()

s.pop()
s.print_stack()

'''
You need to make a back button for a browser.
You use a stack to store the website links visited. Each new link visited is pushed onto the stack.
The back button needs to pop the top link from the stack and navigate to it.

The given code declares a Browser class as a stack and implements some of its methods. 
Then, some links are pushed onto the stack.
A while loop is then used to go back to all links and print them.

Implement the required pop() method for the Browser, so that the given code works as expected.
Note, that the pop() method needs to return the value, so that it can be printed.
'''


class Browser:
    def __init__(self):
      self.links = []  
  
    def is_empty(self):
      return self.links == []
  
    def push(self, link):
      self.links.insert(0, link)

    def pop(self):
        return self.links.pop(0)
    
    
  
x = Browser()
x.push('about:blank')
x.push('www.sololearn.com')
x.push('www.sololearn.com/courses/')
x.push('www.sololearn.com/courses/python/')

while not x.is_empty():
    print(x.pop())

# What does calling list.pop(0) do?