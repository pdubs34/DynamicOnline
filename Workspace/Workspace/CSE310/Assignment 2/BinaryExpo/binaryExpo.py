import sys
a = sys.argv[1]
m = sys.argv[2]
n = sys.argv[3]

n = int(n)
m = int(m)
a = int(a)

def binaryExpo(a,m,n):
    term = a
    binaryNumber = format(n,'b')
    k = len(binaryNumber)
    if(int(binaryNumber[k - 1]) == 1):
        product = a
    else:
        product = 1
    i = 1
    for i in range(1,k): 
        term = (term * term) % m
        if(int(binaryNumber[k - (i+1)]) == 1):
            product = (product * term) % m
    return product

a = 7
n = 2600072
m = 42

result = binaryExpo(a,m,n)
print("{0}^{1} mod {2} = {3}".format(a,n,m,result))