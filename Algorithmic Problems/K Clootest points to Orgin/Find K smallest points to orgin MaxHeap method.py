from MaxHeapForPoints import *

points=[(-2,4), (0,-2), (-1,0), (3,5), (-2,-3), (3,2), (9,2), (5,5), (0,0)]
n = 3

myHeap=MaxHeap(points[0:n])

for point in points[n:]:
    magnitude = point[0]**2 + point[1]**2
    if magnitude < myHeap.peak():
       myHeap.pop()
       myHeap.push(point, magnitude)
print(myHeap)  
     
 
