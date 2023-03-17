'''
Linked List

A linked list is a sequence of nodes where each node stores its own data and a link to the next node.
One node links to another forming what can be thought of as a linked chain:contentImage
The first node is called the head, and it's used as the starting point for any iteration through the list. 
The last node must have its link pointing to None to determine the end of the list.

Unlike stacks and queues, you can insert and remove nodes in any position of the linked list (similar to a standard list).

Applications

Linked lists are useful when your data is linked. For example when you need undo/redo functionality, 
the nodes can represent the state with links to the previous and next states. 
Another example would be a playlist of music, where each clip is linked with the next one.

Linked List in Python

Each node will include data and the link to the next node.
Let's start by creating the Node class:
'''
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_front(self, data):
        self.head = Node(data, self.head)      

    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    def get_last_node(self):
        n = self.head
        while(n.next != None):
            n = n.next
        return n.data

    def is_empty(self):
        return self.head == None

    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end = " => ")
            n = n.next
        print()


s = LinkedList()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list()
print(s.get_last_node())

'''
You are making a Music Player, which allows you to create a playlist of tracks.
The given code defines Player and Track classes, where the Player is a linked list, 
chaining together Track objects.
The code takes a number of tracks from user input and adds them to the playlist.

You need to iterate over the linked list and output all the tracks in the playlist in the order of playback.
'''

class Track:
    def __init__(self, title, next):
        self.title = title
        self.next = next

class Player:
    def __init__(self):
        self.head = None

    def add(self, title):
        if not self.head:
            self.head = Track(title, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Track(title, None)


p = Player()
while True:
    x = input()
    if x == 'end':
        break
    p.add(x)

#your code goes here
curr = p.head
while curr:
    print(curr.title)
    curr = curr.next