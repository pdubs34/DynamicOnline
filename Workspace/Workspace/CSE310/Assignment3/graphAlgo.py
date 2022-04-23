#Authors:Matt Hotovy and Payton Webb
from inspect import stack
from math import inf
from os import curdir
from typing import Dict
import networkx as nx
import sys
from networkx.algorithms.bipartite.basic import color
from networkx.algorithms.operators.product import tensor_product
from networkx.classes import graph
from operator import itemgetter
import heapq

from networkx.classes.function import neighbors, nodes
from networkx.classes.graph import Graph
from networkx.readwrite.json_graph import tree

g = nx.Graph()
inputfile = open(sys.argv[1], 'r')
numVertices = int(inputfile.readline())

def setToWhite(graph):
    for i in range(0, numVertices):
        graph.add_node(i, color = "white")

numEdges = 0
for line in inputfile:
   numEdges = numEdges + 1
   strippedLine = line.rstrip()
   edge = strippedLine.split(" ", 2)
   g.add_edge(int(edge[0]), int(edge[1]), weight = float(edge[2]))
inputfile.close()

def DFSAlgorithm(graph,resultStack,index):
   t = list(graph.nodes)
   count = 1
   stack = []
   stack.append(t[index])
   resultStack.append(t[index])
   graph.add_node(t[index],color = "grey", discoveryTime = count)
   while(len(stack) > 0):
      colorDict = dict(graph.nodes(data="color",default=1))
      count = count + 1
      x = stack[len(stack) - 1]
      neighborsNearMe = list(neighbors(graph,x))
      neighborsNearMe.sort()
      y = None
      for i in range(len(neighborsNearMe)):
         if(neighborsNearMe[i] != None):
            if(colorDict[neighborsNearMe[i]] == "white"):
               y = neighborsNearMe[i]
               resultStack.append(y)
               break
      if(y == None):
         stack.pop()
         graph.add_node(x,color = "black", finishTime = count)
      else:
         stack.append(y)
         graph.add_node(y, color = "grey", discoveryTime = count)
   while(len(resultStack) != numVertices):
        index = len(resultStack)
        resultStack = DFSAlgorithm(g,resultStack,index)
   setToWhite(graph)
   return resultStack

def isDisconnected(graph,resultStack,index):
   t = list(graph.nodes)
   count = 1
   stack = []
   disconnected = False
   stack.append(t[index])
   resultStack.append(t[index])
   graph.add_node(t[index],color = "grey", discoveryTime = count)
   while(len(stack) > 0):
      colorDict = dict(graph.nodes(data="color",default=1))
      count = count + 1
      x = stack[len(stack) - 1]
      neighborsNearMe = list(neighbors(graph,x))
      neighborsNearMe.sort()
      y = None
      for i in range(len(neighborsNearMe)):
         if(neighborsNearMe[i] != None):
            if(colorDict[neighborsNearMe[i]] == "white"):
               y = neighborsNearMe[i]
               resultStack.append(y)
               break
      if(y == None):
         stack.pop()
         graph.add_node(x,color = "black", finishTime = count)
      else:
         stack.append(y)
         graph.add_node(y, color = "grey", discoveryTime = count)
   if(len(resultStack) != numVertices):
        disconnected = True
   setToWhite(graph)
   return disconnected

def BFSTraversal(graph,resultQueue,index):
    t = list(graph.nodes)
    count = 1
    queue = []
    queue.append(t[index])
    resultQueue.append(t[index])
    graph.add_node(t[index],color = "grey", discoveryTime = count)
    while(len(queue) > 0):
      graphList = list(graph.nodes)
      colorDict = dict(graph.nodes(data="color",default=1))
      x = queue.pop(0)
      neighborsNearMe = list(neighbors(graph,x))
      listOfNeighborWeight = []
      weightTuple = []
      for i in range(len(neighborsNearMe)):
        listOfNeighborWeight.append(g[x][neighborsNearMe[i]]["weight"])
        # weightTuple = list(zip(neighborsNearMe[i],listOfNeighborWeight[i]))
      weightTuple = list(zip(neighborsNearMe,listOfNeighborWeight))
      weightTuple = sorted(weightTuple,key=itemgetter(1))
      y = None
      for i in range(len(weightTuple)):
         if(weightTuple[i][0] != None):
            if(colorDict[weightTuple[i][0]] == "white"):
               count = count + 1
               y = weightTuple[i][0]
               graph.add_node(y,color = "grey", discoveryTime = count)
               queue.append(y)
               resultQueue.append(y)
      graph.add_node(x,color = "grey", discoveryTime = count)
    while(len(resultQueue) != numVertices):
        index = len(resultQueue)
        resultQueue = DFSAlgorithm(g,resultQueue,index)
    setToWhite(graph)
    return resultQueue
    
