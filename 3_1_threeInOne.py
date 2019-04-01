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
         return self.items[len(self.items)-1]

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


def threeInOne():
     #this could be done with an array of fixed size 3, with a linked list
     # at each index representing a stack. each individual stack could be
     # accessed from that index in the array and assuming your implementation
     # of the linked list adds and removes nodes at the same side, it is a
     # way of creating 3 stacks from a single array.

     # another way to do this is to have a circular array that starts by
     # splitting the array into thirds, one for each stack. when a stack
     # outgrows its third, the start index of the other arrays shifts up
     # and data is inserted in that spot.


     
