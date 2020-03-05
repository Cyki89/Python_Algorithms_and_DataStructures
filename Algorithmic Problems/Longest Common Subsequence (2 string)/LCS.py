## Recursive solution
'''
def LCS(str1, str2):
    if not str1 or not str2:
        return 0
    if str1[0] == str2[0]:
       return 1 + LCS(str1[1:],str2[1:])
    else:
       return max(LCS(str1[1:],str2),LCS(str1,str2[1:]))
    
print(LCS('AACAD','AACEFD'))
'''

## Recursive solution with memo
'''
memo = {}
def LCS(str1, str2):
    if not str1 or not str2:
        return 0
    try:
        return memo[(str1, str2)]
    except:
        pass
    if str1[0] == str2[0]:
       memo[(str1, str2)] = 1 + LCS(str1[1:], str2[1:]) 
       return memo[(str1, str2)] 
    else:
       memo[(str1, str2)] = max(LCS(str1[1:], str2),LCS(str1, str2[1:]))
       return memo[(str1, str2)]

print(LCS('ACBDA','ABCCDCCDA'))
print(memo)
'''

## iterative solution
'''
def LCS(str1, str2):
    
    if not str1 or not str2:
        return 0
    
    str1 = ' ' + str1
    str2 = ' ' + str2
    
    result = [[0 for y in str2] for x in str1]
    
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                result[i][j] = 1 + result[i-1][j-1]
            else:
                result[i][j] = max(result[i-1][j],result[i][j-1])
    
    return result[-1][-1]  

print(LCS('ACBDA','ABCCDCCDA'))
'''

## iterative solution with printing
'''
def LCS(str1, str2):
    
    if not str1 or not str2:
        print('')
        return 0
    
    str1 = ' ' + str1
    str2 = ' ' + str2
    
    result = [[0 for y in str2] for x in str1]
    
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                result[i][j] = 1 + result[i-1][j-1]
            else:
                result[i][j] = max(result[i-1][j],result[i][j-1])
    
    str_result = ''
    i = len(str1) - 1
    j = len(str2) - 1
    
    while i and j:
       
        if result[i][j] > result[i-1][j] and result[i][j] > result[i][j-1]:
           str_result += str1[i]
           i += -1; j += -1  
           
        elif result[i][j-1] > result[i-1][j]:
           j += -1
           
        else:
           i += -1     
    
    print(str_result[::-1])
    return result[-1][-1]
    

print(LCS('GXTXAYB','AGGTAB'))
'''
