# Edge List
# defining a graph by "edges" - array of connections
edge = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacent List
# defining a graph by node neighbors
# index of the array is the value of the actual graph node
adjacents = [[2], [2, 3], [0, 1, 3], [1, 2]]


# Adjacent Matrix
# 0 or 1 represents connection to corresponding node (index number)
# node
graph = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]
