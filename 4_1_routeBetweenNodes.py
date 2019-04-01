from enum import Enum

class Graph:
    def __init__(self, n):
        self.nodes = n

class State(Enum):
    Unvisited = 1
    Visited = 2
    Visiting = 3

class Node:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.marked = False
        self.state = State.Unvisited
        self.children = []


def visit(node):
    print(node.data)

# basic implementation of DFS. travels to children in the order they are in the list.
# marks nodes as visited as it goes, recursively calls DFS on all unvisited children
def DFS(root):
    if not root: return
    visit(root)
    root.visited = True
    for node in root.children:
        if node.visited == False:
            DFS(node)

# simple DFS recursive solution
def hasPath(s, d):
    hashmap = {}
    return routeDFS(s, d, hashmap)

def routeDFS(source, destination, visited):

    # if source has been visited we have a cycle, return False
    if source in visited:
        return False

    # add source to visited
    visited[source] = ''

    # if the source is our destination, return true
    # because we reached the destination by recursing
    # on the children and comparing

    # basically it travels down the children of the source
    # checking for each child, grandchild etc if it is the destination.
    # if it is, then there must be a path
    if source == destination:
        return True

    
    for child in source.children:
        if routeDFS(child, destination, visited):
            return True
    return False

######################################
######################################

# basic implementation of BFS. travels to children in the order they are in the list.
# marks root and adds it to the queue
# pops node from queue and prints it, adds its children to the queue and marks them
# repeat process
def BFS(root):
    queue = []
    
    root.marked = True
    queue.append(root)

    while not queue == []:
        root = queue.pop(0)
        visit(root)
        for node in root.children:
            if node.marked == False:
                node.marked = True
                queue.append(node)

def runBFS(s, d):
    visited = {}
    queue = []

    # initial step: if either node is Null return false
    # otherwise, mark s as visited and add it to the queue
    if s is None or d is None: return False
    visited[s] = ''
    queue.append(s)

    # while the queue is not empty, pop the element and check if it is d
    # if its d, return true (we reached destination
    # otherwise repeat process on unvisited children of n
    while not queue == []:
        n = queue.pop(0)
        if n == d: return True

        for child in n.children:
            if child not in visited:
                queue.append(child)
                visited[child] = ''
    return False

            
def resetNodes(g):
    for node in g.nodes:
        node.visited = False
        node.marked = False
    return g

def createTree():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n1.children = [n2]
    n2.children = [n3, n4]
    n3.children = []
    n4.children = [n5]
    n5.children = []
    n6.children = [n3]
    n7.children = [n3]
    n8.children = [n5, n9]
    n9.children = [n8]
    gr = Graph([n1,n2,n3,n4,n5,n6,n7,n8,n9])
    DFS(n1)
    print(' ')
    gr = resetNodes(gr)
    DFS(n4)
    print(' ')
    gr = resetNodes(gr)
    DFS(n7)
    print(' ')
    print('DFS ABOVE / BFS BELOW')
    print(' ')
    gr = resetNodes(gr)
    BFS(n1)
    print(' ')
    gr = resetNodes(gr)
    BFS(n4)
    print(' ')
    gr = resetNodes(gr)
    BFS(n7)
    gr = resetNodes(gr)
    gr = Graph([n1,n2,n3,n4,n5])
    return gr
    
