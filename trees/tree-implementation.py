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
        pass


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
print(tree.lookup(15))
tree.print_tree()
print(tree.lookup(55))
print(tree.lookup(20))


#       9
#   4       20
# 1   6   15  170


# def traverse(node):
#     tree = { value = node.value}
#     tree.left = node.left == None ? None: traverse(node.left)
#     tree-ri