Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===== RESTART: /Users/Peter/Documents/Python Scripts/4_3_listOfDepths.py =====
>>> CBT()
<__main__.BT object at 0x105ecfd30>
>>> new = CBT()
>>> mylist = listOfDepths(new)
>>> print(mylist)
[<__main__.LinkedListNode object at 0x105ee4278>, <__main__.LinkedListNode object at 0x105ee4fd0>, <__main__.LinkedListNode object at 0x105eed0b8>, <__main__.LinkedListNode object at 0x105eed198>, <__main__.LinkedListNode object at 0x105eed2b0>, <__main__.LinkedListNode object at 0x105eed358>, <__main__.LinkedListNode object at 0x105eed3c8>, <__main__.LinkedListNode object at 0x105eed438>]
>>> mylist.print()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    mylist.print()
AttributeError: 'list' object has no attribute 'print'
>>> mylist.print()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    mylist.print()
AttributeError: 'list' object has no attribute 'print'
>>> mylist[0].print()
None
6
>>> mylist[1].print()
None
3
7
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_3_checkBalanced.py ====
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_3_checkBalanced.py ====
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_3_checkBalanced.py ====
>>> mylist = BT()
>>> mylist.insert(3)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    mylist.insert(3)
  File "/Users/Peter/Documents/Python Scripts/4_3_checkBalanced.py", line 13, in insert
    insertHelp(self, node)
NameError: name 'insertHelp' is not defined
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_3_checkBalanced.py ====
>>> ml = BT()
>>> ml.insert(4)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ml.insert(4)
  File "/Users/Peter/Documents/Python Scripts/4_3_checkBalanced.py", line 13, in insert
    insertHelp(node)
NameError: name 'insertHelp' is not defined
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_3_checkBalanced.py ====
>>> ml = BT()
>>> ml.insert(4)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ml.insert(4)
  File "/Users/Peter/Documents/Python Scripts/4_3_checkBalanced.py", line 13, in insert
    self.insertHelp(node)
TypeError: insertHelp() takes 1 positional argument but 2 were given
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_3_checkBalanced.py ====
>>> ml = BT()
>>> ml.insert(4)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    ml.insert(4)
  File "/Users/Peter/Documents/Python Scripts/4_3_checkBalanced.py", line 13, in insert
    node.insertHelp()
AttributeError: 'Node' object has no attribute 'insertHelp'
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_3_checkBalanced.py ====
>>> l = BT()
>>> l.insert(3)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l.insert(3)
  File "/Users/Peter/Documents/Python Scripts/4_3_checkBalanced.py", line 13, in insert
    insertHelp(node)
NameError: name 'insertHelp' is not defined
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_3_checkBalanced.py ====
>>> bt = BT()
>>> bt.insert(3)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    bt.insert(3)
AttributeError: 'BT' object has no attribute 'insert'
>>> bt.add(3)
>>> bt.add(5)
>>> bt.add(1)
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = BT()
>>> bt.add(3)
>>> bt.add(1)
>>> bt.add(0)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    bt.add(0)
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 15, in add
    self._add(val, self.root)
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 20, in _add
    self._add(val, node.left)
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 20, in _add
    self._add(val, node.left)
b  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 20, in _add
    self._add(val, node.left)
  [Previous line repeated 989 more times]
t  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 19, in _add
    if val < node.val and node.left:
RecursionError: maximum recursion depth exceeded in comparison
>>> bt.add(2)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    bt.add(2)
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 15, in add
    self._add(val, self.root)
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 20, in _add
    self._add(val, node.left)
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 20, in _add
    self._add(val, node.left)
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 20, in _add
    self._add(val, node.left)
  [Previous line repeated 989 more times]
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 19, in _add
    if val < node.val and node.left:
RecursionError: maximum recursion depth exceeded in comparison
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = BT()
>>> bt.add(3)
>>> bt.add(1)
>>> bt.add(5)
>>> bt.add(2)
>>> bt.add(0)
>>> bt.add(4)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    bt.add(4)
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 15, in add
    self._add(val, self.root)
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 26, in _add
    self._add(val, node.r)
