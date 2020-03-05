## First approach
'''
def LongestCommonPrefix(Input):
    if len(Input) == 0:
        return None
    i = len(Input[0]) - 1
    while i >= 0:
      prefix = Input[0][0:i+1]  
      for j in range(1,len(Input)):
        if prefix != Input[j][0:i+1]:
              break
      else:
        return prefix
      i -= 1
    return ''


Input = ['','']
print(LongestCommonPrefix(Input))

'''

## Optimal approach
'''
def LongestCommonPrefix(Input):
    LCP = Input[0]
    for i in range(1,len(Input)):
        for j in range(len(LCP)):
            if j >=len(Input[i]) or LCP[j] != Input[i][j]:
                LCP = LCP[0:j]
                break
        if LCP == '':
            return ''
    return LCP
   

Input = ["flower","alow","sloght"]
print(LongestCommonPrefix(Input))
'''
