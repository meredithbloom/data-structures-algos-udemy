# DEPTH FIRST SEARCH/TRAVERSAL

# follows one branch of tree as far down as possible, or until target is reached. once we reach the bottom of the tree, we go back to the nearest ancestor with unexplored children and check that branch. continue until we either find target or run out of unexplored nodes

# more memory efficient than BFS because we don't need to keep track of all child nodes

#		9
# 	4		20
#  1  6  15    170

# InOrder - [1, 4, 6, 9, 15, 20, 170]
# PreOrder - [9, 4, 1, 6, 20, 15, 170] - PreOrder makes it much easier to recreate a tree. we know that 4 is the parent node to 1 and 6 because then next item is 20 (meaning it would be on the right side of the tree - > root)
# PostOrder - [1, 6, 4, 15, 170, 20, 9] - children come before parent

# list is different order than BFS
# [9, 4, 1, 6, 20, 15, 170]

# usually implemented with recursion

#    101
# 33     105

# InOrder - 33, 101, 105 
# PreOrder - 101, 33,105
# PostOrder - 33, 105, 101

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __repr__(self):
		return str(self.val)

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
			#print(f'current queue is ' + str(list(queue)))
			current = queue[0]
			#print(current.val)
			del queue[0]
			mylist.append(current.val)
			#print(f'current list is ' + str(mylist))
			if current.left:
				#print(current.left.val)
				queue.append(current.left)
			if current.right:
				#print(current.right.val)
				queue.append(current.right)

		return mylist

	def recursive_BFS(self, queue, mylist):
		if len(queue) == 0:
			return mylist
		current = queue[0]
		del queue[0]
		mylist.append(current.val)
		if current.left:
			#print(current.left.val)
			queue.append(current.left)
		if current.right:
			#print(current.right.val)
			queue.append(current.right)
		return self.recursive_BFS(queue, mylist)

	# DFS implementation
	# in order from right to left regardless of level	
	def inorder(self, node, mylist):
		if node.left != None:
			self.inorder(node.left, mylist)
		mylist.append(node.val)
		if node.right != None:
			self.inorder(node.right, mylist)
		return mylist

	# much easier to recreate tree, as we know right side has started once element in list is greater than root (first element)
	def preorder(self, node, mylist):
		if node != None:
			mylist.append(node.val)
			self.preorder(node.left, mylist)
			# once we can go no deeper on the left side, we check right side
			self.preorder(node.right, mylist)
		return mylist

	# children come before parents. root node will be last in list
	def postorder(self, node, mylist):
		if node.left:
			self.postorder(node.left, mylist)
		if node.right:
			self.postorder(node.right, mylist)
		mylist.append(node.val)
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
#print(tree.BFS())
#print(tree.recursive_BFS([tree.root], []))
print(tree.inorder(tree.root, []))
print(tree.preorder(tree.root, []))
print(tree.postorder(tree.root, []))


# InOrder - [1, 4, 6, 9, 15, 20, 170]

# PreOrder - [9, 4, 1, 6, 20, 15, 170] - PreOrder makes it much easier to recreate a tree. we know that 4 is the parent node to 1 and 6 because then next item is 20 (meaning it would be on the right side of the tree - > root)
# PostOrder - [1, 6, 4, 15, 170, 20, 9] - children come before parent