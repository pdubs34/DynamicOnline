import sys
import math
import heapq

#What I need to do first is go through the file and pick out each character from the
# file and add it to the character set and from there figure out the frequency of that character

charList = []
codeWordList = []
frequencyList = []
input = open(sys.argv[1], 'r')

for line in input:

   for i in range(0, len(line)):

      if line[i] in charList:
         #had to creat another loop to make sure that I was incrementing the list at teh correct index
         for j in range(0, len(charList)):
            if(line[i] == charList[j]):
               frequencyList[j] = frequencyList[j] + 1
      else:
         charList.append(line[i])
         frequencyList.append(1)
         
totalCharacters = 0
for i in range(0, len(frequencyList)):
   totalCharacters = totalCharacters + frequencyList[i]

for i in range(0, len(frequencyList)):
   frequencyList[i] = float(frequencyList[i] / float(totalCharacters))

def createHuffmanTree(charList, frequencyList):
   heap = []
   for i in range(0, len(charList)):
      heapq.heappush(heap, (frequencyList[i], charList[i]))
   
   while (len(heap) > 1):
      
      leftChild = heapq.heappop(heap)
      rightChild =  heapq.heappop(heap)
      parentFrequency = (leftChild[0] + rightChild[0])
      parent = (parentFrequency, (leftChild[1], rightChild[1]))
      heapq.heappush(heap, parent)
   
   return (heap)

heap = createHuffmanTree(charList, frequencyList)

def findCodeWords(heap, charList, codeWord):
   # My idea here is that I could go through the charList index by index and for each index
   # look for the corresponding position in the heap as that char and then when I find that char 
   # I can add its codeword to the CodeworSet at teh same index that the char is at in the charList
   # this function can return the codeWordSet after it is done and then I can print off the charList,
   # frequencyList and codewordList at the end
   codeWordList = [None]*len(charList)

   if isinstance(heap[0], tuple):
      leftSideList = findCodeWords(heap[0], charList, (codeWord + '0'))
      for i in range(0, len(leftSideList)):
         if (codeWordList[i] == None) and (leftSideList[i] != None):
            codeWordList[i] = leftSideList[i]
   else:
      codeWord = codeWord + '0'
      index = charList.index(heap[0])
      codeWordList[index] = codeWord
      codeWord = codeWord[:-1]
   
   if isinstance(heap[1], tuple):
      rightSideList = findCodeWords(heap[1], charList, (codeWord + '1'))
      for i in range(0, len(rightSideList)):
         if (codeWordList[i] == None) and (rightSideList[i] != None):
            codeWordList[i] = rightSideList[i]
   else:
      codeWord = codeWord + '1'
      index = charList.index(heap[1])
      codeWordList[index] = codeWord
      codeWord = codeWord[:-1]

   return codeWordList
codeWordList = findCodeWords(heap[0][1], charList, '')
averageWordLength = 0
sortedList = []
for i in range(len(charList)):
    item = (frequencyList[i],charList[i],codeWordList[i])
    sortedList.append(item)
sortedList.sort(key = lambda x: x[1])
uniqueCharacters = 0
print("Character Codeword Frequency")
for i in range(len(sortedList)):
    if(sortedList[i] != "\n"):
        uniqueCharacters = uniqueCharacters + 1
        totalCharacters = totalCharacters + sortedList[i][0]
        character = sortedList[i][1]
        codeWord = sortedList[i][2]
        frequency =  sortedList[i][0]
        codeWordLength = float(len(codeWord)) * float(frequency)
        frequency =  sortedList[i][0] * 100
        averageWordLength += codeWordLength
        print("{0}          {1}             {2}%".format(character,codeWord,frequency))
blockLength = int(math.ceil(math.log(uniqueCharacters,2)))
totalCharacters = totalCharacters - 1
totalCharactersOriginal = int(totalCharacters * 8)
print("ASCII Codeword Length: 8")
print("Block Length Encoding Codeword Length: {0}".format(blockLength))
print("Average Codeword Length  {0}".format(averageWordLength))
print("Original File Size (ASCII bits):            {0}".format(totalCharactersOriginal))
totalCharactersBlock = int(totalCharacters * blockLength)
print("Original File Size (Block length encoding):  {0}".format(totalCharactersBlock))
print("Actual Encoding Size (bits):      {0}".format(int(averageWordLength * totalCharacters)))
print("Average Codeword Length Compression:   {0}%".format(((blockLength-averageWordLength)/blockLength)*100))
print("File Compression Ratio:      {0}%".format(float((averageWordLength * totalCharacters)/totalCharactersOriginal)*100))

