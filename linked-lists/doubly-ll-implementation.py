# DOUBLY LINKED LIST

# 1 <-> 5 <-> 10 <-> 77 -> null/none


class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None 
        
    def __str__(self):
        if self.prev == None:
            return ('{ value: ' + str(self.data) + ' next: {' + str(self.next)+'}')
        else:
            return ('{ value: ' + str(self.data) + ' prev: {' + str(self.prev.data) + '} next: {' + str(self.next)+'}')

class DoublyLinkedList:
    
    def __init__(self, value = None):
        if value == None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_head = Node(value)
            self.head = new_head
            self.tail = self.head
            self.length = 1

    def __str__(self):
        return ('length: ' + str(self.length) + ', head: ' + str(self.head) + '}')

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            new_node = self.head 
            self.tail = self.head 
            self.length += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node
            self.length += 1
    
    
    def prepend(self, value):
        new_head = Node(value)
        new_head.next = self.head 
        self.head.prev = new_head
        self.head = new_head
        self.length += 1
        
    
    def insert(self, index, value):
        middle = Node(value)
        i = 0
        if index >= self.length:
            self.append(value)
        if index == 0:
            self.prepend(value)
        front = self.traverse_to_index(index-1)
        back = front.next
        front.next = middle
        middle.prev = front
        middle.next = back
        back.prev = middle
        self.length += 1
    
    
    def traverse_to_index(self, index):
        current = self.head
        i = 0
        while i != index:
            current = current.next
            i += 1
        return current
    
    
    def printl(self):
        nodes = []
        current = self.head
        while current != None:
            nodes.append(current.data)
            current = current.next
        print(nodes)
        return(nodes)


    def lookup(self, value):
        current = self.head
        i = 0
        while i < self.length:
            if current.data == value:
                print(current)
                return current
            else:
                current = current.next
                i += 1
        print('value not present in linked list')
        return -1
            
            
    def delete_value(self, value):
        node_to_delete = self.lookup(value)
        front = node_to_delete.prev 
        back = node_to_delete.next 
        front.next = back 
        back.prev = front
        self.length -= 1
        return self.printl()
        
        
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return 
        if index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        front = self.traverse_to_index(index-1)
        node_to_remove = front.next
        back = node_to_remove.next
        front.next = back
        back.prev = front
        self.length -= 1
        return    
        

d = DoublyLinkedList(10)
d.append(15)
#d.printl()
d.prepend(888)
d.insert(1, 17)
#d.printl()
d.lookup(10)
d.delete_value(10)
d.remove(1)
d.printl()