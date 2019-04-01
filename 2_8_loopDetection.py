
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

# original naive solution that uses some extra memory but does it in O(n) time
def loopdetection(llist):
    current = llist.head
    hashmap = {}
    while current:
        if current in hashmap:
            return current
        else:
            hashmap[current] = ''
            current = current.next_node
    return False

# second better solution that uses a runner and no extra space
def detector(llist):
    slow = llist.head
    fast = llist.head
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow == fast:
            break

    
    if fast is None or fast.next_node is None:
        return False

    slow = llist.head
    while slow != fast:
        slow = slow.next_node
        fast = fast.next_node
        
    return fast
        
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
