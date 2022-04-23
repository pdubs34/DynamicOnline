import sys
from collections import Counter
import heapq
from operator import attrgetter

file = open(sys.argv[1], "r")
charList = []
codeWordList = []
frequencyList = []

for line in file:
   for i in range(0, len(line)):

      if line[i] in charList:
         #had to creat another loop to make sure that I was incrementing the list at teh correct index
         for j in range(0, len(charList)):
            if(line[i] == charList[j]):
               frequencyList[j] = frequencyList[j] + 1
      else:
         charList.append(line[i])
         frequencyList.append(1)

class TreeNode:
    def __init__(self,frequency,character,leftNode = None,rightNode = None):
        self.frequency = frequency
        self.character = character
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.binaryRep = ""

def getTreeNodeFrequency(node):
    return node.frequency
totalCharacters = 0

for i in range(0, len(frequencyList)):
   totalCharacters = totalCharacters + frequencyList[i]

for i in range(0, len(frequencyList)):
   frequencyList[i] = float(frequencyList[i] / totalCharacters)

nodeList = []
for i in range(0, len(charList)):
   newNode = TreeNode(frequencyList[i], charList[i])
   nodeList.append(newNode)

def createHuffmanTree(nodeList):
    heap = []
    for i in range(0, len(nodeList)):
      heap.append(nodeList[i])
    heap = sorted(heap, key= getTreeNodeFrequency)  
    while len(heap) > 1:
        rootNode = TreeNode(0,"")
        leftNode = heap[0]
        leftNode.binaryRep = 0
        rightNode = heap[1]
        rightNode.binaryRep = 1
        rootNode.frequency = (leftNode.frequency + rightNode.frequency)
        rootNode.character = (leftNode.character + rightNode.character)
        rootNode.leftNode = leftNode
        rootNode.rightNode = rightNode
        heap.remove(leftNode)
        heap.remove(rightNode)
        heap.append(rootNode)
    return heap



print(createHuffmanTree(nodeList))
#    while (len(heap) > 1): 
#       leftChild = heapq.heappop(heap)
#       rightChild =  heapq.heappop(heap)
#       parentFrequency = (leftChild.frequency + rightChild.frequency)
#       #parent = (parentFrequency, (leftChild[1], rightChild[1]))
#       parent = TreeNode(parentFrequency, None, leftChild, rightChild)
#       heapq.heappush(heap, parent)



# for i in range(len(collectionOfChar)):
#     node[i] = TreeNode(collectionOfChar.character,collectionOfChar.frequency)

heap = []