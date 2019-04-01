class Stack:
     def __init__(self):
          self.items = []

     def isEmpty(self):
          return self.items == []

     def push(self, item):
          self.items.append(item)

     def pop(self):
          if self.isEmpty(): raise ValueError('Empty stack')
          else:
               return self.items.pop()

     def peek(self):
          if self.isEmpty(): raise ValueError('Empty stack')
          else:
               return self.items[-1]


def sortStack(s1):
     s2 = Stack()

     while not s1.isEmpty():
          # pop s1 into a temporary variable
          temp = s1.pop()
          # pop things out of s2 until you find the right spot
          while not s2.isEmpty() and s2.peek() > temp:
               s1.push(s2.pop())
          # insert the temp
          s2.push(temp)
     # repeat

     # copy s2 over to s1
     while not s2.isEmpty():
          s1.push(s2.pop())

     print(s1.items)
     

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




     
