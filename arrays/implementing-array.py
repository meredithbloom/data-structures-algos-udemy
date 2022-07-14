# if we were to create an array data structure (class) ourselves

class Array:
    def __init__(self):
        self.length = 0
        self.data = {}
        
    def __str__(self):
        return str(self.__dict__)
    
    def get(self, index):
        return self.data[index]

    def push(self,item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item
    
    def delete(self, index):
        deleted_item = self.data[index]
        self.shift_items(index)
        return deleted_item
    
    def shift_items(self, index):
        for i in range(index, self.length-1, 1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1



my_array = Array()
print(my_array)
#print(my_array.get(0))
my_array.push(5)
print(my_array)
my_array.push(10)
#print(my_array)
my_array.push('hello')
my_array.push("!")
print(my_array)
my_array.delete(1)
print(my_array)
