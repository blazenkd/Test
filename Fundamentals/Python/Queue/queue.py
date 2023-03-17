'''
Queue

A queue is similar to a stack, but defines a different way to add and remove elements.
The elements are inserted from one end, called the rear, and deleted from the other end, called the front.
This behavior is called FIFO (First in First Out).

Terminology
The process of adding new elements into the queue is called enqueue.
The process of removal of an element from the queue is called dequeue.

Applications
Queues are used whenever we need to manage objects in order starting with the first one in.
Scenarios include printing documents on a printer, call center systems answering people on hold, and so on.

Let's implement the Queue class with it's corresponding enqueue, dequeue, is_empty and print methods.
We will use a list to store the elements.

The enqueue method adds an element at the beginning of the list, while the dequeue method removes the last element.
'''
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def print_queue(self):
        print(self.items)

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('42')
q.print_queue()

q.dequeue()
q.print_queue()

'''
You are making a call center application, which should handle customers in a queue.
The CallCenter class is implemented as a Queue. Each element of the queue has the topic of the call as its value. 
The two possible values are 'general' and 'technical'. A 'general' call takes on average 5 minutes to handle, 
while a 'technical' call requires 10 minutes.
The given code adds multiple customers to the Queue from user input.
You need to dequeue all added customers, calculate and output the total time required to handle all calls.
'''

class CallCenter:
    def __init__(self):
      self.customers = []

    def is_empty(self):
      return self.customers == []

    def add(self, x):
      self.customers.insert(0, x)

    def next(self):
      return self.customers.pop()


c = CallCenter()

while True:
    n = input()
    if n == 'end':
        break
    c.add(n)

#your code goes here
total_time = 0
while not c.is_empty():
    customer = c.next()
    if customer == 'general':
        total_time += 5
    elif customer == 'technical':
        total_time += 10

print("Total time required to handle all calls:", total_time, "minutes")