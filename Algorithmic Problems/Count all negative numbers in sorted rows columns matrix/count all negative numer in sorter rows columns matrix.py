## My first approach (Counting negative numbers in each row) ##
'''
from math import ceil

def find_last_negative_number(data, begin, end):
    
    if data[begin] > 0: 
        return None
        
    if data[end] < 0: 
        return end
    
    t_begin = begin
    t_end = end
    while (data[t_end] >= 0):
        s = ceil((t_begin + t_end)/2)
        if data[s] >= 0:
            t_end = s-1 
        else:    
            t_begin = s
    return t_end


def count_negative_numbers(data):
    count = 0
    end = len(data[0])-1
    for row in data:
        try:
            end = find_last_negative_number(row, 0, end)
            count += end + 1
        except:
            return count


data =[[-3, -2, -1, 1],
       [-2, -2, -3, 4],
       [ 4,  5,  7, 8]]
       
print(count_negative_numbers(data))
'''


## Most efficent appraoch (Counting negative numbers in row and column) ##
''' 
from math import ceil

def find_last_negative_number(data, begin, end):
    
    if data[begin] > 0: 
        return None
        
    if data[end] < 0: 
        return end
    
    t_begin = begin
    t_end = end
    while (data[t_end] >= 0):
        s = ceil((t_begin + t_end)/2)
        if data[s] >= 0:
            t_end = s-1 
        else:    
            t_begin = s
    return t_end


def count_negative_numbers(data):
    
    end_col = find_last_negative_number(data[0], 0, len(data[0])-1) ## idex of last negative number in first row
    end_row = find_last_negative_number([x[0] for x in data], 0, len(data)-1) ## index of last negative number in first column
    
    try: 
        t_data = [[x[i] for x in data[:end_row+1]] for i in range(end_col+1)] ## transposit data in range of occuring negative number
    except:
        return 0
        
    count = 0
    for i in range(0, end_col+1):
       end_row = find_last_negative_number(t_data[i], 0, end_row) 
       count += end_row+1 
    return count


data =[[-1, -2, -3, 4],
       [-1, -2, -3, 5],
       [ 4,  5,  7, 8]]
       
print(count_negative_numbers(data))
'''
