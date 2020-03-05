# Kadan'e algorithm witht three args
'''
def kadane(arr, startMaxSum, endMaxSum):
    
    if arr == None or len(arr) == 0:
        return None
    
    maxSum = arr[0]
    currSum = 0
    startCurrSum = 0
    
    for i in range(len(arr)):
        
        currSum += arr[i]
        
        if currSum > maxSum:
            maxSum = currSum
            startMaxSum = startCurrSum
            endMaxSum = i
        
        if currSum < 0:
            currSum = 0 
            startCurrSum = i+1
    
    return maxSum
    
    
arr = [-2, -3, 4, -1, -2, 1, 5, -3] 
print(kadane(arr, 0, len(arr)-1))
'''


# Kadan'e algorithm witht one arg
'''
def kadane(arr):
    
    if arr == None or len(arr) == 0:
        return None
    
    maxSum = arr[0]
    currSum = 0
    startMaxSum = endMaxSum = startCurrSum = 0
    
    for i in range(len(arr)):
        
        currSum += arr[i]
        
        if currSum > maxSum:
            maxSum = currSum
            startMaxSum = startCurrSum
            endMaxSum = i
        
        if currSum < 0:
            currSum = 0 
            startCurrSum = i+1
    
    return maxSum
    
    
arr = [-2, -3, 4, -1, -2, 1, 5, -3] 
print(kadane(arr))
'''
