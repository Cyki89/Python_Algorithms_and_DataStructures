## Dynamic solution
'''
def SupperEggDrop(eggs, floors):
    
    result = [[ y if x == 1 else 0 for y in range(floors+1)] for x in range(eggs+1)]
    print(result)
    for i in range(2, eggs+1):
        for j in range(1, floors+1):
            if i > j:   
                result[i][j] = result[i-1][j]
                continue
            minimun = result[1][j]
            for k in range(2, j+1):
                temp = 1 + max(result[i][j-k],result[i-1][k-1])    
                if temp < minimun:
                    minimun = temp
            result[i][j] = minimun
    return result[-1][-1]
            

eggs = 2
floors = 6

print(SupperEggDrop(eggs, floors))
'''

## Recursive solution

memo = {}

def SupperEggDrop(eggs, floors):
    
    if eggs == 0:  
        return 0
    
    if eggs == 1 or floors == 0 or floors == 1:
        memo[(eggs,floors)] = floors
        return floors
        
    try: 
        return memo[(eggs,floors)] 
    except: 
        pass
    
    min_try  = floors   
    
    for k in range(1, floors+1):
        temp  = 1 + max(SupperEggDrop(eggs, floors-k),SupperEggDrop(eggs-1, k-1))
        if min_try > temp:
           min_try = temp 
    memo[(eggs,floors)] = min_try
    return min_try       


eggs = 2
floors = 6

print(SupperEggDrop(eggs, floors))
print(sorted(memo))


