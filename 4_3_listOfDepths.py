class LinkedListNode:
    next_node = None
    val = None

    def __init__(self, val):
        self.val = val

    def add(self, val):
        while self.next_node:
            self = self.next_node
        self.next_node = LinkedListNode(val)

    def print(self):
        while self:
            print(self.val)
            self = self.next_node

class BT:
    val = None
    left = None
    right = None

    def __init__(self, val):
        self.val = val

    def insert(self, val):
        if self.val == val: return
        
        if val > self.val and not self.right:
            self.right = BT(val)
        elif val < self.val and not self.left:
            self.left = BT(val)
        elif val > self.val and self.right:
            self.right.insert(val)
        else:
            self.left.insert(val)

def depth(tree):
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1
    else:
        depthL = 1 + depth(tree.left)
        depthR = 1 + depth(tree.right)
        if depthL > depthR: return depthL
        else: return depthR

def listOfDepths(root):
    if root is None: return
    q1 = []
    q2 = []
    llists = []
    q1.append(root)

    while not q1 == [] or not q2 == []:
        llist = LinkedListNode(None)
        while not q1 == []:
            root = q1.pop(0)
            llist.add(root.val)
            if root.left is not None: q2.append(root.left)
            if root.right is not None: q2.append(root.right)
            
        llists.append(llist)
        llist = LinkedListNode(None)
        while not q2 == []:
            root = q2.pop(0)
            llist.add(root.val)
            if root.left is not None: q1.append(root.left)
            if root.right is not None: q1.append(root.right)
        llists.append(llist)

    return llists

def printAll(lst):
    for x in lst:
        x.print()

def CBT():
    bt = BT(6)
    bt.insert(3)
    bt.insert(7)
    bt.insert(1)
    bt.insert(13)
    bt.insert(44)
    bt.insert(22)
    bt.insert(2)
    bt.insert(8)
    bt.insert(9)
    bt.insert(12)
    bt.insert(10)
    bt.insert(4)
    bt.insert(5)
    return bt
    



    
