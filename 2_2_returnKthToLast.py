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

# my first naive solution, 2 passes, one for count and one to find node
def kthtolast(llist, k):
    current = llist.head
    count = 0
    while current:
        count += 1
        current = current.get_next()

    if k > count or k < 1: return False
    else:
        current = llist.head
        for x in range(0, count - k):
            current = current.get_next()
    return current.get_data()

# a better, one pass iterative solution with two pointers
def kthbetter(llist, k):
    if k < 1: return False
    current = llist.head
    runner = llist.head

    for x in range(0, k):
        runner = runner.get_next()

    while runner:
        current = current.get_next()
        runner = runner.get_next()
        
    return current.get_data()
        
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
