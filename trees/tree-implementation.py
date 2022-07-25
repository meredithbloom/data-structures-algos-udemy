# BINARY SEARCH TREE


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):            
        return('value: ' + str(self.value) + ', left child: {' + str(self.left) + '}, right child: {' + str(self.right) + '}')


class BinarySearchTree:
    def __init__(self):
        self.root = None
    

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root == None:
            self.root = new_node
            return
        temp = self.root
        while True:
            if value < temp.value:
                # go left
                if temp.left == None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left   
            if new_node.value > temp.value:
                # go right
                if temp.right == None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right    
        
    
    def lookup(self, value):
        node = self.root 
        while node != None:
            if value == node.value:
                return node
            elif value < node.value:
                node = node.left 
            elif value > node.value:
                node = node.right
        return 'node does not exist'
    
    
    def remove(self, value):
        if self.root == None:
            return False 
        temp = self.root
        parent = None
        while temp:
            if value < temp.value:
                # go left
                parent = temp
                temp = temp.left 
                child = parent.left
            elif value > temp.value:
                # go right
                parent = temp
                temp = temp.right
                child = parent.right
            # once we find a match
            elif value == temp.value:
                # if node to be removed DOES NOT have children
                if temp.left == None and temp.right == None:
                    if child == parent.right:
                        parent.right = None
                        return  
                    elif child == parent.left:
                        parent.left = None
                        return 
                # if node to be removed only has a left child
                elif temp.left != None and temp.right == None:
                    if child == parent.right:
                        parent.right = temp.left 
                        return 
                    elif child == parent.left:
                        parent.left = temp.left 
                        return
                # if node to be removed only has a right child
                elif temp.left == None and temp.right != None:
                    if child == parent.right:
                        parent.right = temp.right
                        return
                    elif child == parent.left:
                        parent.right = temp.left
                        return 
                # if node to be removed has children on both sides
                elif temp.left != None and temp.right != None:
                    if child == parent.right:
                        # connect parent to left child of removed node
                        parent.right = temp.left 
                        # connect right node as new child of former left sibling
                        new_child = temp.right 
                        # replace removed node with former child
                        temp = temp.left 
                        # reconnect right node to new parent
                        temp.right = new_child
                        return
                    elif child == parent.left:
                        # connect parent to right child of removed node
                        parent.left = temp.right 
                        #connect left node as new child of former right sibling
                        new_child = temp.left 
                        #replace removed node with former child
                        temp = temp.right 
                        # reconnect left node to new parent
                        temp.left = new_child
                        return
                        



    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
    
    # sorted order of elements in tree
    def printt(self, node):
        if node != None:
            self.printt(node.left)
            print(str(node.value))
            self.printt(node.right)


tree = BinarySearchTree()
tree.insert(15)
tree.insert(10)
tree.insert(20)
tree.insert(9)
tree.insert(7)
#print(tree.lookup(15))
tree.print_tree()
print()
#print(tree.lookup(55))
#print(tree.lookup(20))
tree.remove(10)
tree.print_tree()
print(tree.lookup(10))
tree.insert(96)
tree.insert(75)
print()
tree.print_tree()
print(tree.lookup(15))


#       9
#   4       20
# 1   6   15  170


# def traverse(node):
#     tree = { value = node.value}
#     tree.left = node.left == None ? None: traverse(node.left)
#     tree-ri