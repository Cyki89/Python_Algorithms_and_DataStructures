def kadane(arr):
    
    if arr == None or len(arr) == 0:
        return None
    
    maxSum = arr[0]
    currSum = 0
    startCurrSum = startMaxSum = endMaxSum = 0
    
    for i in range(len(arr)):
        
        currSum += arr[i]
        
        if currSum > maxSum:
            maxSum = currSum
            startMaxSum = startCurrSum
            endMaxSum = i
        
        if currSum < 0:
            currSum = 0 
            startCurrSum = i+1
    
    return (maxSum, startMaxSum, endMaxSum)
    
def findMaxSum(matrix):
    
    if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    
    maxSum = float('-inf')
    maxTop = maxBottom = maxLeft = maxRight = 0
    
    for L in range(len(matrix[0])): ## iterate over colum
        arrKadane = [0 for i in range(len(matrix))] ## for each row
        for R in range(L,len(matrix[0])):
            for i in range(len(matrix)):
                arrKadane[i] += matrix[i][R]
                currSum, startCurrSum, endCurrSum = kadane(arrKadane)
                if currSum > maxSum:
                    maxSum = currSum
                    maxTop = startCurrSum
                    maxBottom = endCurrSum
                    maxLeft = L 
                    maxRight = R   
    
    result=[]
    
    for i in range(maxTop, maxBottom+1):
        row = []
        for j in range(maxLeft, maxRight+1):    
            row.append(matrix[i][j])
        result.append(row)
    
    print (result)    
    
    return maxSum

    
matrix = [[-2, 4,-1, 6], ## ans is 20
          [ 1, 4, 5,-1],   
          [-1,-1,-1,-1], 
          [ 2, 3,-2, 5]]
print(findMaxSum(matrix))

