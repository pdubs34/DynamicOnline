from bisect import bisect_left
import sys
import pprint

inputfile = open(sys.argv[1], 'r')
word = inputfile.readlines()

def contiguousPalindromeLength(string):
    end = len(string) - 1
    start = 0
    while(start < end):
        if(string[start] == string[end]):
            start = start + 1
            end = end - 1
        else:
            return 0
    return len(string)

def noncontiguousPalindromeLength(string):
    word = []
    singleChar = []
    for element in range(len(string)):
        word.append(string[element])
    longestPalindrome = []
    while(len(word) > 1):
        currLetter = word[0]
        print(word)
        element = 1
        for element in range(1, len(word) ):
            letter = word[element]
            if(letter == currLetter):  
                longestPalindrome.append(currLetter)
                longestPalindrome.append(letter)
                word.remove(currLetter)
                word.remove(letter)
                break
            elif(element == len(word) - 1):
                word.remove(currLetter)
                singleChar.append(currLetter)
                break
    if(len(singleChar) > 0):
        n = int((len(longestPalindrome) / 2))
        longestPalindrome.insert(n,singleChar[0])

    return len(longestPalindrome)
            
            


def palindromeTable(string):
    table = {}
    for g in range(len(string)):
        for t in range(len(string)):
            table[(g,t)] = 0
    for i in range(len(string)):
        for j in range(i + 1,len(string)):
            currLength = contiguousPalindromeLength(string[i:j+1])
            if(currLength > table[(i,j -1)]):
                table[(i,j)] = currLength
            else:
                table[(i,j)] = table[(i,j - 1)]
    return table

print(noncontiguousPalindromeLength(word[0]))
# table = palindromeTable(word[0])
# palindromeValues = table.values()
# biggest = max(palindromeValues)
# print(word[0])
# print(table)
# print(biggest)