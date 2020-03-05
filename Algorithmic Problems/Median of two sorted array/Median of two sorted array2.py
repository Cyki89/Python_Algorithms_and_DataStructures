# O(log(n+m))
def medianOfTwoArray(arr1, arr2):    
    
    if arr1 == [] and arr2 ==[]:
        return False      

    total = len(arr1) + len(arr2)

    if total % 2 == 1:
        return findKthElement(arr1, 0, arr2, 0, total//2+1)
    else:
        return (findKthElement(arr1, 0, arr2, 0, total//2) +
                findKthElement(arr1, 0, arr2, 0, total//2+1))/2

def findKthElement(arr1, s1, arr2, s2, k):

    if k == 1:
        return min(arr1[s1], arr2[s2])

    if s1 >= len(arr1):
        return arr2[s2+k-1]

    if s2 >= len(arr2):
        return arr1[s1+k-1]

    i1 = s1 + k//2 -1
    i2 = s2 + k//2 -1
    v1 = arr1[i1] if i1 < len(arr1) else float('inf')
    v2 = arr2[i2] if i2 < len(arr2) else float('inf')

    if v1 < v2:
        return findKthElement(arr1, s1+k//2, arr2, s2, k-k//2)
    else:
        return findKthElement(arr1, s1, arr2, s2+k//2, k-k//2)

arr1= [1,2,4,5,6]
arr2= [2,3,7,8,9,10]
print(medianOfTwoArray(arr1, arr2))



