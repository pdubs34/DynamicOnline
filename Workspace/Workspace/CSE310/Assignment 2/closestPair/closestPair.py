import math
from operator import itemgetter
import sys

inputfile = open(sys.argv[1], 'r')
pairs = inputfile.readlines()
formattedPairs = []
for line in pairs:
    line.strip
    formattedPairs.append(line)

n = int(pairs[0])
pairs = []
print(n)
for i in range(1, n + 1):
    set = formattedPairs[i].split(" ")
    xCord = float(set[0])
    yCord = float(set[1])
    point = (xCord,yCord)
    pairs.append(point)

minDist = 9999999999999
xSortedPairs =  sorted(pairs)

def findLeftArrayIndex(array,d,XorY):
    i = 0
    n = len(array) - 1
    index = -1
    if(d < array[i][XorY]):
       return n

    while (i <= n):
        mid = (i + n) // 2
        if (array[mid][XorY] <= d):
            i = mid + 1
        else:
            index = mid
            n = mid - 1
 
    return index

def findRightArrayIndex(array,d,XorY):
    i = 0
    n = len(array) - 1
    if(d > array[n][XorY]):
       return n
    index = 0
    while (i <= n):

        mid = ((i + n)// 2)
        if (array[mid][XorY] > d):
            n = mid - 1
        else:
            index = mid
            i = mid + 1
    return index


def findDistance(p,q):
    return math.sqrt( (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1]) )

def bruteForceClosest(points, n , minDist):
    minDistPair = []
    for i in range(n - 1):
        for j in range(i+1,n):
            d = findDistance(points[i], points[j])
            if(d < minDist):
                minDist = d
                minDistPair = []
                minDistPair.append(points[i])
                minDistPair.append(points[j])
    return minDistPair

def recursiveClosest(points,n,minDist,smallestPair):
    if(n <= 6):
        return bruteForceClosest(points,n,minDist)
    middle = int((n)/2)
    leftPartition = points[:middle]
    rightPartition = points[middle:]
    # Divide and Conquer until size is brute-force
    leftPair = (recursiveClosest(leftPartition,len(leftPartition),minDist,smallestPair))
    rightPair = (recursiveClosest(rightPartition,len(rightPartition),minDist,smallestPair))
    #Set whichever half to the minDistance/smallestPoints
    if(findDistance(leftPair[0],leftPair[1]) > findDistance(rightPair[0],rightPair[1])):
        minDist = findDistance(rightPair[0],rightPair[1])
        smallestPair = rightPair
    else:
        minDist = findDistance(leftPair[0],leftPair[1])
        smallestPair = leftPair
    median = points[middle]
    leftArray = []
    rightArray = []
    center = median[0]
    xMax = center + minDist
    xMin = center - minDist
    leftArray = leftPartition[findRightArrayIndex(leftPartition,xMin,0):]
    rightArray = rightPartition[:findLeftArrayIndex(rightPartition,xMax,0)]
    if(len(leftArray) > 0 and len(rightArray) > 0):
        ySortedLeftArray = sorted(leftArray,key=itemgetter(1))
        ySortedRightArray = sorted(rightArray,key=itemgetter(1))
        for i in range(len(ySortedLeftArray)):
            maxY = ySortedLeftArray[i][1] + minDist
            minY = ySortedLeftArray[i][1] - minDist
            right = findRightArrayIndex(ySortedRightArray,maxY - 0.00001,1)
            left = findLeftArrayIndex(ySortedRightArray,minY-0.0001,1)
            binarySearchedArray = ySortedRightArray[left:right + 1]
            j = i 
            while j < len(binarySearchedArray):
                distance = findDistance(ySortedLeftArray[i], binarySearchedArray[j])
                if(distance < minDist):
                    smallestPair = (ySortedLeftArray[i],binarySearchedArray[j])
                    minDist = distance
                j += 1
    
    return smallestPair

smallestPair = []
leftPair = []
rightPair = []
smallestPair = recursiveClosest(xSortedPairs,n,minDist,smallestPair)
print("==========OPTIMAL==========")
print("{0}".format(smallestPair[0]))
print("{0}".format(smallestPair[1]))
print(findDistance(smallestPair[0],smallestPair[1]))