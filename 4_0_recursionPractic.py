def sumlist(mylist):
    
    if len(mylist) == 1:
        return mylist[0]
    else:
        return mylist[0] + sumlist(mylist[1:])

def listsum(mylist):
    total = 0
    for element in mylist:
        if type(element) == type(1):
            total = total + element
        else:
            total = total + listsum(element)
    return total

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def sumSeries(n):
    if n < 1:
        return 0
    else:
        return n + sumSeries(n - 2)

def sumDigit(n):
    if len(str(n)) == 1:
        return int(str(n)[0])
    else:
        return int(str(n)[0]) + sumDigit(int(str(n)[1:]))

def harmonic(n):
    if n == 0:
        return 0
    else:
        return n + harmonic(n - 1)

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

def gcd(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        

