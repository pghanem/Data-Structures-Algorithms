class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self.getHash(key)  #generate index value that were placing it in
        key_value = [key, value]      #what we want to insert into the cell


        #if that index is empty, place the key-value pair into it
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
        #if the index is not empty, check if the key is already in it
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    #if the key is already there, simply update the value
                    pair[1] = value
                    return True
            #otherwise its a new key, to the linked list in the cell
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        #generate index value that we are looking up
        key_hash = self.getHash(key)
        #if there is a pair(s) at that index, check all and return value of the matching key
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        #else does not exist, return none
        return None

    def delete(self, key):
        key_hash = self.getHash(key)
        if self.map[key_hash] is None:
            return False
        # use for loop because you need the index for deletions
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))

                
                    
