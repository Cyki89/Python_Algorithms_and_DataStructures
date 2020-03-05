## O(nlogn) solution?
''' 
from random import random
from math import floor

def reorderArray(array):
    array_size = len(array)
    for i in range(array_size):
        rand_index = floor(random()*array_size)
        print(rand_index)
        array[i], array[rand_index] = array[rand_index], array[i]
    return array


array = [1, 0, 3, 9, 2]
print(reorderArray(array))
'''

## O(n) solution?


