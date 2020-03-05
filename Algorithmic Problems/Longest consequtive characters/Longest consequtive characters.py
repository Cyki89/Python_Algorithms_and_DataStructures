## Easy approach ##
'''
def find_LCCH(data):
    if data == '':
        return None
    
    count = 1
    result = [data[0], 1]

    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            if count > result[1]:
                result = (data[i-1], count)
            count = 1
    if count > result[1]:
                result = (data[i], count)
    return result


data='ABCD'
print(find_LCCH(data))
'''

## Efficient approach ? ##
'''
def find_LCCH(data):
    if data == '':
        return None
    
    LCCH = [data[0], 1]
    i = 0
    while i < len(data):
        try:
            if data[i] == data[i+LCCH[1]]:
                for j in range(i+1, i+LCCH[1]):
                    if data[i] != data[j]:
                        i += LCCH[1]+1
                        while i > 0 and data[i]==data[i-1]:
                            i -= 1
                        break
                else:
                    j = i+LCCH[1]
                    try:
                        while data[i] == data[j+1]:
                            j +=1
                    finally:
                        LCCH =[data[i], j-i+1]
                        i = j+1
            else:
                i +=1
        except:
            return LCCH


data='AABCBDBBBCDE'
print(find_LCCH(data))

'''
