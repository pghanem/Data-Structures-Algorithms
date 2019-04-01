class Stack:
     def __init__(self):
          self.items = []

     def isEmpty(self):
          return self.items == []

     def push(self, item):
          self.items.append(item)

     def pop(self):
          return self.items.pop()

     def peek(self):
          return self.items[-1]
     
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
          return self.items[-1]

     def size(self):
          return len(self.items)

class MyQueue:
     def __init__(self):
          self.s1 = Stack()
          self.s2 = Stack()

     def isEmpty(self):
          return self.s1.size() == 0

     # enqueue is standard, push onto stack 1
     def enqueue(self, item):
          self.s1.push(item)

     def dequeue(self):
          # if the adjusted list is empty, bring in everything from the unajusted list
          # and pop them onto the adjusted list, return the last node of adjusted list
          if self.s2.size() == 0:
               while self.s1.size() >= 1:
                    self.s2.push(self.s1.pop())
          # return the correct value and pop it from the list
          return self.s2.pop()

     def peek(self):
          # if the adjusted list is empty, bring in everything from the unajusted list
          # and pop them onto the adjusted list, return the last node of adjusted list
          if self.s2.size() == 0:
               while self.s1.size() >= 1:
                    self.s2.push(self.s1.pop())
          # return the correct value
          return self.s2[-1]

     def size(self):
          return len(self.s2) + len(self.s2)
