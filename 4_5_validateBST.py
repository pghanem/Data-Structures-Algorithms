class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

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

####### original solution, only checks each 3 node subtree for BST 
def validate(node):
    # base-base
    if node is None: return True

    #base, if we are at a leaf with no children, trivially it is a BST
    if node.left is None and node.right is None:
        return True
    elif node.left and node.left.val > node.val:
        return False
    elif node.right and node.right.val < node.val:
        return False
    else:
        return validate(node.left) and validate(node.right)



############# solution that uses an array
def valid(node):
    arr = []
    newArr = _valid(node, arr)
    for x in range(0, len(newArr)-2):
        if newArr[x] > newArr[x+1]:
            return False
    return True
    
def _valid(node, arr):
        
    if node:
        _valid(node.left, arr)
        arr.append(node.val)
        _valid(node.right, arr)

    return arr
#############       

############# solution that uses less memory

last = None
    
def validLess(node):
    global last
    if node == None: return True
        
    if node:
        validLess(node.left)
        if last is not None and node.val <= last:
            return False
        last = node.val
        validLess(node.right)

    return True
#############

############# my minmax solution
cmin = None
cmax = None

def val(node):
    global cmin
    global cmax
    # base-base
    if node is None: return True

    #base, if we are at a leaf with no children, trivially it is a BST
    if node.left is None and node.right is None:
        return True
    elif (node.left and node.left.val > node.val) or (cmax and node.left.val > cmax):
        return False
    elif (node.right and node.right.val < node.val) or (cmin and node.right.val < cmin):
        return False
    else:
        cmin = node.right.val
        cmax = node.left.val
        return validate(node.left) and validate(node.right)


#############

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
