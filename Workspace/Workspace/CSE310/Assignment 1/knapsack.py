from bisect import bisect_left
import sys

inputfile = open(sys.argv[1], 'r')
knapsack = inputfile.readlines()
formatKnapsack = []

for line in knapsack:
    line.strip
    formatKnapsack.append(line)


firstLine =  formatKnapsack[0].split(" ")
n = int(firstLine[0])
wMax = float((firstLine[1]))
weightLine = formatKnapsack[1].split(" ")
valueLine = formatKnapsack[2].split(" ")

j = 0
solution = []
totalWeight = 0
totalValue = 0

def knapSack(weightLine,valueLine,solution,totalValue,totalWeight,j):
    if(j == n):
        return solution
    bestSol = solution
    for k in range(j+1,n+1):
        if k - 1 not in solution:
            currentSol = solution + [k - 1]
        totalValue = findTotalValue(currentSol)
        totalWeight = findTotalWeight(currentSol)
        if(totalWeight <= wMax):
            solution = knapSack(weightLine,valueLine,currentSol,totalValue,totalWeight,k)
        if(findTotalValue(solution) > findTotalValue(bestSol)):
            bestSol = solution
        totalWeight = 0
        totalValue = 0
    return bestSol

def findTotalValue(solution):
    value = 0
    for i in solution:
        value = value + float(valueLine[i])
    return value

def findTotalWeight(solution):
    value = 0
    for i in solution:
        value = value + float(weightLine[i])
    return value
solutions = []
optimalSolution = knapSack(weightLine,valueLine,solution,totalValue,totalWeight,j)
j = j+1

for j  in range(n):
    solutions = knapSack(weightLine,valueLine,solution,totalValue,totalWeight,j)
    if(findTotalValue(solutions) > findTotalValue(optimalSolution) ):
        optimalSolution = solutions
if (len(optimalSolution) == 0):
    print("No optimal Solution")
else:
    print("Optimal knapsack:{0}".format(optimalSolution))
