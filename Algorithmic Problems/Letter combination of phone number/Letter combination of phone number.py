## Optiimal approach
'''
def letterCombination(Input):
    
    my_dict = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','t'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
          }
    
    result = []
    
    helper(Input, '', result, 0, my_dict)         
    
    return result

            
def helper(Input, combination, result, index, my_dict):
    
    if  len(combination) == len(Input):
        result.append(combination)
        return
    
    letters = my_dict[Input[index]]
    
    for i in range(len(letters)):
        helper(Input, combination + letters[i], result, index + 1, my_dict)


Input = "232"

print(letterCombination(Input))
'''

## Optiimal approach II (with 2 for loop)
'''
def letterCombination(Input):
    
    my_dict = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','t'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
          }
    
    result = []
    
    helper(Input, '', result, 0, my_dict)         
    
    return result

            
def helper(Input, combination, result, index, my_dict):
    
    if  len(combination) == len(Input):
        result.append(combination)
        return
    
    for letters in my_dict[Input[index]]:    
        for letter in letters:
            helper(Input, combination + letter, result, index + 1, my_dict)


Input = "23"

print(letterCombination(Input))
'''

## Optiimal approach III (with 2 for loop without creating copy of string)
'''
def letterCombination(Input):
    
    my_dict = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','t'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
          }
    
    result = []
    
    helper(Input, '', result, 0, my_dict)         
    
    return result

            
def helper(Input, combination, result, index, my_dict):
    
    if  len(combination) == len(Input):
        result.append(combination)
        return
    
    for letters in my_dict[Input[index]]:    
        for letter in letters:
            combination += letter
            helper(Input, combination, result, index + 1, my_dict)
            combination = combination[:-1] 

Input = "23"

print(letterCombination(Input))
'''

## Optiimal approach IV (Iterative with cartesian product)
'''
def letterCombination(Input):
    
    my_dict = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','t'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
          }
    
    result = ['']
    
    for number in Input: 
        new_result = []
        for letter in my_dict[number]:            
            for element in result:
                new_result.append(element+letter)
        new_result, result = result, new_result
        
    return result
           

Input = "23"

print(letterCombination(Input))
'''

