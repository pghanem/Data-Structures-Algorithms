class Stack:
     def __init__(self):
          self.items = []
          self.min = []

     def isEmpty(self):
          # returns true if list is empty, false otherwise
          return self.items == []

     def push(self, item):
          # appends the item first
          self.items.append(item)
          # if min list is empty, or the item is smaller than current min, append to min list
          if len(self.min) == 0 or item <= self.min[-1]:
               self.min.append(item)

     def pop(self):
          if self.isEmpty(): raise ValueError('Empty stack')
          else:
               if self.items[-1] == self.min[-1]:
                    self.min.pop()
               return self.items.pop()

     def peek(self):
          if self.isEmpty(): raise ValueError('Empty stack')
          else: return self.items[-1]

     def minimum(self):
          if self.isEmpty(): raise ValueError('Empty stack')
          return self.min[-1]

     def size(self):
          return len(self.items)

class Queue:
     def __init__(self):
          self.items = []

     def isEmpty(self):
          return self.items == []

     def enqueue(self, item):
          self.items.insert(0, item)

     def dequeue(self):
          return self.items.pop()

     def peek(self):
          return self.items[len(self.items)-1]

     def size(self):
          return len(self.items)




     
