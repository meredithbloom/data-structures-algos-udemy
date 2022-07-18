# STACK DATA STRUCTURE

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
        
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    
    # lets us see the top node
    def peek(self):
        return 'top of stack is ' + str(self.top.value)
    
    # adds us add to the top of the stack
    def push(self, value):
        new_top = Node(value)
        if self.length == 0:
            self.bottom = new_top
            self.top = self.bottom
        else:
            new_top.next = self.top
            self.top = new_top
        self.length += 1
            
    
    # remove top item in the stack
    def pop(self):
        if self.length > 1:
            self.top = self.top.next 
            self.length -= 1
        elif self.length == 1:
            self.top = None
            self.bottom = None
            self.length = 0
    
    
    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False
    
    
    def print_stack(self):
        values = []
        current_node = self.top
        while current_node != None:
            print(current_node.value, end = ' -> ')
            current_node = current_node.next
        print()
    
    
myStack = Stack()

myStack.push('google')
myStack.push('microsoft')
myStack.print_stack()
myStack.push('facebook')
myStack.print_stack()
myStack.pop()
myStack.print_stack()
top = myStack.peek()
print(top)
myStack.push('apple')
myStack.print_stack()
print(myStack)