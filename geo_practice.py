def insort(l, val):
    
    mid = len(l)// 2

    if l[mid] == val:
        return True
    elif l[mid] > val:
        insort(l[:mid-1], val)
    elif l[mid] < val:
        insort(l[mid+1:], val)
    else:
        return False

def binarySearch(seq, t):
    left = 0
    right = len(seq) - 1
    while True:
        if right < left:
            return False
        m = (left + right) // 2
        if seq[m] < t:
            left = m + 1
        elif seq[m] > t:
            right = m - 1
        else:
            return m

def pal(s):
    arr = [False] * 128
    if len(s) <= 1:
        return True
    for x in s:
        arr[ord(x)] = not arr[ord(x)]

    print(arr)

    val = 0
    for x in arr:
        if x == True:
            val += 1

    print(val)
    return val % 2 is 0 or val is 1
        

def zeros(arr):
    arr = [[1,1,1,1,1,1,1],
           [0,1,1,1,1,0,1],
           [1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1]]

    rows = len(arr)
    cols = len(arr[0])
    hashmap = {}
    for x in range(rows):
        for y in range(cols):
            if arr[x][y] == 0:
                hashmap[x] = y
    print(hashmap)

    for x in range(rows):
        for y in range(cols):
            if y in hashmap.values() or x in hashmap:
                arr[x][y] = 0

    print(arr)

