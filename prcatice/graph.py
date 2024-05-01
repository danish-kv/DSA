class MatrixGraph:
    def __init__(self):
        self.vertices = []
        self.graph = []
        self.count = 0

    def print_graph(self):
        for i in range(self.count):
            for j in range(self.count):
                print(format(self.graph[i][j],'3' ),end=' ')
            print()
    def insert(self,v):
        if v in self.vertices:
            print('dup not allowed')
        else:
            self.vertices.append(v)
            self.count += 1
            for n in self.graph:
                n.append(0)

            temp = []
            for i in range(self.count):
                temp.append(0)
            self.graph.append(temp)

    def add_edges(self,v1,v2):
        if v1 not in self.vertices:
            print('not found')
            return
        elif v2 not  in self.vertices:
            print('Not')
            return
        else:
            index1 = self.vertices.index(v1)
            index2 = self.vertices.index(v2)
            self.graph[index1][index2] = 1
            self.graph[index2][index2] = 1


    def DFS(self,node,visited = set()):
        if node not in self.vertices:
            print('sorry')
            return
        if node not in visited:
            visited.add(node)
            print(node)

            index = self.vertices.index(node)

            for i, connected in enumerate(self.graph[index]):
                if connected and self.vertices[i] not in visited:
                    self.DFS(self.vertices[i], visited)

            unvisited = set(self.vertices) - visited
            for vertix in unvisited:
                if vertix not in visited:
                    self.DFS(vertix,visited)

g = MatrixGraph()
g.insert(10)
g.insert(11)
g.insert(12)
g.add_edges(10, 11)
g.add_edges(12, 11)
print("Vertices:", g.vertices)
print("Adjacency Matrix:")
g.print_graph()
print("DFS Traversal:")
g.DFS(10)

