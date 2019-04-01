
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

# first solution that uses a hashmap which has a bit of extra memory usage
def intersection(list1, list2):
    current1 = list1.head
    current2 = list2.head

    hashmap = {}

    while current1:
        hashmap[current1] = ''
        current1 = current1.next_node

    while current2:
        if current2 in hashmap:
            return current2
        else:
            current2 = current2.next_node

    return False

# second solution that finds the tail and len of each array, compares them to see if an intersection even exists
# if an intersection exists, it starts iterating over both lists (cuts off front of longer one) and checks
# if nodes are equal by reference as it goes.
def intersection2(list1, list2):
    current1 = list1.head
    current2 = list2.head
    len1 = 0
    len2 = 0
    while current1:
        len1 += 1
        current1 = current1.next_node

    while current2:
        len2 += 1
        current2 = current2.next_node

    if current1 != current2: return None

    current1 = list1.head
    current2 = list2.head
    if len1 > len2:
        for x in range(0, len1-len2):
            current1 = current1.next_node
    if len2 > len1:
        for x in range(0, len2-len1):
            current2 = current2.next_node

    while current1 != None and current2 != None:
        if current1 == current2: return current1
        else:
            current1 = current1.next_node
            current2 = current2.next_node
            
    return False

        
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
