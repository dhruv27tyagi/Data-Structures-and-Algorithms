def count_digits(n):
    if(n>=1 and n<=9 ):
        return 1
    if (n==0):
        return 1
    
    smallNumber = int(n/10)
    smallAnswer = count_digits(smallNumber)

    ans = 1 + smallAnswer

    return ans

print(count_digits(4387))