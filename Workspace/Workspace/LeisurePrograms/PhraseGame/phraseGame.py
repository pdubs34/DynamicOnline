import sys
import random

inputfile = open(sys.argv[1], 'r')
dictPhrases = inputfile.readlines()

def findTotalLines(dict):
    counter = 0
    for line in dict:
        counter = counter + 1
    return counter

numlines = findTotalLines(dictPhrases)
phraseToGet = random.randint(0,numlines - 1)
print("{0}".format(dictPhrases[phraseToGet]))




