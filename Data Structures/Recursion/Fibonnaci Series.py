def fib(n):
   
    if n ==0 :
        return -1
    if n ==1:
        return 0
    last = fib(n-1)
    secondlast = fib(n-2)
    ans = abs(last + secondlast)
    return ans

print(fib(7 ))