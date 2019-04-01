class Node():
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
        
        if val < node.val and node.left:
            self._add(val, node.left)
        elif val > node.val and node.right:
            self._add(val, node.right)
        elif val < node.val:
            self.root.left = node
        else:
            self.root.right = node
