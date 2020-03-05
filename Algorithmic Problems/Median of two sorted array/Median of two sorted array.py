# O(log(min(n,m))
def medianOfTwoArray(arr1, arr2):    
    
    if arr1 == [] and arr2 ==[]:
        return False      

    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1    

    s1 = len(arr1)
    s2 = len(arr2)
    
    s = 0
    e = s1         
    
    while True:

        p1 = (s+e)//2
        p2 = (s1+s2+1)//2 - p1
        
        l1 = arr1[p1-1] if p1 != 0 else float('-inf') 
        r1 = arr1[p1] if p1 != s1 else  float('inf')
        l2 = arr2[p2-1] if p2 != 0 else float('-inf') 
        r2 = arr2[p2] if p2 != s2 else float('inf')

        if l1 <= r2 and l2 <= r1:
            if (s1+s2)%2 == 0:
                return (max(l1,l2) + min(r1,r2))/2
            else:
                return max(l1,l2)            
        elif l1 > r2:
             e = p1-1
        else:
             s = p1+1


arr1= [1,5]
arr2= []
print(medianOfTwoArray(arr1, arr2))



