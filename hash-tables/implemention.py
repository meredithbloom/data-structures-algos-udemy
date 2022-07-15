# implementing a hash table class from scratch

""" 
(https://github.com/theja-m/Data-Structures-and-Algorithms/blob/master/Data%20Structures%20-%20Hashtables/Hash%20Table%20Implementation.py)
		Create an array(self.mydict) with a bucket size - which is derived from the load factor.
		The Load factor is a measure that decides when to increase the HashMap capacity to maintain the get() and put() operation complexity of O(1).
		The default load factor of HashMap is 0.75f (75% of the map size).
		Load Factor = (n/k)
		where n is the number of max number of elements that can be stored dict
		k is the bucket size
		Optimal Load factor is around (2/3) such that the effect of hash collisions is minimum 
"""


class Hashtable:
    def __init__(self):
        self.bucket = 50
        # creating an empty list of length 50
        self.map = [[] for i in range(self.bucket)]
    
    
    def __str__(self):
        # __dict__ means contents of dictionary
        return str(self.__dict__)
    
    
    def hash(self,key):
        hash_address = len(key) % self.bucket
        #print(hash_address)
        return hash_address
    
    
    def put(self, key, value):
        # value may already be present
        hash_value = self.hash(key)
        reference = self.map[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference[i][1] = value
                return None
        reference.append([key, value])
        return None
    
    
    def get(self, key):
        # returns value mapped to key, or -1 if there is no value mapped to said key
        hash_value = self.hash(key)
        reference = self.map[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                return reference[i][1]
        return -1
    
    
    def remove(self, key):
        # removes mapping of the specified value key if the map contains mapping
        hash_value = self.hash(key)
        reference = self.map[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference.pop()
                return None
        return None
    
    
    def keys(self):
        key_list = []
        for i in range(self.bucket):
            if self.map[i] != []:
                if len(self.map[i]) > 1:
                    for j in range(len(self.map[i])):
                        #print(self.map[i][j][0])
                        key_list.append(self.map[i][j][0])
                else:
                    #print(self.map[i][0][0])
                    key_list.append(self.map[i][0][0])
        print(key_list)
            
    
my_hash_table = Hashtable()
my_hash_table.put('grapes', 1000)
#print(my_hash_table.get('grapes'))
my_hash_table.put('oranges', 50)
my_hash_table.put('apples', 12)
my_hash_table.put('milk', 1)
my_hash_table.put('brie', 2)
#print(my_hash_table)
#my_hash_table.remove('oranges')
#print(my_hash_table)
#print(my_hash_table.get('brie'))
my_hash_table.keys()