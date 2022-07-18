
# implementing a stack with an array based structure


class Stack:
    def __init__(self):
        self.length = 0
        self.data = []
    
    
    def __str__(self):
        return str(self.__dict__)
    
    
    def push(self, value):
        self.data.append(value)
        self.length += 1
    
    
    def pop(self):
        if self.length > 0:
            popped_item = self.data[self.length-1]
            del self.data[self.length-1]
            self.length -= 1
            return popped_item
            
        else:
            return "stack is empty"
            
    
    def peek(self):
        if self.length > 0:
            return self.data[self.length-1]
        else:
            return "stack is empty"
        
    
    def print_stack(self):
        index = 0
        for i in range(self.length):
            print(self.data[i] + ' -> ') 
        print()


myStack = Stack()
myStack.push('microsoft')
myStack.push('facebook')
myStack.push('google')
myStack.print_stack()
print(myStack)
# myStack.pop()
# print(myStack)
print(myStack.peek())