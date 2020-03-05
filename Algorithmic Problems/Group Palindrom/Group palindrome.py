
def groupAnagrams(Input):

    myDict = {}
    result = []
    
    for i in range(len(Input)):
        key = ''.join(sorted(Input[i]))
        try:
            myDict[key].append(Input[i])
        except:
            myDict[key] = [Input[i]]

    for v in myDict.values():
        result.append(v)

    return result


Input = ["eata", "teaa", "tana", "atea", "nata", "bata", "eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(Input))
