## Head Recursion 
def isSorted(arr):

    length = len(arr)
    if length == 0 or length==1:
        return True
    
    ans = isSorted(arr[1:])

    if arr[0] < arr[1]:
        return ans
    else:
        return False

arr = [2,3,4,5,7,8]




## Tail Recursion 

def isSorted2(arr):
    length = len(arr)
    if length == 0 or length==1:
        return True

    if arr[0] >= arr[1]:
        return False
    
    return isSorted2(arr[1:])

print(isSorted2(arr)) 