# DEPTH FIRST SEARCH/TRAVERSAL

# follows one branch of tree as far down as possible, or until target is reached. once we reach the bottom of the tree, we go back to the nearest ancestor with unexplored children and check that branch. continue until we either find target or run out of unexplored nodes

# more memory efficient than BFS because we don't need to keep track of all child nodes

#			9
# 	4		20
# 1  6  15  170

# list is different order than BFS
# [9, 4, 1, 6, 20, 15, 170]

# usually implemented with recursion