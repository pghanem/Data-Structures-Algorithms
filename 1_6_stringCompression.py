#naive solution that creates a new string and does a lot of concatenation (slow)
def compress(s):
    count = 1
    ns = ''
    for x in range(0, len(s)-1):
        if s[x] != s[x+1]:
            ns += s[x] + str(count)
            count = 1
        else:
            count+=1
    ns += s[len(s)-1] + str(count)
        
    if len(s) >= len(ns):
        print(ns)
    else:
        print(s)
        
#better solution that saves runtime spent concatenating strings
def compressBetter(s):
    count = 1
    nl = []
    for x in range(0, len(s)-1):
        if s[x] != s[x+1]:
            nl.append(s[x] + str(count))
            count = 1
        else:
            count+=1
    nl.append(s[len(s)-1] + str(count))
    
    ns = ''.join(nl)
    if len(s) >= len(ns):
        print(ns)
    else:
        print(s)
        
#best solution that saves time concatenating strings and prints
#the original string sooner
def compressBest(s):
    count = 1
    nl = []
    for x in range(0, len(s)-1):
        if s[x] != s[x+1]:
            nl.append(s[x] + str(count))
            count = 1
        else:
            count+=1
    nl.append(s[len(s)-1] + str(count))
    
    ns = ''.join(nl)
    if len(s) >= len(ns):
        print(ns)
    else:
        print(s)
