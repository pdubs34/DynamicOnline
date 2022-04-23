def maxClique(G):
    len = len(vertices)
    max = 0
    for i in range(i + 2, len + 1):
        boolean = oracle(G,i)
        if(boolean == true):
            max = i
    return max

max =  maxClique(G,k)
numVertices = len(V)
vertices = []
for i in range(numVertices):
    temp = graph
    temp = temp.remove(vertex[i])
    boolean = oracle(G,max)
    if(boolean == false):
        vertices.append(vertices[i])
return vertices

