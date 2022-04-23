"""
CSCE 310
Summer 2021

A collection of recursive divide-and-conquer algorithms and functions.

- You must implement the largest(), addAll() and median() methods
- You may not use any library or built-in methods to implement these
- All implementations *must* be recursive/divide-and-conquer
- The defined methods must be used and should be considered "entry
  points" for your own recursive function that you should define

Author: Payton Webb, Matt Hotovy
"""
import copy
import math

"""
Partitions the given array (arr) around a pivot element which is chosen
to be the last element in the array.  Partitioning means that all elements
less than the pivot will appear before the pivot and all elements greater
will appear after but there is no guarantee that the original order will
be preserved.

Once partitioned, the function
returns the index at which the pivot element ends up.

For example, with an input of arr = [8, 4, 1, 9, 3, 5], the pivot
would element would be 5 (the last element) and after partitioning, the
array may look like:
  [4, 1, 3, 5, 8, 9]
and the function will return 3 (the index where 5 ends up)
"""
def partition(arr):
    if len(arr) == 1:
      return 0
    i = -1
    n = len(arr)-1
    pivot = arr[n]

    for j in range(0 , n):
        if arr[j] <= pivot:
          i = i+1
          arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[n] = arr[n],arr[i+1]
    return ( i+1 )

"""
Searches the given array for the provided key, returns
true if the array contains the key.

This function has been done for you as an example.  This
function is the non-recursive "entry point"
"""
def contains( arr, key ):
  # start the search at index 0...
  return containsRecursive(arr, key, 0)
  # alternative:
  # return containsRecursiveDivide(arr, key)

"""
Recursive contains function
"""
def containsRecursive( arr, key, index ):
  if index > len(arr)-1:
    return False
  elif arr[index] == key:
    return True
  else:
    return containsRecursive(arr, key, index+1)

"""
Recursive (divide/conquer) contains function
"""
def containsRecursiveDivide( arr, key ):

  if(len(arr) == 0):
    return False
  elif len(arr) == 1:
    return arr[0] == key
  else:
    m = int(len(arr)/2)
    return containsRecursiveDivide(arr[0:m], key) or containsRecursiveDivide(arr[m:], key)


"""
Finds and returns the maximum value in the given array
"""
def largest( arr ):
  if(len(arr) == 1):
    return arr
  return 1

"""
Computes the sum of all elements in the given array.
"""
def addAll( arr ):
  ## TODO: implement calling your own recursive function
  ## this method is just the entry point to the recursion
  return 1

"""
Computes the median element of the given array, but
does *not* modify the given array.
"""
def median( arr ):
  # make a copy to recurse on:
  b = copy.deepcopy(arr)
  if(len(arr) == 1):
    return arr
  arr.sort()
  median = math.floor((len(arr)/2))
  return arr[median]

# def recursiveLargest(arr):
#   middle = len(arr)/2
#   if(len(arr) == 1):
#     return arr[0]
#   elif(len(arr) == 2):
#     if(arr[0] > arr[1]):
#       return arr[0]
#     elif(arr[1] >= arr[0]):
#       return arr[1]
#   return max(recursiveLargest(arr[0:middle]),recursiveLargest(arr[middle:]))

def recursiveMedian(arr):
 print(arr)
 if(len(arr) == 1):
    return arr[0]
 elif(len(arr) == 2):
    if(arr[0] > arr[1]):
      print("joe")
      return arr[1]
    elif(arr[1] >= arr[0]):
      print("momma")
      return arr[0]
 m = math.floor((len(arr)/2))
 partitionPoint = partition(arr)
 if(len(arr[0:partitionPoint]) > len(arr[partitionPoint:len(arr)])):
   recursiveMedian(arr[0:m])
 if(len(arr[partitionPoint:len(arr)]) > len(arr[0:partitionPoint])):
   recursiveMedian(arr[m:len(arr)])
 if(len(arr[partitionPoint:len(arr)]) == len(arr[0:partitionPoint])):
   return arr[partitionPoint]
