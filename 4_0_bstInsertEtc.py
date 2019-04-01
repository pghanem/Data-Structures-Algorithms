class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if data < root.data:
        if root.left == None:
            print('Insert left')
            root.left = Node(data)
        else:
            print('Going left')
            insert(root.left, data)

    else:
        if root.right == None:
            print('Insert right')
            root.right = Node(data)
        else:
            print('Going right')
            insert(root.right, data)

    return

def searchBST(root, data):
    if data == root.data: return True
    
    if data < root.data:
        if root.left == None:
            return False
        else:
            return searchBST(root.left, data)
            
    if data > root.data:
        if root.right == None:
            return False
        else:
            return searchBST(root.right, data)

def delete(root, data):
    if data == root.data and root.left is None and root.right is None:
        root.data = None
    
    if data < root.data:
        if root.left == None:
            return False
        else:  
            return searchBST(root.left, data)
            
    if data > root.data:
        if root.right == None:
            return False
        else:
            return searchBST(root.right, data)
        

def preorder(root, order):
    order.append(root.data)
    if root.left is not None:
        preorder(root.left, order)
    if root.right is not None:
        preorder(root.right, order)
    return order

def inorder(root):
    if root.left is not None:
        inorder(root.left)
    print(root.data)
    if root.right is not None:
        inorder(root.right)
        
def postorder(root):
    if root.left is not None:
        postorder(root.left)
    if root.right is not None:
        postorder(root.right)
    print(root.data)

def subTree(root):
    subList = []
    subList = preorder(root, subList)
    print(subList)
    

def buildTree():
    root = Node(8)
    insert(root, 4)
    insert(root, 2)
    insert(root, 6)
    insert(root, 1)
    insert(root, 3)
    insert(root, 7)
    insert(root, 10)
    insert(root, 9)
    insert(root, 12)
    insert(root, 11)
    insert(root, 13)
    return root
