#simple solution using constant amount of memory, probably optimal at O(n)
# can possibly be improved with resizable array for less memory
def paliperm(sentence):
    lst = [0] * 128
    for char in sentence:
        lst[ord(char)] += 1

    print(lst)
    oddcounter = 0
    for x in range(0, len(lst)):
        if lst[x] % 2 != 0 and x != ord(' '):
            oddcounter +=1
            
    return oddcounter < 2
