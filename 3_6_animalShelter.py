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

# original solution with two lists
class Shelter:
     def __init__(self):
          self.cats = LinkedList()
          self.dogs = LinkedList()
          self.hashmap = {}
          self.pos = 0

     def isEmpty(self):
          return self.cats.size() == 0 and self.dogs.size == 0

     def enqueue(self, name, species):
          self.hashmap[name] = self.pos
          self.pos += 1
          if species == 0:
               self.cats.insert(name)
          if species == 1:
               self.dogs.insert(name)

     def dequeueAny(self):
          cat = self.cats.head
          dog = self.dogs.head
          while cat:
               cat = cat.next_node
          while dog:
               dog = dog.next_node

          if self.hashmap[dog.data] < self.hashmap[cat.data]:
               dequeueDog()
          else:
               dequeueCat()

     def dequeueCat(self):
          cat = self.cats.head.next_node
          prev = self.cats.head
          while cat.next_node:
               cat = cat.next_node
               prev = prev.next_node
          print(prev.next_node.data)
          prev.next_node = None
          

     def dequeueDog(self):
          dog = self.dogs.head.next_node
          prev = self.dogs.head
          while dog:
               dog = dog.next_node
               prev = prev.next_node
          print(prev.next_node.data)
          prev.next_node = None

     def peek(self):
          if self.isEmpty(): raise ValueError('Empty queue')
          return self.items[-1]

     def size(self):
          return len(self.items)




     
