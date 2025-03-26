def factorial(num):
    if num == 1:
        return 1
    
    ans = num*factorial(num-1)

    return ans


print(factorial(5))