AttributeError: 'Node' object has no attribute 'r'
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = BT()
>>> bt.add(3)
>>> bt.add(1)
>>> bt.add(5)
>>> bt.add(2)
>>> bt.add(0)
>>> bt.add(4)
>>> bt.add(6)
>>> bt.print
<bound method BT.print of <__main__.BT object at 0x10a524cf8>>
>>> bt.print()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    bt.print()
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 31, in print
    if self.left:
AttributeError: 'BT' object has no attribute 'left'
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = BT()
>>> bt.add(3)
>>> bt.add(1)
>>> bt.add(5)
>>> bt.add(2)
>>> bt.add(4)
>>> bt.root.print()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    bt.root.print()
AttributeError: 'Node' object has no attribute 'print'
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = BT()
>>> bt.add(3)
>>> bt.add(1)
>>> bt.add(5)
>>> print(bt)
<__main__.BT object at 0x109c57d30>
>>> bt.print()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    bt.print()
TypeError: print() missing 1 required positional argument: 'node'
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = BT()
>>> bt.add(3)
>>> bt.add(1)
>>> bt.add(5)
>>> bt.print()
1
3
5
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> 
KeyboardInterrupt
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = BT()
>>> bt.add(3)
>>> bt.add(1)
>>> bt.add(5)
>>> ct.check()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    ct.check()
NameError: name 'ct' is not defined
>>> bt.check()
1
3
5
0
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = BT()
>>> bt.add(3)
>>> bt.add(1)
>>> bt.add(5)
>>> bt.check()
1
1
3
0
5
1
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = BT()
>>> bt.add(3)
>>> bt.add(1)
>>> bt.add(5)
>>> bt.check()
1
1
3
0
5
1
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = CBT()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    bt = CBT()
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 54, in CBT
    bt = BT(6)
TypeError: __init__() takes 1 positional argument but 2 were given
>>> CBT()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    CBT()
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 54, in CBT
    bt = BT(6)
TypeError: __init__() takes 1 positional argument but 2 were given
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = CBT()
>>> bt.print()
1
2
3
4
5
7
8
9
10
12
13
22
44
>>> bt.check()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    bt.check()
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 43, in check
    self._check(self.root, count)
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 48, in _check
    self._check(node.left, c + 1)
  File "/Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py", line 49, in _check
    print('Node: ' + node.val)
TypeError: can only concatenate str (not "int") to str
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt.check()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    bt.check()
NameError: name 'bt' is not defined
>>> bt = CBT()
>>> bt.check()
Node: 1
Count: 1
Node: 2
Count: 2
Node: 3
Count: 0
Node: 4
Count: 2
Node: 5
Count: 3
Node: 7
Count: 1
Node: 8
Count: 3
Node: 9
Count: 4
Node: 10
Count: 6
Node: 12
Count: 5
Node: 13
Count: 2
Node: 22
Count: 4
Node: 44
Count: 3
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = CBT()
>>> bt.check()
Node (1) is at depth 1
Node (2) is at depth 2
Node (3) is at depth 0
Node (4) is at depth 2
Node (5) is at depth 3
Node (7) is at depth 1
Node (8) is at depth 3
Node (9) is at depth 4
Node (10) is at depth 6
Node (12) is at depth 5
Node (13) is at depth 2
Node (22) is at depth 4
Node (44) is at depth 3
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = CBT()
>>> bt.check()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    bt.check()
AttributeError: 'BT' object has no attribute 'check'
>>> bt.printDepth()
Node (1) is at depth 1
Node (2) is at depth 2
Node (3) is at depth 0
Node (4) is at depth 2
Node (5) is at depth 3
Node (7) is at depth 1
Node (8) is at depth 3
Node (9) is at depth 4
Node (10) is at depth 6
Node (12) is at depth 5
Node (13) is at depth 2
Node (22) is at depth 4
Node (44) is at depth 3
>>> 
==== RESTART: /Users/Peter/Documents/Python Scripts/4_4_checkBalanced.py ====
>>> bt = CBT()
>>> isBalanced(bt.root)
False
>>> nt = BT()
>>> nt.add(1)
>>> isBalanced(bt.root)
False
>>> isBalanced(nt.root)
True
>>> nt.add(0)
>>> nt.add(2)
>>> isBalanced(nt.root)
True
>>> getHeight(nt.root)
1
>>> getHeight(nt.root.left)
0
>>> nt.add(4)
>>> nt.add(3)
>>> nt.getHeight(nt.root)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    nt.getHeight(nt.root)
AttributeError: 'BT' object has no attribute 'getHeight'
>>> getHeight(nt.root)
3
>>> 
=== RESTART: /Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py ===
>>> l = [1, 2, 3, 4, 5]
>>> sumlist(l)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    sumlist(l)
  File "/Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py", line 7, in sumlist
    total = sumList(l[length - 1])
