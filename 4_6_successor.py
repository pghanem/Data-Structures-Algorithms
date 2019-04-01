class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.parent = val * 100

class BT:
    def __init__(self):
        self.root = None
        
    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        
        if val < node.val:
            if node.left:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def print(self):
        if self.root:
            self._print(self.root)
    
    def _print(self, node):
        if node:
            self._print(node.left)
            print(node.val)
            self._print(node.right)
   
    def printDepth(self):
        count = 0
        if self.root:
            self._printDepth(self.root, count)

    def _printDepth(self, node, count):
        c = count
        if node:
            self._printDepth(node.left, c + 1)
            print('Node (' + str(node.val) + ') is at depth ' + str(c))
            self._printDepth(node.right, c + 1)

def CBT():
    bt = BT()
    bt.add(3)
    bt.add(7)
    bt.add(1)
    bt.add(13)
    bt.add(44)
    bt.add(22)
    bt.add(2)
    bt.add(8)
    bt.add(9)
    bt.add(12)
    bt.add(10)
    bt.add(4)
    bt.add(5)
    return bt
    
def CBT2():
    bt = BT()
    bt.root = Node(5)
    bt.root.right = Node(7)
    bt.root.left = Node(3)
    bt.root.left.right = Node(6)
    return bt

def BST():
    bt = BT()
    bt.add(3)
    bt.add(1)
    bt.add(5)
    bt.add(0)
    bt.add(2)
    bt.add(4)
    bt.add(7)
    bt.add(6)
    bt.add(9)
    bt.add(8)
    return bt

######## first naive solution using an array
def successor(node, val):
    arr = []
    newArr = _successor(node, val, arr)
    for x in range(0, len(arr)-1):
        if arr[x] == val:
            return arr[x+1]
    
    return False

def _successor(node, val, arr):
    if node:
        _successor(node.left, val, arr)
        arr.append(node.val)
        _successor(node.right, val, arr)

    return arr
##############

######### better soln. using inorder and logic: successor is leftmost node of the right subtree.

def find(node, val):
    if node is None or node.val == val:
        if node.right:
            return findLeft(node.right)
        elif node.right is None and node.left is None:
            while node.parent < val:
                node = node.parent
            return node
    elif val > node.val: return find(node.right, val)
    else: return find(node.left, val)
    
def findLeft(node):
    while node.left:
        node = node.left
    return node.val
    
    


    
