def Sum(num):
    if num == 0 :
        return 0
    
    ans = num + Sum(num-1)

    return ans

print(Sum(10))