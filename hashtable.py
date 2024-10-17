'''A class implementing a Hashtable as a list of lists
   Uses Chaining for collision resolution'''

class Hashtable:

    
    ''' returns a new empty hashtable of size s'''
    def _inittable(self, s):
        newtable = []
        for i in range(s):
            newtable.append([]) #an empty list
        return newtable

    '''returns the hash value of the given key'''
    def _hash(self, key):
        return key%self.size()

    def __init__(self, size=5, maxload= .5, maxchainlen = 3):

        self.min_size = size
        self.numKeys = 0
        self.maxload = maxload
        self.maxChain = maxchainlen
        self.table = self._inittable(size)

    def contains(self,key):
        slotNum = self._hash(key)
        if key in self.table[slotNum]:
            return True
        return False
    def resize(self, newSize):
        prevTable = self.table
        self.table = self._inittable(newSize)
        for iList in prevTable:
            for item in iList:
                slotNum = self._hash(item)
                self.table[slotNum].append(item)

    def insert(self, key):
        if self.contains(key):
            return False
        else:
            slotNum = self._hash(key)
            self.table[slotNum].append(key)
            self.numKeys += 1

            if (len(self.table[slotNum])> self.maxChain) or ((self.numKeys/self.size()) >= self.maxload):
                self.resize(self.size() * 2)
        return True
                
    def remove(self, key):
        if not self.contains(key):
            return False
        else:
            slotNum = self._hash(key)
            self.table[slotNum].remove(key)
            self.numKeys -= 1

            if ((self.size()/ 2) >= self.min_size ):
                self.resize(self.size() // 2)

                if ((self.numKeys / self.size()) > self.maxload):
                    self.resize(self.size() * 2)
            
        return True









    def getNumKeys(self):
        total = 0
        for iList in self.table:
            total = total + len(iList)
        return total

    def size(self):
        return len(self.table)

    def isEmpty(self):
        if self.getNumKeys() == 0:
            return True

        else:
            return False

    def displayStats(self):
        print('Current Size is: ' , self.size())
        print('Number of keys: ' , self.getNumKeys())
        print('Current Load factor: ' , self.getNumKeys()/ self.size())
        max_chain = 0
        for i in range(self.size()):
            if(len(self.table[i]) > max_chain):
                max_chain = len(self.table[i])
            else:
                continue
        print('Max chain lenght is: ' , max_chain)

        zero_chains = 0
        for i in range(self.size()):
            if(len(self.table[i]) == 0):
                zero_chains += 1
            else:
                continue
        print('Num of chains with lenght 0: ' , zero_chains)

      
        total_length = 0
        total_chains = 0
        for i in range(self.size()):
            if(len(self.table[i]) != 0):
                total_chains += 1
                total_length += len(self.table[i])
            else:
                continue
        print('Average length of chains: ' , (total_length/ total_chains))


        
        
            
        
    

def test_insert():
    a = Hashtable()
    print(a.table)
    a.insert(2)
    a.insert(5)
    print(a.table)
    a.insert(2)
    a.insert(12)
    a.insert(9)
    print(a.table)
    a.remove(12)
    print(a.table)
    a.remove(2)
    print(a.table)


test_insert()

    
    
    

