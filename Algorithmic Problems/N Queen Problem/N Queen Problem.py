## First approach 
'''
def nQueenSolution(n):
    
    result = []
    findSolution(0, n, [], result)
    print(len(result))
    return result


def findSolution(row, n, solution, result):
    
    if row == n:
       result.append(solution.copy())
       return
       
    for col in range(0,n):    
        if validateSolution(row,col, solution):
           solution.append((row,col))  
           findSolution(row+1, n, solution, result)
           solution.pop()    
    

def validateSolution(row, col, solution):

    for i,j in solution:
        if j == col or i + j == row + col or i - j == row - col:
            return False
    return True

    
n = 5
print(nQueenSolution(n))
'''



## Second approach
'''
def nQueenSolution(n):
    
    result = []
    chestBoard = [[0 for i in range(n)] for j in range(n)]
    dict_DP = {i:[] for i in range(n)} ## dict of disalbedPostions
    findSolution(0, n, chestBoard, dict_DP, [], result)
    print(len(result))
    return result


def findSolution(row, n, chestBoard, dict_DP, solution, result):
    
    if row == n:
       result.append(solution.copy())
       return
       
    for col in range(0,n):    
        if chestBoard[row][col] == 0:
            solution.append((row,col))
            disalbePostions(row, col, n, chestBoard, dict_DP)
            findSolution(row+1, n, chestBoard, dict_DP, solution, result)
            for x in dict_DP[row]:
                chestBoard[x[0]][x[1]] = 0    
            dict_DP[row] = []
            solution.pop()
            

def disalbePostions(row, col, n, chestBoard, dict_DP):
    
    d1 = row + col 
    d2 = row - col
    
    for i in range(row,n):
        if chestBoard[i][col] == 0:
            chestBoard[i][col] = -1
            dict_DP[row].append((i,col))
        if d1-i in range(0,n) and chestBoard[i][d1-i] == 0:
            chestBoard[i][d1-i] = -1
            dict_DP[row].append((i,d1-i))
        if i-d2 in range(0,n) and chestBoard[i][i-d2] == 0:
            chestBoard[i][i-d2] = -1
            dict_DP[row].append((i,i-d2))


n = 5
print(nQueenSolution(n))
'''

