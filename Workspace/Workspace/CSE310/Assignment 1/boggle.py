import sys

from bisect import bisect_left


dict = open(sys.argv[2], 'r')
inputfile = open(sys.argv[1], 'r')
matrix = inputfile.readlines()
dictList = dict.readlines()
wordSet = set()
i= 0
u = 0
v = 0
shortenedDict_set = set()
threewordSet = set()
fourwordSet = set()
fivewordSet = set()
sixwordSet = set()
sevenwordSet = set()
eightwordSet = set()
ninewordSet = set()
tenwordSet = set()
elevenwordSet = set()
twelvewordSet = set()
thirteenwordSet = set()
fourteenwordSet = set()
fifteenwordSet = set()
sixteenwordSet = set()

for line in dictList:
    strippedLine = line.rstrip()
    shortenedDict_set.add(strippedLine)

def findSolution(matrix,visited, xCord, yCord, string):
    visited[xCord][yCord] = 1
    string = string + matrix[xCord][yCord]
    if string in shortenedDict_set and len(string) > 2 and len(string) < 17 :
            if(len(string) == 3):
                threewordSet.add(string)
            if(len(string) == 4):
                fourwordSet.add(string)
            if(len(string) == 5):
                fivewordSet.add(string)
            if(len(string) == 6):
                sixwordSet.add(string)
            if(len(string) == 7):
                sevenwordSet.add(string)
            if(len(string) == 8):
                eightwordSet.add(string)
            if(len(string) == 9):
                ninewordSet.add(string)
            if(len(string) == 10):
                tenwordSet.add(string)
            if(len(string) == 11):
                elevenwordSet.add(string)
            if(len(string) == 12):
                twelvewordSet.add(string)
            if(len(string) == 13):
                thirteenwordSet.add(string)
            if(len(string) == 14):
                fourteenwordSet.add(string)
            if(len(string) == 15):
                fifteenwordSet.add(string)
            if(len(string) == 16):
                sixteenwordSet.add(string)
    xCordOriginal = xCord
    yCordOriginal = yCord
    row = 0
    col = 0
    for row in range(-1,2):
        xCord = xCordOriginal + row
        for col in range(-1,2):
            yCord = yCordOriginal + col
            if (xCord >= 0 and yCord >= 0 and yCord < 4 and xCord < 4 and visited[xCord][yCord] != 1):
                findSolution(matrix, visited, xCord, yCord, string)       
    string = string[:-1]
    visited[xCordOriginal][yCordOriginal] = 0

string = ''
for u in range(4):
    for v in range(4):
        visited =  [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
        findSolution(matrix,visited,u,v,string)
sortedList = sorted(wordSet)
for line in matrix:
    print(line)
print("Words Formed:0")
counter = 0
if(len(threewordSet)!= 0):
    print("Length 3 ({0})".format(len(threewordSet)))
    print("==============")
    threewordSet = sorted(threewordSet)
    for line in threewordSet:
        counter = counter + 1
        print(line)
if(len(fourwordSet)!= 0):
    print("Length 4 ({0})".format(len(fourwordSet)))
    print("==============")
    fourwordSet = sorted(fourwordSet)
    for line in fourwordSet:
        counter = counter + 1
        print(line)
if(len(fivewordSet)!= 0):
    print("Length 5 ({0})".format(len(fivewordSet)))
    print("==============")
    fivewordSet = sorted(fivewordSet)
    for line in fivewordSet:
        counter = counter + 1
        print(line)
if(len(sixwordSet)!= 0):
    print("Length 6 ({0})".format(len(sixwordSet)))
    print("==============")
    sixwordSet = sorted(sixwordSet)
    for line in sixwordSet:
        counter = counter + 1
        print(line)
if(len(sevenwordSet)!= 0):
    print("Length 7 ({0})".format(len(sevenwordSet)))
    print("==============")
    sevenwordSet = sorted(sevenwordSet)
    for line in sevenwordSet:
        counter = counter + 1
        print(line)
if(len(eightwordSet)!= 0):
    print("Length 8 ({0})".format(len(eightwordSet)))
    print("==============")
    eightwordSet = sorted(eightwordSet)
    for line in eightwordSet:
        counter = counter + 1
        print(line)
if(len(ninewordSet)!= 0):
    print("Length 9 ({0})".format(len(ninewordSet)))
    print("==============")
    ninewordSet = sorted(ninewordSet)
    for line in ninewordSet:
        counter = counter + 1
        print(line)
if(len(tenwordSet)!= 0):
    print("Length 10 ({0})".format(len(tenwordSet)))
    print("==============")
    tenwordSet = sorted(tenwordSet)
    for line in tenwordSet:
        counter = counter + 1
        print(line)
if(len(elevenwordSet)!= 0):
    print("Length 11 ({0})".format(len(elevenwordSet)))
    print("==============")
    elevenwordSet = sorted(elevenwordSet)
    for line in elevenwordSet:
        counter = counter + 1
        print(line)
if(len(twelvewordSet)!= 0):
    print("Length 12 ({0})".format(len(twelvewordSet)))
    print("==============")
    twelvewordSet = sorted(twelvewordSet)
    for line in twelvewordSet:
        counter = counter + 1
        print(line)
if(len(thirteenwordSet)!= 0):
    print("Length 13 ({0})".format(len(thirteenwordSet)))
    print("==============")
    thirteenwordSet = sorted(thirteenwordSet)
    for line in thirteenwordSet:
        counter = counter + 1
        print(line)
if(len(fourteenwordSet)!= 0):
    print("Length 14 ({0})".format(len(fourteenwordSet)))
    print("==============")
    fourteenwordSet = sorted(fourteenwordSet)
    for line in fourteenwordSet:
        counter = counter + 1
        print(line)
if(len(fifteenwordSet)!= 0):
    print("Length 15 ({0})".format(len(fifteenwordSet)))
    print("==============")
    fifteenwordSet = sorted(fifteenwordSet)
    for line in fifteenwordSet:
        counter = counter + 1
        print(line)
if(len(sixteenwordSet)!= 0):
    print("Length 16 ({0})".format(len(sixteenwordSet)))
    print("==============")
    sixteenwordSet = sorted(sixteenwordSet)
    for line in sixteenwordSet:
        counter = counter + 1
        print(line)

print("Total number of words formed: {0}".format(counter))     
inputfile.close()