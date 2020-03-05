# using list as extra space
'''
def isPalidrome(num):
    if num < 0:
        return False
    list_num = []
    while num > 0:
        list_num.append(num%10)
        num = num // 10
    if list_num == list_num[::-1]:
        return True
    else:
        return False
    
    
num = 0
print(isPalidrome(num))
'''

# without using extra space
'''
def isPalidrome(num):
    if num < 0:
        return False
    list_num = []
    while num > 0:
        list_num.append(num%10)
        num = num // 10
    if list_num == list_num[::-1]:
        return True
    else:
        return False
    
    
num = 0
print(isPalidrome(num))
'''
