import sys

inputfile = open(sys.argv[1], 'r')
infoSet = set()
peopleSet = set()
number = 0
numLines = 0
noResponses = 0
yesResponses = 0

for lines in inputfile:
    if (number > 0):
        infoSet.add(lines)
        number = number + 1

for lines in infoSet:
    numLines = numLines + 1

def YesOrNoCalculator(Info):
    line =  Info[0].split(",")
    peopleSet.add(line[0])
    if(line[1] == "Yay"):
        response = "yes"
    else:
        response = "no"
    return response

response = YesOrNoCalculator(infoSet)
if(response == "yes"):
    yesResponses = yesResponses + 1
else:
    noResponses = noResponses + 1


print("People:",peopleSet)
print("Yes Responses",yesResponses)
print("No Responses", noResponses)
inputfile.close()
