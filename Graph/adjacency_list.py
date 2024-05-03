class GraphList:
    def __init__(self):
        self.graph = {}
    def add_node(self,v1):
        if v1 in self.graph:
            print(v1, 'is already present in graph')
        else:
            self.graph[v1] = []


    def add_edges(self,v1, v2):
        if v1 not in self.graph:
            print(v1, 'not present in graph')
        elif v2 not in self.graph:
            print(v2, 'not present in graph')
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)


    def add_edges_with_weight(self,v1, v2, cost):
        if v1 not in self.graph:
            print(v1, 'not present in graph')
        elif v2 not in self.graph:
            print(v2, 'not present in graph')
        else:
            list1 = [v2, cost]
            list2 = [v1, cost]
            self.graph[v1].append(list1)
            self.graph[v2].append(list2)

    def delete_node(self,v1):
        if v1 not in self.graph:
            print(v1,'not present in graph')
        else:
            self.graph.pop(v1)
            for i in self.graph:
                list1 = self.graph[i]
                if v1 in list1:
                    list1.remove(v1)

    def delete_edges(self,v1,v2):
        if v1 not in self.graph:
            print(v1,'not present in graph')
        elif v2 not in self.graph:
            print(v2,'not present in graph')
        else:
            # for i in self.graph:
            if v2 in self.graph[v1]:
                self.graph[v1].remove(v2)
                self.graph[v2].remove(v1)


    def print_graph(self):
        for i, j in self.graph.items():
            print(i, j)

    def DFS(self,node,visited = set()):
        if node not in self.graph:
            print(node,'vertex not present in graph')
            return
        if node not in visited:
            visited.add(node)
            print(node)
            for i in self.graph[node]:
                self.DFS(i,visited)





G = GraphList()
G.add_node('A')
G.add_node("B")
G.add_node("C")

G.add_edges("A", "B")
G.add_edges("A", "C")

print(G.graph)
print('after deleting vertex')
# G.delete_node('A')
G.delete_edges('A','B')
print(G.graph)
print('DFS:_')
G.DFS('B')