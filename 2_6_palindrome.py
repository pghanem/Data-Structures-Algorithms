
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
        
class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count +=1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in list')
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in list')
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


# first solution that uses a stack. iterate over LL and push current onto stack.
# then iterate over LL again and pop from stack comparing to current. O(N) time and memory.
def palindrome(llist):
    stack = []
    current = llist.head
    while current:
        stack.append(current.data)
        current = current.next_node

    current = llist.head
    while current:
        if stack.pop() != current.data: return False
        current = current.next_node
    return True

# second solution done by reversing the list
def palindrome2(llist):
    backwards = reverseAndClone(llist.head)
    return isEqual(llist.head, backwards)

def reverseAndClone(node):
    head = None
    while node:
        n = Node(node.data)
        n.next_node = head
        head = n
        node = node.next_node
    return head

def isEqual(node1, node2):
    while node1 and node2:
        if node1.data != node2.data: return False
        node1 = node1.next_node
        node2 = node2.next_node
    return node1 == None and node2 == None


def printlist(llist):
        current = llist.head
        while current:
            print(current.data)
            current = current.next_node
    

def addvals(mylist):
    mylist.insert(5)
    mylist.insert(5)
    mylist.insert(5)
    mylist.insert(3)
    mylist.insert(3)
    mylist.insert(2)
    mylist.insert(1)
    print(mylist.size())

def addvals2(mylist):
    mylist.insert(5)
    mylist.insert(3)
    mylist.insert(2)
    mylist.insert(1)
    mylist.insert(2)
    mylist.insert(3)
    mylist.insert(5)
    print(mylist.size())
