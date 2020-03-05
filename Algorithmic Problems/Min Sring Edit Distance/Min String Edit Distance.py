## Recursive approach
'''
def editDistDP(str1, str2):
    minDist = 0
    return _editDistDP(str1, str2, minDist)


def _editDistDP(str1, str2, minDist):
    
    if str1 == str2:
        return minDist
    
    if str1 and str2 and str1[-1] == str2[-1]:
        return _editDistDP(str1[:-1], str2[:-1], minDist)
    
    else:
        R = _editDistDP(str1[:-1], str2[:-1], minDist+1) if str1 and str2 else float('inf')
        I = _editDistDP(str1, str2[:-1], minDist+1) if str2 else float('inf')
        D = _editDistDP(str1[:-1], str2, minDist+1) if str1 else float('inf')
        minDist = min(R, I, D)
        
        return minDist
   

str1 = "saturday"
str2 = "sunday"
print('Min Edit Distane:' ,editDistDP(str1, str2))
'''

## Dp approach with printing
'''
def editDistDP (str1, str2):
    
    Dp = [[None for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    
    for i in range(len(str2)+1): ## fill first row
        Dp[0][i] = i
    
    for i in range(len(str1)+1): ## fill first column
        Dp[i][0] = i

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                Dp[i+1][j+1] = Dp[i][j]
            else:
                Dp[i+1][j+1] = 1 + min(Dp[i][j], Dp[i][j+1], Dp[i+1][j])
    return Dp[len(str1)][len(str2)]


str1 = "sunday"
str2 = "saturday"
print(editDistDP(str1, str2))
'''

## Dp approach with printing
'''
def editDistDP (str1, str2):
    
    str1 = ' ' + str1
    str2 = ' ' + str2
    
    Dp = [[None for i in range(len(str1))] for j in range(len(str2))]
    
    for i in range(len(str1)): ## fill first row
        Dp[0][i] = i
    
    for i in range(len(str2)): ## fill first column
        Dp[i][0] = i

    for i in range(1,len(str2)):
        for j in range(1,len(str1)):
            if str2[i] == str1[j]:
                Dp[i][j] = Dp[i-1][j-1]
            else:
                Dp[i][j] = 1 + min(Dp[i-1][j-1], Dp[i-1][j], Dp[i][j-1])

    i = len(Dp) - 1
    j = len(Dp[0]) - 1
    lst = []
    
    while i>=0 and j>=0:
        if str2[i] != str1[j]:
            if j and Dp[i][j] == Dp[i][j-1] + 1:
                lst.append('delete: {}'.format(str1[j]))
                j -=1
            elif i and Dp[i][j] == Dp[i-1][j] + 1:
                lst.append('add: {}'.format(str2[i]))
                i -=1    
            else:
                lst.append('replace: {} -> {}'.format(str1[j],str2[i]))
                i -= 1
                j -= 1   
        else:
            i -= 1
            j -= 1
            
    for i, x in enumerate(lst[::-1],1):
        print(i,x)
    print('')
    
    return Dp[len(str2)-1][len(str1)-1]


str1 = "sunday"
str2 = "saturday"
print('Min Edit Distane:' ,editDistDP(str1, str2))
'''
