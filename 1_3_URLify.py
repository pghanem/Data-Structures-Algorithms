# basic solution, if character is not a space carry it over to a new array
# but if it is, instead add '%20'. returns a copy. O(n)
def urlify(sentence, truelen):
    new = ''
    for x in range(0, truelen):
        if ord(sentence[x]) != 32:
            new += sentence[x]
        else:
            new += '%20'
    print(new)

# in-place solution

def urlifyinplace(sentence, truelen):
    lst = [None] * (truelen + 1)
    for x in range(0, truelen):
        lst[x] = sentence[x]
    print(lst)

    spacecount = 0
    for i in range(0, truelen):
        if lst[i] == ' ':
            spacecount+=1
            
    #start at the back of the list with enough space for everything
    end = truelen + spacecount * 2
    lst[truelen] = '/0'
    #start rewriting the list
    for x in range(truelen - 1, 0, -1):
        print(x)
            