def minSpanningTreeKru(graph):
    edges = graph.edges.data("weight", default=1)
    edges = sorted(edges,key=itemgetter(2))
    edgeSet = []
    k = 1
    while(len(edgeSet) < numVertices - 1):
        if(edgeSet.is_directed_acyclic_graph()):
            edgeSet.append(edges[k])
        k = k + 1
    return edgeSet

def minSpanningTreePrim(graph):
    nodes = list(graph.nodes)
    edges = graph.edges.data("weight", default=1)
    edges = sorted(edges,key=itemgetter(2))
    heap = []
    tree = []
    pointsTree = []
    edgeTree = []
    tempVar = []
    edgeDict = dict()
    heapq.heappush(heap,(nodes[0],"",0))
    edgeDict[nodes[0]] = "",0
    for i in range(1,len(nodes)):
        heapq.heappush(heap,(nodes[i],"",inf))
        edgeDict[nodes[i]] = "",inf
    while(len(heap) > 0):
        formattedHeap = []
        for line in heap:
            formattedHeap.append(list(line))
        formattedHeap = sorted(formattedHeap,key=itemgetter(2))
        for a in range(len(heap)):
            tempList = list(heap[a])
            if(tempList[0] == formattedHeap[0][0]):
                storedVar = a
        tempVar = heap.pop(storedVar)
        tree.append((tempVar[0],(tempVar[0],tempVar[1])))
        pointsTree.append(tempVar[0])
        pointsTree.append(tempVar[1])
        edgeTree.append((tempVar[0],tempVar[1]))
        neighborsNearMe = list(neighbors(graph,tempVar[0]))
        weightTuple = []
        listOfNeighborWeight = []
        for i in range(len(neighborsNearMe)):
            listOfNeighborWeight.append(graph[tempVar[0]][neighborsNearMe[i]]["weight"])
        weightTuple = list(zip(neighborsNearMe,listOfNeighborWeight))
        weightTuple = sorted(weightTuple,key=itemgetter(1))
        for y in range(len(weightTuple)):
            tempDict = list(edgeDict[weightTuple[y][0]])
            if((weightTuple[y][1] < tempDict[1] or tempVar[2] == 0)and weightTuple[y][0] not in pointsTree):
                heapList = []
                for g in range(len(heap)):
                    tempList = list(heap[g])
                    heapList.append(tempList)
                    if(tempList[0] == weightTuple[y][0]):
                        storedVar = g
                heap.pop(storedVar)
                heapq.heappush(heap,(weightTuple[y][0],tempVar[0],weightTuple[y][1]))
                edgeDict[weightTuple[y][0]] = tempVar[0], weightTuple[y][1]
    pairs = []
    for n in range(len(edgeDict)):
        tempList = list(edgeDict[n])
        if(tempList[0] != ''):
            if(n < tempList[0]):
                pairs.append((n,tempList[0],tempList[1]))
            else:
                pairs.append((tempList[0],n,tempList[1]))
    pairs = sorted(pairs)
    return pairs

