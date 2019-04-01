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

# first solution, O(n + m) since it runs through both lists
def sumlist1(list1, list2):
    total = 0
    multiplier = 1

    current = list1.head
    while current:
        total += current.data * multiplier
        multiplier = multiplier * 10
        current = current.next_node

    multiplier = 1

    current = list2.head
    while current:
        total += current.data * multiplier
        multiplier = multiplier * 10
        current = current.next_node

    newList = LinkedList()

    for x in str(total):
        newList.insert(int(x))
        
    printlist(newList)

# follow up solution, O(n + m) since it runs through both lists
def sumlist2(list1, list2):
    total = 0
    maxlen = max(list1.size(), list2.size())
    print(maxlen)
    multiplier = 10 ** (maxlen - 1)

    current = list1.head
    while current:
        print(multiplier)
        total += current.data * multiplier
        multiplier = multiplier // 10
        current = current.next_node

    multiplier = 10 ** (maxlen - 1)

    current = list2.head
    while current:
        print(multiplier)
        total += current.data * multiplier
        multiplier = multiplier // 10
        current = current.next_node

    print(total)

    newList = LinkedList()

    for x in range(len(str(total)) -1, -1, -1):
        newList.insert(str(total)[x])
        
    printlist(newList)


# one pass solution
def sumlist3(n1, n2):
    n = Node(-1)
    head = n

    carry = 0
    while(n1 or n2 or carry != 0):
        total = 0
        if n1:
            total += n1.data
            n1 = n1.next_node
        if n2:
            total += n2.data
            n2 = n2.next_node
        if carry != 0:
            total += carry
        digit = total % 10
        carry = total // 10
        n.next_node = Node(digit)
        n = n.next_node
        
    current = head
    while current:
        print(current.data)
        current = current.next_node
    
        
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

