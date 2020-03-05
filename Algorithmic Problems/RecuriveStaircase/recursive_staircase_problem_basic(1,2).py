## My first try
'''
def num_ways(N):
    if N == 0:
        return 0

    memo=[None for i in range(N+1)]

    result = helper(N, memo)
    return result


def helper(N, memo):
    if N == 0:
        return 1

    if memo[N] != None:
        return memo[N]
    
    result = helper(N-1, memo)
    if N >=2:
        result += helper(N-2, memo)
    memo[N] = result
    return result       


print(num_ways(4))
'''

## Good iterative
''' 
def num_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        ways = [None for i in range(n+1)]
        ways[0] = 1
        ways[1] = 1
        for i in range(2,n+1):
            ways[i] = ways[i-1] + ways[i-2] 
        return ways[n]


print(num_ways(4))
'''

## Good simple recursive
'''
def num_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return num_ways(n-1) + num_ways(n-2)


print(num_ways(4))    
'''

## Good recursive with memo
''' 
def main_num_ways(n):
    if n == 0 or n == 1:
       return 1
    else:
        ways = [None for i in range(n+1)]
        ways[0] = 1
        ways[1] = 1 
        return num_ways(n,ways)
        
def num_ways(n,ways):
    if ways[n] != None:
       return ways[n] 
    else:
        ways[n]=num_ways(n-1,ways) + num_ways(n-2,ways)
    return ways[n]


print(main_num_ways(10))  
'''
