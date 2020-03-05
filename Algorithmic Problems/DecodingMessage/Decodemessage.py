## First approach return list of all posible message
'''
def decode_message(user_message):
    result = []
    decode_part(user_message, result, [], 0)
    return result

    
def decode_part(user_message, result, part, start):

    if start == len(user_message):        
       result.append(''.join(part))

    else:
            i = start

            part_copy = part.copy()
            part_copy.append(chr(int(user_message[i])+96))
            decode_part(user_message, result, part_copy, i+1)

            if i < len(user_message)-1 and int(user_message[i:i+2])+96 <= 122:
                part2_copy = part.copy()
                part2_copy.append(chr(int(user_message[i:i+2])+96))
                decode_part(user_message, result, part2_copy, i+2)
                    

print(decode_message('5512'))
'''

## Recursive solution counting all posible message
'''
def num_ways(data):
    return helper(data, len(data))
    
def helper(data,k):
    if k == 0:
        return 1
    
    s = len(data)-k
    if data[s] == '0':
        return 0
    
    result = helper(data, k-1)
    if k >=2 and int(data[s:s+2]) <= 26:
        result += helper(data, k-2)
    return result
    
print(num_ways('1012'))
'''

## Recursive solution counting all posible message with memo
''''
def num_ways(data):
    memo=[None for i in range(len(data)+1)]
    return helper(data, len(data), memo)
    
def helper(data, k, memo):
    if k == 0:
        return 1
    
    s = len(data)-k
    if data[s] == '0':
        return 0
    
    if memo[k] != None:
        return memo[k]
        
    result = helper(data, k-1, memo)
    if k >=2 and int(data[s:s+2]) <= 26:
        result += helper(data, k-2, memo)
    memo[k]=result
    return result
    
print(num_ways('11'))
'''
            

    

