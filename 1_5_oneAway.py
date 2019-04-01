def oneaway(first, second):
    if (len(first) == len(second)):
        return oneReplace(first, second)
    elif (len(first) + 1 == len(second)):
        return oneInsert(first, second)
    elif (len(first) - 1 == len(second)):
        return oneInsert(second, first)
    return False

def oneReplace(s1, s2):
    diff = False
    for x in range(0, len(s1)):
        if s1[x] != s2[x]:
            if diff:
                return False
            diff = True
    return True
    

def oneInsert(s1, s2):
    index1 = 0
    index2 = 0
    while(index2 < len(s2) and index1 < len(s1)):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True
