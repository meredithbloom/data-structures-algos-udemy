#BREADTH FIRST SEARCH/TRAVERSAL

#moving left to right through all nodes in a tree, going level by level until we either find our target node, or the tree ends

#takes more memory because we need to keep track of all nodes and their children
'''
		9
  4	  20
1  6  15  170
'''
#[9, 4, 20, 1, 6, 15, 170]

print('please work')

class Node:
	def __init__(self, val):
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

	def lookup(self, val):
		temp = self.root
		while True:
			if temp.val == val:
				return True
			elif temp == None:
				return False
			elif val < temp.val:
				temp = temp.left
			elif val > temp.val:
				temp = temp.right

	def BFS(self):
		current = self.root
		mylist = []
		queue = []
		queue.append(current)

		while len(queue) > 0:
			current = queue[0]
			del queue[0]
			mylist.append(current.val)
			if current.left:
				queue.append(current.left)
			if current.right:
				queue.append(current.right)

		return mylist


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

x = tree.lookup(170)
print(x)
print(tree.BFS())