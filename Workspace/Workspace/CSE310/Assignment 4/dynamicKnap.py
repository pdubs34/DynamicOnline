from bisect import bisect_left
import sys
import pprint

inputfile = open(sys.argv[1], 'r')
knapsack = inputfile.readlines()
formatKnapsack = []

for line in knapsack:
    line.strip
    formatKnapsack.append(line)
minWeight = int(min(formatKnapsack[1].split(" ")))

firstLine =  formatKnapsack[0].split(" ")
n = int(firstLine[0])
wMax = int((firstLine[1]))
weightLine = [0]
valueLine = [0]
weights = formatKnapsack[1].split(" ")
values = formatKnapsack[2].split(" ")
for i in range(n):
    weightLine.append(int(weights[i]))
    valueLine.append(int(values[i]))
    
def knapsackTable(weightLine,valueLine):
    table = {}
    for g in range(wMax + 1):
        table[(0,g)] = 0
    for t in range(n+1):
        for s in range(2):
            table[(t,s)] = 0

    for i in range(1,n + 1):
        for j in range(1,wMax + 1):
            if (j - weightLine[i] >= 0):
                if(table[(i - 1,j)] > table[(i - 1,j - weightLine[i])] + valueLine[i]):
                    table[(i,j)] = table[(i-1,j)] 
                else:
                    table[(i,j)] = table[(i-1,j - weightLine[i])] + valueLine[i]
            else:
                table[(i,j)] = table[(i - 1,j)]
    return table

def findSolution(table):
    items = []
    i = n
    j = wMax
    while(i >= 1 and j >= 1):
        while(i >= 1 and table[(i,j)] == table[(i - 1,j)]):
            i = i - 1
        if(weightLine[i] != 0):
            items.append((i,weightLine[i],valueLine[i]))
        j = j - weightLine[i]
        i = i - 1
    return items

table = knapsackTable(weightLine,valueLine)
print("Tableau:")
for i in range(n + 1):
    iList = []
    for j in range(wMax + 1):
        iList.append(table[(i,j)])
        if(j == wMax):
            print(iList)
print("Maximum Capacity: W = {0}".format(wMax))
original = []
for t in range(1,n + 1):
    original.append((t,weightLine[t],valueLine[t]))
print("Original Knapsack Items: {0}".format(original))
result = findSolution(table)
result = sorted(result)
print("Optimal Knapsack Items: {0}".format(result))
weight = 0
value = 0
for s in range(len(result)):
    currWeight = result[s][1]
    currValue = result[s][2]
    weight = weight + currWeight
    value = value + currValue
print("Optimal Weight: {0}".format(weight))
print("Optimal Value: {0}".format(value))
