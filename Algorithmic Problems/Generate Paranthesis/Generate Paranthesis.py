#Recursive solution 1
'''
def generateParentheses(l, r, cur, result):
    print(l, r, cur, result)
    if r == 0:
        result.append(cur)
    else:
        if l > 0:
            generateParentheses(l-1, r, cur+'(', result)
        if r > l:
            generateParentheses(l, r-1, cur+')', result)
    return result

n = 3
l = r = n
print(generateParentheses(l, r, '', []))
'''

#Recursive solution 2
'''
def generateParentheses(n):
    return _generateParentheses(n, n, '')

def _generateParentheses(l, r, cur):
    if l == 0:
        return [cur+')'*r]
    if r > l:
        return _generateParentheses(l-1, r, cur+'(') + _generateParentheses(l, r-1, cur+')')               
    else:
        return _generateParentheses(l-1, r, cur+'(')
    
n = 4
print(generateParentheses(n))
'''
#Recursive solution 3
'''
def generateParentheses(n):
    return _generateParentheses(n, n, '')

def _generateParentheses(l, r, cur):
    if r == 0:
        return [cur]
    if r > l:
        if l>0:
            return _generateParentheses(l-1, r, cur+'(') + _generateParentheses(l, r-1, cur+')')
        else:
            return _generateParentheses(l, r-1, cur+')')
    else:
        return _generateParentheses(l-1, r, cur+'(')
    
n = 3
print(generateParentheses(n))
'''
