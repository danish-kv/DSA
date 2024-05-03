def add_vertex(v):
    global count
    if v in vertices:
        print('its already in vertices')
    else:
        vertices.append(v)
        count += 1
        for n in graph:
            n.append(0)
        temp = []
        for i in range(count):
            temp.append(0)
        graph.append(temp)

def print_graph():
    for i in range(count):
        for j in range(count):
            print(format(graph[i][j],'3'),end=" ")
        print()

def add_edges(v1, v2):
    if v1 not in vertices:
        print("can't find vertices of ",v1)
    elif v2 not in vertices:
        print("can't connect",v2,'not in vertices' )
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1

def delete_node(v):
    global count
    if v not in vertices:
        print(v,'not in vertices')
    else:
        index1 = vertices.index(v)
        count -= 1
        vertices.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def delete_edges(v1,v2):
    if v1 not in vertices:
        print(v1,'not present in vertices')
    elif v2 not in vertices:
        print(v2,'not present in vertices')
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0


vertices = []
graph = []
count = 0

add_vertex('A')
add_vertex('B')
add_vertex("C")

add_edges('A',"B")
add_edges('A',"C")

print_graph()
print(vertices)
print(graph)

delete_node('A')

print('After deleting')

print_graph()
print(vertices)
print(graph)