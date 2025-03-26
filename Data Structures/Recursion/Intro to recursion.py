def printNumFive(num):
    print(num)
    printNumfour(num-1)

def printNumfour(num):
    print(num)
    printNumthree(num-1)

def printNumthree(num):
    print(num)

print(printNumFive(5))