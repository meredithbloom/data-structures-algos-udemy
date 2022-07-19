# TREES

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Perfect Binary Tree - each node has only either 2 OR zero children. 

# 1. Number of total nodes on each level is double the number of nodes on the previous level
# 2. Number of nodes on the lowest level is equal to all the nodes on higher levels plus one

# Number of nodes on a level = 2^(level number)

# Level 0: 2^0 = 1 node
# Level 1: 2^1 = 2 nodes
# Level 2: 2^2 = 4 nodes
# Level 3: 2^3 = 8 nodes ... 


# Total number of nodes in a tree = 2^(height) - 1
# log of nodes = steps

# log 100 = 2
# 10^2 = 100

# unbalanced trees can have, at worst, O(n) for lookup, insert, delete