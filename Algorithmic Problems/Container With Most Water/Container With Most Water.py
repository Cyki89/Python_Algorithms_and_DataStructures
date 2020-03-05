## my first solution correct???
'''
def maxWaterContainer(data):
    max_volume = 0
    max_high = 0
    max_high_index = 0
    i = 0
    for j in range(len(data)):

        if (j-i)*min(data[j],data[i]) > max_volume:
           max_volume = (j-i)*min(data[j],data[i])

        if (j-max_high_index)*min(data[j],max_high) > max_volume: 
           max_volume = (j-max_high_index)*min(data[j],max_high)
           i = max_high_index

        if data[j] > max_high:
            max_high = data[j]
            max_high_index = j
    
    return max_volume 
 
               
data = [10, 1, 30, 4, 5]
print(maxWaterContainer(data))
'''


## optimal solution
'''
def maxWaterContainer(data):
    max_volume = float('-inf')
    i = 0; j = len(data)-1
    while i < j:
        h_i = data[i]
        h_j = data[j]
        curr_volume = min(h_i, h_j)*(j-i)
        if  curr_volume > max_volume:
            max_volume = curr_volume
        if h_j > h_i:
            i += 1
        else:
            j -= 1
    return max_volume

               
data = [10, 1, 30, 4, 5]
print(maxWaterContainer(data))
'''
