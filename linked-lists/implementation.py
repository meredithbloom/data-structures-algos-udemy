# 10 --> 5 --> 16

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
        return ('head: ' + str(self.head) + '}')


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



my_linkedlist = LinkedList(10)
print(my_linkedlist)
my_linkedlist.append(5)
my_linkedlist.append(16)
print(my_linkedlist)
my_linkedlist.prepend(1)
print(my_linkedlist)
