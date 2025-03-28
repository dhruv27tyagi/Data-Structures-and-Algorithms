## head recursion 

def Sum(arr):
    if(len(arr)==0):
        return 0
    
    ans = arr[0] + Sum(arr[1:])
    return ans

arr = [2,2,2,2,2]

print(Sum(arr))
## Tail recursion 

def Sum_tail(arr, accumulator=0):
    if(len(arr==0)):
        return accumulator

    accumulator += arr[0]

    return Sum_tail(arr[1:],accumulator)