from operator import index
import sys

def findLeftArrayIndex(array,d):
    i = 0
    n = len(array) - 1
    if(d < array[i]):
       return n
    index = -1
    while (i <= n):
        mid = (i + n) // 2
        if (array[mid] <= d):
            i = mid + 1
        else:
            index = mid
            n = mid - 1
 
    return index
def findLeftArrayIndexd(array,d,start,end,index):
    if(len(array)>start):
        if(d < array[start]):
            return end
        if(start <= end):
            mid = (start + end) // 2
        if (array[mid] <= d):
            start = mid + 1
            return(findLeftArrayIndexd(array,d,start,end,index))
        else:
            index = mid
            end = mid - 1
            return(findLeftArrayIndexd(array,d,start,end,index))
    return index

def findRightArrayIndex(array,d):
    i = 0
    n = len(array) - 1
    if(d > array[n]):
       return n
    index = 0
    while (i <= n):
        mid = ((i + n)// 2)
        if (array[mid] > d):
            n = mid - 1
        else:
            index = mid
            i = mid + 1
    return index

array = [10,11,12]
array2 = [(2,10),(2,11),(2,12)]
middleArray = array
# middleArray = array[:findRightArrayIndex(array2,8,1)+1 ]
number = findLeftArrayIndexd(array,10.999999,0,len(array)-1,0)
print(number)
number2 = findRightArrayIndex(array,13.9999)
# print(middleArray)
# number2 = findLeftArrayIndexd(array,13,0,len(array),0)
print(array[:number])