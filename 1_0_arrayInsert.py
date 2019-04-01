def insertion(l, val):
    x = 0
    
    while x < len(l) and l[x] <= val:
        x += 1
    l.insert(x, val)

    print(l)


def insort(a, x):
    lo = 0
    hi = len(a)

    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x:
            lo = mid+1
        else:
            hi = mid
            
    a.insert(lo, x)
    return a

