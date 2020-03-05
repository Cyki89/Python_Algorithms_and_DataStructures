def BS_FirstGreater(arr, x):
    
    if len(arr) == 0:
        return 0
        
    l = 0; r = len(arr)-1
    
    while l <= r:
        s = (l+r)//2
        if arr[s] == x:
            break
        elif arr[s] > x:
            r = s - 1    
        else:
            l = s + 1
    
    index = s
    while index < len(arr) and arr[index] <= x :
        index += 1 
    return index
        
def calculateArraysSize(arrs, size):
    
    maxSize = size[0] = len(arrs[0]) 
    maxIndex = 0
    for i in range(1,len(arrs)):
        size[i] = len(arrs[i])
        if size[i] > maxSize:
           maxSize = size[i]
           maxIndex = i
    if maxIndex != 0:
        arrs[maxIndex], arrs[0] = arrs[0], arrs[maxIndex]
        size[maxIndex], size[0] = size[0], size[maxIndex]

    
def findKElement(arrs, k):
    
    arrs_size = len(arrs)
    size = [0 for i in range(arrs_size)]
    calculateArraysSize(arrs, size)
    
    if sum(size) < k:
        return False
        
    index = [0 for i in range(arrs_size)]
    index[0] = size[0]//2
    x = arrs[0][index[0]]                    
    L = index[0]+1 
    for i in range(1,arrs_size):
        index[i] = BS_FirstGreater(arrs[i],x)
        L += index[i] 
    
    if L == k:
        return x
        
    elif k > L:
        k -= L
        arrs[0] = arrs[0][index[0]+1:]
        for i in range(1,arrs_size):
            arrs[i] = arrs[i][index[i]:]
        return findKElement(arrs, k)
        
    else:
        for i in range(arrs_size):
            arrs[i] = arrs[i][:index[i]]
        return findKElement(arrs, k)


arrs = [[3,3], [3,4]]
print(findKElement(arrs, 3))
