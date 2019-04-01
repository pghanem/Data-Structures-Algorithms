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

# code to remove duplicates given a list, produces a new list with no dupes
def removeDups(llist):
    hashMap = {}
    current = llist.head
    while current:
        hashMap[str(current.data)] = ''
        current = current.next_node

    newlist = LinkedList()
    for x in hashMap:
        newlist.insert(x)

    llist = newlist
    printlist(llist)
    return llist

# code to remove duplicates with no temporary buffer, BCR is O(n^2)
def removeDupsBF(llist):
    current = llist.head
    other = current.next_node
    prev = current
    while current:
        while other:
            if current.data == other.data:
                prev.next_node = other.next_node
                other = prev.next_node
            else:
                other = other.next_node
                prev = prev.next_node
                
        other = current.next_node
        current = current.next_node 
        prev = current

    printlist(llist)
    return llist

# remove duplicates in one pass with buffer
def removeSoln(llist):
    current = llist.head
    hashmap = {}
    previous = None
    while current:
        if current.data in hashmap:
            previous.next_node = current.next_node
        else:
            hashmap[current.data] = ''
            previous = current

        current = current.next_node
    printlist(llist)
    return llist


# remove dupes in one pass without buffer (runner technique)
def removeSolnBF(llist):
    current = llist.head
    while current:
        runner = current
        while runner.next_node != None:
            if runner.next_node.data == current.data:
                runner.next_node = runner.next_node.next_node
            else:
                runner = runner.next_node
        current = current.next_node
    printlist(llist)
    return llist


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

