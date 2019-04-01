class SetOfStacks:
     def __init__(self):
          self.stacks = []

     def isEmpty(self):
          return self.stacks == []

     def push(self, item):
          if self.isEmpty() or len(self.stacks[-1]) >= 10:
               self.stacks.append([item])
          else:
               self.stacks[-1].append(item)

     def pop(self):
          if self.isEmpty(): raise ValueError('Empty stack')
          else:
               if len(self.stacks[-1]) == 1:
                    self.stacks.pop()
               else: self.stacks[-1].pop()

     def peek(self):
          if self.isEmpty(): raise ValueError('Empty stack')
          else:
               return self.stacks[-1][-1]
          
     def popAt(self, index):
          if self.isEmpty(): raise ValueError('Empty stack')
          else:
               if len(self.stacks[index]) == 1:
                    del self.stacks[index]
               else:
                    self.stacks[index].pop()
          
     def size(self):
          return len(self.stacks)

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




     
