## Dp solution
'''
def coinChange(N, S):
    
    Dp = [[0 for i in range(N+1)] for j in range(len(S)+1)]
        
    for i in range(len(S)+1):
        Dp[i][0] = 1

    for i in range(1, len(S)+1):
        for j in range(1, N+1):
            if S[i-1] > j:
                Dp[i][j] = Dp[i-1][j]
            else:
                Dp[i][j] = Dp[i-1][j] + Dp[i][j-S[i-1]]
    print(Dp)
    return Dp[len(S)][N]
    
    
N = 4
S = [1,2,3]
print(coinChange(N, S))
'''

## Dp solution with returning solutions
'''
def coinChange(N, S):   

    Dp = [[[] for i in range(N+1)] for j in range(len(S))] ## result table

    for i in range(len(S)):
        for j in range(N+1):
            if i != 0:                  ## no previous solutions
                Dp[i][j] = Dp[i-1][j].copy()
            if S[i] == j:
                Dp[i][j].append([S[i]]) ## append list with one element of curent coin
            elif S[i] < j:   
                for x in Dp[i][j-S[i]]: ## to each solution of current value subtract curent coin append curent coin (if no solution append nothing)
                    Dp[i][j].append(x+[S[i]])
    return Dp[len(S)-1][N]
    
    
N = 4
S = [1,2,3]
print(coinChange(N, S))
'''

## Recusrive solution with for loop
'''
def coinChange(target, coins, index):
  
    if target == 0:
        return 1 
    
    ways = 0
    for i in range(index, len(coins)):
        if coins[i] > target:
            break
        ways += coinChange(target-coins[i], coins, i)
    return ways   
   

target = 4
coins = [1,2,3]
print(coinChange(target, coins, 0))
'''

## Recusrive solution with for loop and returning solutions
'''
def coinChange(target, coins, index, cur, result):
  
    if target == 0:
       result.append(cur)

    else:
        for i in range(index, len(coins)):
            if coins[i] > target:
                break
            coinChange(target-coins[i], coins, i, cur + [coins[i]], result)
        return result
   

target = 4
coins = [1,2,3]
print(coinChange(target, coins, 0, [], []))
'''

## Recusrive solution with while loop
'''
def coinChange(target, coins, index):
    
    if target == 0:
        return 1

    ways = 0
    i = index

    while i < len(coins) and coins[i] <= target:
        ways += coinChange(target-coins[i], coins, i)
        i += 1

    return ways   
   

target = 4
coins = [1,2,3]
print(coinChange(target, coins, 0))
'''

#Iterative solution with printing
'''
def coinChange(target, coins):
    
    result = []
    cur = []
    
    for coin in coins:
        if coin < target:
            cur.append([coin])
        elif coin == target:
            result.append([coin])   
    
    while cur:
        new = []
        for x in cur:
            for coin in coins:
                if coin >= x[-1]:
                    if sum(x) + coin < target:
                        new.append(x +[coin])
                    elif sum(x) + coin == target:
                        result.append(x +[coin])
        cur = new    
    return result
    
N = 4
S = [3,2,1,4,5]
print(coinChange(N, S))
'''
