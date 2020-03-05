# First approach (with no duplicate char in T)
'''
def findMinSubstring(S,T):
    
    hash_T = {char: None for char in T}
    result = ""
    
    if not S or not T:
        return ""
    
    S += T[0]   # to compare last curr with result
    
    for i, char in enumerate(S):
     
        if char in hash_T.keys():
            
            if not None in hash_T.values():
                
                curr = S[min(hash_T.values()) : max(hash_T.values()) + 1]
               
                if not result or len(curr) < len(result):
                    result = curr 
                
            hash_T[char] = i 
       
    return result


S = 'ADOBECODEBANC' 
T = 'ABC'

print(findMinSubstring(S,T))
'''


## Correct optimal solution
'''
def findMinSubstring(S,T):
    
    if not S or not T:
        return ""
    
    hash_T = {}
    result = ""
    left = 0
    count = 0 
    min_size = float('inf')
    
    for char in T:
        try:
            hash_T[char] +=1
        except:
            hash_T[char] = 1
    
    for right in range(len(S)):
        try:
            hash_T[S[right]] -= 1
            if hash_T[S[right]] >= 0:
                count += 1
        except:
            pass
        
        while count == len(T):
            if min_size > right - left + 1:
                min_size = right - left + 1
                result = S[left:right+1]
            try:
                hash_T[S[left]] += 1
                if hash_T[S[left]] > 0:
                    count -= 1
            except:
                pass
            left += 1    
       
    return result


S = 'AAAADOABECODEBANCADE' 
T = 'Z'

print(findMinSubstring(S,T))
'''
