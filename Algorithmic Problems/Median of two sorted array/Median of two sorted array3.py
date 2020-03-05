# O(log(n+m))
from math import ceil
def medianOfTwoArray(arr1, arr2):    
    
    if arr1 == [] and arr2 ==[]:
        return False      

    total = len(arr1) + len(arr2)

    if total % 2 == 1:
        return findKthElement(arr1, 0, arr2, 0, total//2)
    else:
        return (findKthElement(arr1, 0, arr2, 0, total//2-1) +
                findKthElement(arr1, 0, arr2, 0, total//2))/2

def findKthElement(arr1, s1, arr2, s2, k):

    if k == 0:
        return min(arr1[s1], arr2[s2])

    if s1 >= len(arr1):
        return arr2[s2+k]

    if s2 >= len(arr2):
        return arr1[s1+k]

    i1 = s1 + k//2
    i2 = s2 + k//2
    v1 = arr1[i1] if i1 < len(arr1) else float('inf')
    v2 = arr2[i2] if i2 < len(arr2) else float('inf')

    if v1 < v2:
        return findKthElement(arr1, s1+k//2, arr2, s2, k-ceil(k/2))
    else:
        return findKthElement(arr1, s1, arr2, s2+k//2, k-ceil(k/2))

arr1= [1,2]
arr2= [2]
print(medianOfTwoArray(arr1, arr2))



