def removeDuplicate(arr):
    
    i = 0
    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
           i += 1 
           arr[i] = arr[j] 
    arr = arr[:i+1]
    return arr
            
        
arr = []
arr = removeDuplicate(arr)
print(arr)
print(len(arr))
