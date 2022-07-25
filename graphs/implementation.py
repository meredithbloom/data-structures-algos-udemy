# Implementing a graph - built on top of other data structures


class Graph:
    def __init__(self):
        self.node_count = 0
        self.adjacent_list = {}
    
    
    def __str__(self):
        return str(self.__dict__)
    
    
    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.node_count += 1


    def add_edge(self, node1, node2):
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)       
    # undirected graph - bidirectional
    
    
    def show_connections(self):
        for node, neighbors in self.adjacent_list.items():
            print(node, end = ' --> ')
            print(' '.join(neighbors))
         
            

myGraph = Graph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')
myGraph.add_edge('3', '1')
myGraph.add_edge('3', '4')
myGraph.add_edge('4', '2')
myGraph.add_edge('4', '5')
myGraph.add_edge('1', '2')
myGraph.add_edge('1', '0')
myGraph.add_edge('0', '2')
myGraph.add_edge('6', '5')
print(myGraph)
myGraph.show_connections()