NameError: name 'sumList' is not defined
>>> 
=== RESTART: /Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py ===
>>> l = [1,2,3,4]
>>> sumlist(l)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    sumlist(l)
  File "/Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py", line 7, in sumlist
    total = sumlist(l[length - 1])
  File "/Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py", line 3, in sumlist
    length = len(l) - 1
TypeError: object of type 'int' has no len()
>>> print(l)
[1, 2, 3, 4]
>>> 
=== RESTART: /Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py ===
>>> l = [1,2,3,4]
>>> sumlist(l)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    sumlist(l)
  File "/Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py", line 3, in sumlist
    if length == 1:
NameError: name 'length' is not defined
>>> 
=== RESTART: /Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py ===
>>> l = [1,2,3,4,5]
>>> sumlist(l)
>>> 
=== RESTART: /Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py ===
>>> l = [1,2,3,4,5]
>>> sumlist(1)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    sumlist(1)
  File "/Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py", line 3, in sumlist
    if len(l) == 1:
TypeError: object of type 'int' has no len()
>>> 
=== RESTART: /Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py ===
>>> l = [1,2,3,4,5]
>>> sumlist(l)
6
>>> sumlist(l)
6
>>> 
=== RESTART: /Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py ===
>>> l = [1,2,3,4]
>>> sumlist(l)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    sumlist(l)
  File "/Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py", line 6, in sumlist
    return sumlist(mylist[1:len(mylist)-1])
  File "/Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py", line 6, in sumlist
    return sumlist(mylist[1:len(mylist)-1])
  File "/Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py", line 6, in sumlist
    return sumlist(mylist[1:len(mylist)-1])
  [Previous line repeated 990 more times]
  File "/Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py", line 3, in sumlist
    if len(mylist) == 1:
RecursionError: maximum recursion depth exceeded while calling a Python object
>>> 
=== RESTART: /Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py ===
>>> l = [1,2,3,4,5]
>>> sumlist(l)
15
>>> 
=== RESTART: /Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py ===
>>> l = [1,2,3,4,5,6]
>>> sumlist(l)
21
>>> listsum(1)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    listsum(1)
  File "/Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py", line 10, in listsum
    for element in mylist:
TypeError: 'int' object is not iterable
>>> listsum(l)
21
>>> l = [[1,2],[3,4],[5,6], 7, 8, [9, 10]]
>>> sumlist[l]
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    sumlist[l]
TypeError: 'function' object is not subscriptable
>>> sumlist(l)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    sumlist(l)
  File "/Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py", line 6, in sumlist
    return mylist[0] + sumlist(mylist[1:])
  File "/Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py", line 6, in sumlist
    return mylist[0] + sumlist(mylist[1:])
  File "/Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py", line 6, in sumlist
    return mylist[0] + sumlist(mylist[1:])
  [Previous line repeated 2 more times]
TypeError: unsupported operand type(s) for +: 'int' and 'list'
l
>>> listsum(l)
55
>>> 
=== RESTART: /Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py ===
>>> l = [1,2,3,4,5]
>>> listsum(l)
15
>>> l = [[1,2],[3,4,5]]
>>> listsum(l)
15
>>> 
=== RESTART: /Users/Peter/Documents/Python Scripts/4_0_recursionPractic.py ===
>>> fact(10)
3628800
>>> fact(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
>>> fact(5)
120
>>> 
