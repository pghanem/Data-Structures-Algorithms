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

def getHeight(node):
    if node is None:
        return -1
    else:
        return 1 + max(getHeight(node.left), getHeight(node.right))
    

def isBalanced(node):

    heightDiff = getHeight(node.left) - getHeight(node.right)
    
    if abs(heightDiff) > 1:
        return False
    else:
        return isBalanced(node.left) and isBalanced(node.right)
    
            
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
    
