from MaxHeap import *

points=[2, 22, 33, 20, 54, 1, 6, 8, 9, 10, 22, 3]
n = 2

myHeap=MaxHeap(points[0:n])

for point in points[n:]:
    if point < myHeap.peak():
       myHeap.pop()
       myHeap.push(point)
print(myHeap)  
     
 
