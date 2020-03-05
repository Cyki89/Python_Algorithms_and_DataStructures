## Recursive solution with rev_sort outside function
'''
def is_hoppable(data):
    if data == []:
            return True
    for x in enumerate(data,1):
        if x[0] <= x[1]:
            if is_hoppable(data[x[0]:]):
                return True
    return False
            

data = [4,2,0,0,2,0]
data = data[::-1]
print(is_hoppable(data))
'''

## Recursive solution with 2 fuctions (main function only to rev_sort data)
'''
def is_hoppable(data):
    data = data[::-1]
    if helper(data):
        return True
    return False     


def helper(data):
    if data == []:
            return True
    for x in enumerate(data,1):
        if x[0] <= x[1]:
            if helper(data[x[0]:]):
                return True
    return False            

data = [4,2,0,0,2,0]
print(is_hoppable(data))
'''

## Dynamic programing solution
'''
def is_hoppable(data):
    max_range = [0 for i in range(len(data))]
    for i in range(len(max_range)):
        if max_range[i-1] < i: ## for i = 0 I used property of list in python compare max_range[-1] < i (0 < 0)
            return False        
        elif max_range[i-1] < data[i] + i:
            max_range[i] = data[i] + i
        else:
            max_range[i] = max_range[i-1]
    if max_range[i] > i: ## the same as max_range[len(max_range)-1] > len(max_range)-1
        return True
    else:
        return False             
                 
    
data = [4,2,0,0,2,0]
print(is_hoppable(data))
'''
