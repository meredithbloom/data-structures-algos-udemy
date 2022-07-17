# my_linked_list = {
#     'head': {
#         'value': 10,
#         'next': {
#             'value': 5,
#             'next': {
#                 'value': 16,
#                 'next': None
#             }
#         }
#     }
# }


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def __str__(self):
        return ('{ value: '+ str(self.data) + 
            ' next: {' + str(self.next)+'}')
            


class LinkedList:
    def __init__(self, value = None):
        if value != None:
            new_head = Node(value)
            self.head = new_head
            self.tail = self.head
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0


    def __str__(self):
        return ('length: ' + str(self.length) + ', head: ' + str(self.head) + '}')


    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1


    def prepend(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        self.length += 1


    def lookup(self, value):
        current_node = self.head
        index = 0
        while index < self.length:
            if current_node.data == value:
                print(current_node)
                return current_node
            else:
                current_node = current_node.next
                index += 1
        print ("value does not exist in linked list")
        return -1
    
    
    def insert(self, index, value):
        new_node = Node(value)
        current_index = 0
        current_node = self.head
        if index >= self.length:
            self.append(value)
            return
        if index == 0:
            self.prepend(value)
        while current_index < self.length:
            if current_index == index-1:
                current_node.next, new_node.next = new_node, current_node.next
                self.length += 1
                break
            current_node = current_node.next
            current_index += 1
        
    
    def print_list(self):
        values = []
        current_node = self.head
        while current_node != None:
            values.append(current_node.data)
            current_node = current_node.next
        print(values)
    
    
    def remove(self, value):
        current = self.head 
        index = 0
        next_node = current.next
        while index < self.length:
            if next_node.data == value:
                next_node = next_node.next 
                current.next = next_node
                self.length -= 1
                return
            else:
                current = current.next
                next_node = current.next 
                index += 1
        print("value not present in linked list")
        return -1



my_linkedlist = LinkedList(10)
#print(my_linkedlist)
my_linkedlist.append(5)
my_linkedlist.append(16)
#print(my_linkedlist)
my_linkedlist.insert(2, 55)
#print(my_linkedlist)
my_linkedlist.lookup(55)
my_linkedlist.lookup(72)
my_linkedlist.print_list()
my_linkedlist.remove(55)
my_linkedlist.print_list()