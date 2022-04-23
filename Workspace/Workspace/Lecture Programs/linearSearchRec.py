import math

def linearSearchRec(a,key,l,r):
    if l > r:
        return -1
    m = math.floor( (l + r) / 2)
    if a[m] == key:
        return m
    index = linearSearchRec(a, key, l, m - 1)
    if index > -1:
        return index
    return linearSearchRec(a, key, m+1,r)

a = {0,1,4,5,2,3,9,2,3,42}
key = 101
index = linearSearchRec(a, key, 0, len(a)-1)
print("%d found at index %d"(key, index))