'''
Graph

Graphs are used to represent many real-life applications like networks, transportation paths of a city, 
and social network connections.

A graph is a set of connected nodes where each node is called a Vertex and the connection between two of 
them is called an Edge.

Here is an example graph:

This can represent, for example, connections on a social network, 
where each Vertex represents a person and the Edges represent connections.
'''

# A node of a graph is called a:
# Vertex

'''
A graph can be represented using a square matrix, where each element represents the 
edges: 0 indicates no edge, while 1 indicates an edge. The rows and columns represent the vertices.

For example:
0 1 1
1 0 0
1 0 0

The matrix above represents a graph with 3 vertices (that's why it's a 3x3 matrix).
The 1s represent the edges. There are 2 edges: the 1st vertex is connected with the 2nd and 3rd.
There are four 1s in the matrix, because if A is connected with B, then B is connected to A.

This type of matrix is called an adjacency matrix, because it shows if the corresponding vertices are adjacent or not.
'''

'''
Let's implement the Graph class:
'''
class Graph(): 
    def __init__(self, size): 
        self.adj = [ [0] * size for i in range(size)]
        self.size = size 
    
    def add_edge(self, orig, dest): 
        if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][dest-1] = 1 
            self.adj[dest-1][orig-1] = 1 
        
    def remove_edge(self, orig, dest): 
        if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][dest-1] = 0 
            self.adj[dest-1][orig-1] = 0 
            
    def display(self): 
        for row in self.adj: 
            print() 
            for val in row: 
                print('{:4}'.format(val),end="") 

#a sample Graph 
G = Graph(4) 
G.add_edge(1, 3) 
G.add_edge(3, 4)
G.add_edge(2, 4)
G.display()

'''
You are making a social network called X.
Connections between the users are stored as a graph.
The given code declares an X class with its add_friend() method and creates some connections for 5 users.

You need to take a number as input and output the number of connections of the corresponding user.
'''
class X(): 
    def __init__(self, size): 
        self.adj = [ [0] * size for i in range(size)]
        self.size = size 
    
    def add_friend(self, x, y): 
        if x > self.size or y > self.size or x < 0 or y < 0: 
            print("Error") 
        else: 
            self.adj[x-1][y-1] = 1 
            self.adj[y-1][x-1] = 1 
        
    def remove_friend(self, x, y): 
        if x > self.size or y > self.size or x < 0 or y < 0: 
            print("Error") 
        else: 
            self.adj[x-1][y-1] = 0 
            self.adj[y-1][x-1] = 0 
            

x = X(5)

x.add_friend(1, 3) 
x.add_friend(1, 5)
x.add_friend(2, 5)
x.add_friend(2, 4)
x.add_friend(4, 5)

n = int(input())
#your code goes here
if n > x.size or n < 1:
    print("Invalid user")
else:
    connections = sum(x.adj[n-1])
    print(f"User {n} has {connections} connections")

# True or False: for any "x" and "y" in an adjacency matrix "m", m[x][y] == m[y][x] 
'''
True. In an undirected graph, the adjacency matrix is symmetric. 
This means that if there is an edge from vertex x to vertex y, then there is also an edge from vertex y to vertex x. 
Therefore, m[x][y] and m[y][x] will have the same value, which will be 1 if there is an edge between the vertices, and 0 otherwise.
'''