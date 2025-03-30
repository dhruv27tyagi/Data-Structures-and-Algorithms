"""
Given an array and an element, find 
a. first index of element
b. last index of element
c. return -1 if element not in list
"""

def find_first_index(arr, element):
    if len(arr) == 0:
        return -1
    
    if(arr[0]==element):
        return 0
    
    ansfromrecursion =  find_first_index(arr[1:],element) + 1
    if ansfromrecursion == -1:
        return ansfromrecursion
    else:
        return ansfromrecursion + 1


arr = [3,2,1,7,5,7,8]       
print(find_first_index(arr,5))


    
