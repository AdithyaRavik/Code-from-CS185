'''This is a test script for the class HashTable.py'''
from hashtable import Hashtable

'''1. Simple Tests:'''
table = Hashtable()
print( "table size: " , table.size()) #expected: table size 5
table.insert(0)
table.insert(1)
table.insert(2)
print(table.table)
print ("table size: ", table.size()) #expected: table size 10
table.insert(10)
table.insert(20)
print(table.table)
print ("table size: ", table.size()) #expected: table size 20
table.remove(1)
print ("table size: ", table.size()) #expected: table size 10
print ("number of items: ", table.getNumKeys()) #expected: number of items 4
table.remove(0)
print ("table size: ", table.size()) #expected: table size 10
print( "contains 0? ", table.contains(0)) #expected : contains 0? false
print( "contains 6? ", table.contains(6)) #expected : contains 6? false
print( "contains 30? ", table.contains(30)) #expected : contains 30? false
print( "contains 20? ", table.contains(20)) #expected : contains 20? true
table.displayStats()
#expected table size: 10, number of items in the table: 3, current load: .3
#length of longest chain: 2, number of slots with empty lists: 8
# average length of chains which are greater than 0: 1.5


'''2. Creating a bad dataset'''
growHT=Hashtable(10, .5, 3)
'''TODO: Create a dataset of 7 numbers such that inserting them into hash table growHT
causes it to increases in size 5 times.
Define your dataset, insert it into growHT and show the output of displayStats'''

dataset = [5,10,15,25,35,40,45]
for i in dataset: 
    growHT.insert(i)
print(growHT.table)
print( growHT.displayStats())
#Output: Current size = 20, Number of Keys = 7 Load Factor = 0.35, Max chain length= 3, 
# Num of chains with length 0 = 16, Average length of chains = 1.75



'''3. Creating a good dataset'''
nogrowHT = Hashtable(5, .5, 3)
'''TODO: Create the largest dataset you can such
that all the all numbers of the dataset can be inserted into hash table nogrowHT
without causing it to increase in size.
Define your dataset, insert it into nogrowHT and show the output of displayStats'''
dataset2 = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,55]

for i in dataset2:
    nogrowHT.insert(i)
print(nogrowHT.table)
print(nogrowHT.displayStats())

#Output: Current size = 5, Number of Keys = 2 Load Factor = 0.4, Max chain length= 2, 
# Num of chains with length 0 = 4, Average length of chains = 2





