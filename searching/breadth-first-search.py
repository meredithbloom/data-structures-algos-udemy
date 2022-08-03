#BREADTH FIRST SEARCH/TRAVERSAL

#moving left to right through all nodes in a tree, going level by level until we either find our target node, or the tree ends

#takes more memory because we need to keep track of all nodes and their children
'''
		9
  4	  20
1  6  15  170
'''
#[9, 4, 20, 1, 6, 15, 170]

class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

class BinarySearchTree:
	def __init__(self):
	  self.root = None

  def insert(self, val):
    new = Node(val)
    if self.root == None:
      self.root = new
      return
    temp = self.root
    while True:
      if new.val < temp.val:
        if temp.left == None:
          temp.left = new
          break
        else:
          temp = temp.left
      elif new.val > temp.val:
        if temp.right == None:
          temp.right = new
          break
        else:
          temp = temp.right
	
	def BFS(self):
		return self.root



tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.BFS())



	