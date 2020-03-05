# Brute force solution recursive
'''
def findMaxSum(matrix):
    if matrix == None:
        return None
    
    maxSum = float('-inf')
    rows = len(matrix)
    cols = len(matrix[0])
    tL = [0,0] # topleft corner of rectangle
    bR = [0,0] # bottomRight corner of rectangle
    return _findMaxSum(tL, bR, rows, cols, matrix, maxSum)

    
def _findMaxSum(tL, bR, rows, cols, matrix, maxSum):
    
    if tL[0] == rows: # topleft at the end - stop calling
        return maxSum 
    
    if tL[1] == cols: # move topleft one row down
        tL[0] +=1
        tL[1] = 0 
        bR = tL
        return _findMaxSum(tL, bR, rows, cols, matrix, maxSum)    
    
    if bR[0] == rows: # bottomRight corner at end - move topleft right
        tL[1] += 1
        bR = tL
        return _findMaxSum(tL, bR, rows, cols, matrix, maxSum)    
    
    if bR[1] == cols: # bottomRight corner at end of column - move bottomRight one row down 
        bR[0] += 1
        bR[1] = tL[1]
        return _findMaxSum(tL, bR, rows, cols, matrix, maxSum)    
    
    curr_sum = 0
    
    for i in range(tL[0],bR[0]+1):
        for j in range(tL[1],bR[1]+1):
            curr_sum += matrix[i][j]
    
    if curr_sum > maxSum:
        maxSum = curr_sum
    
    bR[1] += 1
    return _findMaxSum(tL, bR, rows, cols, matrix, maxSum)


matrix = [[1,4], [3,4]]
print(findMaxSum(matrix))
'''

# Brute force iterative
'''
def findMaxSum(matrix):
    
    if matrix == None:
        return None

    rows = len(matrix)
    cols = len(matrix[0])
    x_tL = 0 ; y_tL = 0 # cordinate of topLeft corner 
    x_bR = 0 ; y_bR = 0 # cordinate of bottomRight corner
    maxSum = float('-inf')
    currSum = 0
    
    for x_tL in range(0, rows):
        for y_tL in range(0, cols):
            currSum = 0
            for x_bR in range(x_tL, rows):
                for y_bR in range(y_tL, cols):        
                    currSum += matrix[x_bR][y_bR]
                    if currSum > maxSum:
                        maxSum = currSum    
    return maxSum

    
matrix = [[1,4]]
print(findMaxSum(matrix))
'''
