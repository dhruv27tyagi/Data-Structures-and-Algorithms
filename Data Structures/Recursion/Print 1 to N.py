## 1. Printing from 1 to N

def print1toN(n):

    if n<=0: # base case
        return

    print1toN(n-1)

    print(n)

print1toN(5)

## Printing fron N to 1

def printNto1(n):

    if n<=0:
        return
    
    print(n)
    printNto1(n-1)

printNto1(5)