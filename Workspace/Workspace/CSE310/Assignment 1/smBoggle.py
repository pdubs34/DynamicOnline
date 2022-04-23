import sys
from bisect import bisect_left

dict = open(sys.argv[2], 'r')
inputfile = open(sys.argv[1], 'r')
matrix = inputfile.readlines()
dictList = dict.readlines()
i= 0
u = 0
v = 0
shortenedDict = []
for line in dictList:
    if (len(line) > 2) and (len(line) < 9):
      strippedLine = line.rstrip()
      shortenedDict.append(strippedLine)
      i = i + 1
answers = ["ope","peg","ego"]
# def BinarySearch(a, x):
#     i = bisect_left(a, x)
#     if i != len(a) and a[i] == x:
#         return i
#     else:
#         return -1

# t = BinarySearch(shortenedDict,'ace')
# if(t != 1):
#     print("found it")
# res = BinarySearch(shortenedDict, 'voyeurism')
# if res == -1:
#     print("book" + "is absent")
# else:
#     print("Book is in the dictionary")


def findSolution(matrix,visited, xCord, yCord, string):
    visited[xCord][yCord] = 1
    string = string + matrix[xCord][yCord]
    # match = BinarySearch(shortenedDict,string)
    if string in answers:
        print(string)
    xCordOriginal = xCord
    yCordOriginal = yCord
    row = 0
    col = 0
    for row in range(-1,2):
        xCord = xCordOriginal + row
        for col in range(-1,2):
            yCord = yCordOriginal + col
            if (xCord >= 0 and yCord >= 0 and yCord < 3 and xCord < 3 and visited[xCord][yCord] != 1):
                findSolution(matrix, visited, xCord, yCord, string)
               
                
    string = string[:-1]
    visited[xCordOriginal][yCordOriginal] = 0

string = ''
for u in range(3):
    for v in range(3):
        visited =  [[0,0,0],
            [0,0,0],
            [0,0,0],]
        findSolution(matrix,visited,u,v,string)

inputfile.close()