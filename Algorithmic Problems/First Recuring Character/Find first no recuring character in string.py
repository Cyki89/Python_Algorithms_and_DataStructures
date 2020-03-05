## Iterating each element in data ##
'''
def firstNoRecuringCharacter(data):
    results_dict = {}
    final_result = None
    for char in data[::-1]:
        try:
            results_dict[char] += 1
        except:
            results_dict[char] = 1
            final_result = char 
    return final_result       

           
data = "ABECSDESQASDASDCXZCASDIOQWSADCXZHASJDASOP"
print(firstNoRecuringCharacter(data))
'''

## Iterating each index in data ##
'''
def firstNoRecuringCharacter(data):
    results_dict = {}
    final_result = None
    for i in range(len(data)-1, -1, -1): ## reverse iteration
        try:
            results_dict[data[i]] += 1
        except:
            results_dict[data[i]] = 1
            final_result = data[i] 
    return final_result       

            
data = "ABECSDESQASDASDCXZCASDIOQWSADCXZHASJDASOP"
print(firstNoRecuringCharacter(data))
'''