def minDistanceTwoPoints(u,graph):
    nodes = list(graph.nodes)
    nodes = sorted(nodes)
    edges = graph.edges.data("weight", default=1)
    edges = sorted(edges,key=itemgetter(2))
    heap = []
    edgeDict = dict()
    for i in range(0,len(nodes)):
        heapq.heappush(heap,(nodes[i],"",inf))
        edgeDict[nodes[i]] = "",inf
    heap.pop(nodes[u])
    heapq.heappush(heap,(nodes[u],"",0))
    edgeDict[nodes[u]] = "",0
    while(len(heap) > 0):
        formattedHeap = []
        for line in heap:
            formattedHeap.append(list(line))
        formattedHeap = sorted(formattedHeap,key=itemgetter(2))
        for a in range(len(heap)):
            tempList = list(heap[a])
            if(tempList[0] == formattedHeap[0][0]):
                storedVar = a
        tempVar = heap.pop(storedVar)
        neighborsNearMe = list(neighbors(graph,tempVar[0]))
        weightTuple = []
        listOfNeighborWeight = []
        for i in range(len(neighborsNearMe)):
            listOfNeighborWeight.append(graph[tempVar[0]][neighborsNearMe[i]]["weight"])
        weightTuple = list(zip(neighborsNearMe,listOfNeighborWeight))
        weightTuple = sorted(weightTuple,key=itemgetter(1))
        heapList = []
        for i in range(len(heap)):
            heapList.append(heap[i][0])
        for y in range(len(weightTuple)):
            tempList = list(edgeDict[weightTuple[y][0]])
            if(weightTuple[y][0] in heapList and weightTuple[y][1] + tempVar[2] < tempList[1]):
                edgeDict[weightTuple[y][0]] = tempVar[0],weightTuple[y][1] + tempVar[2]
                for g in range(len(heap)):
                    tempList = list(heap[g])
                    if(tempList[0] == weightTuple[y][0]):
                        storedVar = g
                heap.pop(storedVar)
                heapq.heappush(heap,(weightTuple[y][0],tempVar[0],weightTuple[y][1] + tempVar[2]))
    return edgeDict

print("Depth First Traversal (vertex visited order):")
setToWhite(g)
print(DFSAlgorithm(g,[],0))
print("\nBreadth First Traversal (lowest-weight-next):")
print(BFSTraversal(g,[],0))
print("\nMinimum Spanning Tree")
minSpanTree = minSpanningTreePrim(g)
weight = 0
for i in range(len(minSpanTree)):
    print(minSpanTree[i])
    weight += minSpanTree[i][2]
if(isDisconnected(g,[],0) == True):
    print("Type: Spanning Forest")
else:
    print("Type: Full Spanning Tree")
print("Total Weight: {0}\n".format(weight))
print("Shortest Paths:")

n = list(g.nodes)
n = sorted(n)
for i in range(numVertices):
    starting = n[i]
    currDict = minDistanceTwoPoints(starting,g)
    valList = list(currDict.values())
    key_list = list(currDict.keys())
    for j in range(numVertices):
        dictValues = list(currDict[j])
        currentNum = n[j]
        pairList = []
        token = True
        if(currentNum > starting):
            weight = 0
            formattedPairs = []
            if(dictValues[0] == starting and dictValues[1] != inf):
                weight = dictValues[1]
                pairList.append((currentNum,dictValues[0]))
            elif(dictValues[1] == inf):
                token = False
            else:
                while(dictValues[0] != starting):
                    weight += currDict[currentNum][1]
                    if(len(pairList) == 0):
                        pairList.append((dictValues[0],currentNum))
                        position = dictValues[0]
                        dictValues = list(currDict[dictValues[0]]) 
                    else:
                        pairList.append((j,dictValues[0]))
                        position = dictValues[0]
                        dictValues = list(currDict[dictValues[0]])   
                    pairList.append((position,dictValues[0]))
            for line in pairList:
                if(line[1] < line[0]):
                    formattedPairs.append((line[1],line[0]))
                else:
                    formattedPairs.append((line[0],line[1]))
            formattedPairs = sorted(formattedPairs)
            print("{0} -> {1}".format(starting,currentNum))
            edges = list(g.edges.data("weight", default=1))
            edgeList = []
            weightList = []
            newPairs = []
            for i in range(len(edges)):
                if(edges[i][0] > edges[i][1]):
                    edgeList.append((edges[i][1],edges[i][0]))
                    weightList.append(edges[i][2])
                else:
                    edgeList.append((edges[i][0],edges[i][1]))
                    weightList.append(edges[i][2])
            weight = 0
            if(len(formattedPairs) > 0):
                for i in range(len(formattedPairs)):
                    if(formattedPairs[i] in edgeList):
                        newPairs.append(formattedPairs[i])
                        spot = edgeList.index(formattedPairs[i])
                        weight = weight + weightList[spot]
                print("   {0}".format(newPairs))
                print("     Path Weight: {0}".format(weight))
            if(token == False):
                print("     No Path")
