## Iterating each index in data ##
'''
def firstRecuringCharacter(data):
    results_dict = {}
    min_index = len(data)
    for i in range(len(data)): 
        try:
            if results_dict[data[i]] < min_index:
               min_index = results_dict[data[i]]
        except:
            results_dict[data[i]] = i
    try:
        return data[min_index]     
    except:
        return None

            
data = "BECSDESQASDASDCXZCASDIOQWSADCXZHASJDASOP"
print(firstRecuringCharacter(data))
'''

## Dummy approach ##
'''
from random import randint

def firstRecuringCharacter(data):
    for i in range(len(data)):
        if data[i] in data[:i]:
            return data[i]
    return None


data =''.join([chr(randint(97,122)) for i in range(randint(1,20))])
print(data)
print(firstRecuringCharacter(data))
'''
