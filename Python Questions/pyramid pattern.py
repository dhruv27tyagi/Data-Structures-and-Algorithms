def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """

    pattern_list = []
    for i in range(1,n+1):
        if i == 1:
            pattern_list.append((n-i)*' '+i * '*'+ (n-i)*' ')
        else:
            pattern_list.append((n-i)*' '+i * '*' + (i-1)*'*'+(n-i)*' ')

    return pattern_list

print(generate_pyramid(5))