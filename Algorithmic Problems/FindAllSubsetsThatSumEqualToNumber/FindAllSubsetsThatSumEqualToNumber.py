## recursive approach iterate reverse solution 1 ##
'''
def find_all_subsets(data, target):
    data.sort()
    return rec(data, target, len(data)-1)
    
def rec(data, total, i):
    if total == 0:
        return 1
    elif i < 0:
        return 0
    else:
        if total < data[i]:
           return rec(data, total, i-1)
        else:
            return rec(data, total-data[i], i-1) + rec(data, total, i-1)
       

data = [2, 4, 6, 10, 16]
target = 16
print(find_all_subsets(data, target))
'''

## recursive approach iterate reverse solution 2 ##
'''
def find_all_subsets(data, target):
    data.sort()
    return rec(data, target, len(data)-1)
    
def rec(data, total, i):
    if total == 0:
        return 1
    if total < 0:
        return 0    
    elif i < 0:
        return 0
    else:
        return rec(data, total-data[i], i-1) + rec(data, total, i-1)
       

data = [2, 4, 6, 10, 16]
target = 16
print(find_all_subsets(data, target))
'''

## recursive approach iterate positive with memo ##
'''
def find_all_subsets(data, target):
    data.sort()
    memo = {}
    return rec(data, target, 0, memo)
    
def rec(data, total, i, memo):
    if total == 0:
        return 1
    if total < 0:
        return 0    
    elif i == len(data):
        return 0
    else:
        if (total, i) in memo.keys():
            return memo[(total, i)]
        memo[(total, i)] = rec(data, total-data[i], i+1, memo) + rec(data, total, i+1, memo)
        return memo[(total, i)]

data = [2, 4, 6, 10, 16]
target = 16
print(find_all_subsets(data, target))

'''

## recursive approach iterate positive ##
'''
def find_all_subsets(data, target):
    data.sort()
    return rec(data, target, 0)
    
def rec(data, total, i):
    if total == 0:
        return 1
    if total < 0:
        return 0    
    elif i == len(data):
        return 0
    else:
        return rec(data, total-data[i], i+1) + rec(data, total, i+1)
       

data = [2, 4, 6, 10, 16]
target = 16
print(find_all_subsets(data, target))
'''


