# hashtable solution that inserts all chars from both into a hashtable and uses len to
# check if any non-matching characters were added O(n) but takes memory
def checkPermHash(word1, word2):
    if len(word1) != len(word2): return False

    hashmap = {}
    
    for i in range(0, len(word1)):
        hashmap[word1[i]] = ''
        hashmap[word2[i]] = ''
        
    return len(hashmap) == len(word1)
        
# sort solution that takes less memory but is slower O(nlogn)
def checkPermSort(word1, word2):
    return sorted(word1) == sorted(word2)


#array solution with fixed array size 128, takes O(n) and less memory
def checkPermArray(word1, word2):
    if len(word1) != len(word2): return False

    arr = [0] * 128
    
    for char in word1:
        arr[ord(char)] += 1
    
    for char in word2:
        arr[ord(char)] -= 1
        if arr[ord(char)] < 0:
            return False

    return True
