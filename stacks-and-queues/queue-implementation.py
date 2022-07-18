# QUEUE - implemented with linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    # return value of first item in line    
    def peek(self):
        return str(self.first.value) + ' is first in line'
    
    # only add to back of the line
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = self.first 
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
            
    
    # only remove from front of the line
    def dequeue(self):
        new_first = self.first.next
        dequeued_node = self.first 
        if new_first == None:
            self.first = None
            self.length -= 1
            return
        self.first.next = None
        self.first = new_first
        self.length -= 1
    
    
    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False


    def print_queue(self):
        temp = self.first
        while temp != None:
            print(temp.value, end=' -> ')
            temp = temp.next 
        print()    
        print(self.length)


myQueue = Queue()
myQueue.enqueue('meredith')
myQueue.enqueue('benjamin')
myQueue.enqueue('helen')
print(myQueue.peek()) 
myQueue.print_queue()   