def FindKElement(arr1, arr2, k):
    
    while  k > 0 and len(arr1) + len(arr2) >= k:
        
        if len(arr1) == 0:
            return arr2[k-1]
        
        if len(arr2) == 0:
            return arr1[k-1]
        
        if k == 1:
            return min(arr1[0], arr2[0])
        
        p1 = min(k//2, len(arr1))
        p2 = min(k//2, len(arr2))
        
        if arr1[p1-1] > arr2[p2-1]:
            arr2 = arr2[p2:]
            k -= p2
            arr1 = arr1[:k]
        else:
            arr1 = arr1[p1:]
            k -= p1
            arr2 = arr2[:k]
    
    return False
    
        
arr1 = [1,4,8,10]
arr2 = [2,3,6,7,9]
k = 5
print(FindKElement(arr1, arr2, k))
