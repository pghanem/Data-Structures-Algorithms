import time

#naive brute force solution O(n^2)
def isUniqueBF(word):
    for i in range(0, len(word)):
        for x in range(0, len(word)):
            if word[i] == word[x] and x != i:
                return False
    return True


#improved brute force solution that avoids multiple checks on same pairs O(n^2)
def isUniqueBFBetter(word):
    for i in range(0, len(word)):
        for x in range(i + 1, len(word)):
            if word[i] == word[x]:
                return False
    return True


#improved solution using hashtables O(n)
def isUniqueHash(word):
    hashmap = {}
    for char in word:
        hashmap[char] = None
    return len(hashmap.items()) == len(word)


#improved solution using boolean array O(n)
def isUniqueBool(word):
    if len(word) > 128: return false
    
    arr = [None] * 128
    for char in word:
        if arr[ord(char)] is None:
            arr[ord(char)] = True
        else:
            return False
    return True
