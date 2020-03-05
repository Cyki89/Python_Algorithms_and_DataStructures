##  My first try
''' 
def num_ways(N,steps):
    if N < min(steps):
        return 0
    result = helper(N,steps)
    return result


def helper(N, steps):
    if N == 0:
        return 1
    f_step = True ## First step
    for step in steps:
        if step <= N:
            if f_step:
                result = helper(N-step, steps)
                f_step = False
            else:
                result += helper(N-step, steps)
    return result


print(num_ways(5,[1,3,5]))
'''

## Good !!! Corected my first try
''' 
def num_ways(N,steps):
    if N == 0:
        return 1
    if N < min(steps):
        return 0
    result = helper(N,steps)
    return result


def helper(N, steps):
    if N == 0:
        return 1
    result = 0
    for step in steps:
        if step <= N:
                result += helper(N-step, steps)
    return result


print(num_ways(1,[2,3,5]))
'''

## Good rec with memo
''' 
def main_num_ways(n,steps):
        ways = [None for i in range(n+1)]
        ways[0] = 1
        return num_ways(n, ways, steps)

def num_ways(n, ways, steps):
    if ways[n] != None:
        return ways[n]
    for i in range(1,n+1):
        total = 0
        for step in steps:
            if step <= i:
                    total += num_ways(i-step, ways, steps)
        ways[i] = total
    return ways[n]


print(main_num_ways(2,[1,3,5]))
'''

## Good rec with memo with showing ways
'''
def main_num_ways(n,steps):
        ways = [[] for i in range(n+1)]
        ways[0] += '0' 
        return num_ways(n, ways, steps)

def num_ways(n, ways, steps):
    if ways[n] != []:
        return ways[n]
    for i in range(1,n+1):
        for step in steps:
            if step <= i:
                    current_ways = num_ways(i-step, ways, steps)
                    for way in current_ways:
                        new_way = way + str(i)
                        ways[i].append(new_way) 
    return ways[n]


print(main_num_ways(5,[1,3,5]))
'''


## Good bottom_up
'''   
def num_ways(n, steps):
    if n == 0:
        return 1
    ways = [None for i in range(n+1)]
    ways[0] = 1    
    for i in range(1,n+1):
        total = 0
        for step in steps:
            if step <= i:
                    total += ways[i-step]
        ways[i] = total
    return ways[n]


print(num_ways(5,[1,3,5]))
'''

## Good bottom_up with showing ways
'''
def num_ways(n, steps):
    if n == ['0']:
        return '0'
    ways = [[] for i in range(n+1)]
    ways[0] += '0'   
    for i in range(1,n+1):        
        for step in steps:
            if step <= i:
                for way in ways[i-step]:
                    new_way = way + str(i)
                    ways[i].append(new_way)        
    return ways[n]


print(num_ways(5,[1,3,5]))
'''
