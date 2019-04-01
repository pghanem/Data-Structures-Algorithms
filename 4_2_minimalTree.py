class Graph:
    def __init__(self, n):
        self.nodes = n

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def visit(node):
    print(node.data)

def minimalTree(array):
    firsthalf = array[0 : len(array) - 1 // 2]
    secondhalf = array[len(array) - 1 // 2 + 1 : len(array) - 1]


    node = Node(array[len(array) // 2])
    if len(firsthalf) == 1:
        return node.children
    if len(secondhalf) == 1:
        return
    
    node.children.append(minimalTree(firsthalf))
    node.children.append(minimalTree(secondhalf))

def minTree(array):
    return minRecurse(array, 0, len(array) - 1)

def minRecurse(array, start, end):
    if end < start:
        return None

    mid = (start + end) // 2
    n = Node(array[mid])
    
    n.left = minRecurse(array, start, mid - 1)
    n.right = minRecurse(array, mid + 1, end)

    return n

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 2) + fib(n - 1)

