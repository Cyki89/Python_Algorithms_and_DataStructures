def overlapIntervals(Input):
    
    if len(Input) == 0:
        return []   
    
    Input.sort()
    
    newInput = [Input[0]]
    
    for i in range(1,len(Input)):
        end = len(newInput)-1
        if newInput[end][1]-Input[i][0] >= 0:
            newInput[end] = [newInput[end][0],max(Input[i][1],newInput[end][1])] 
        else:
            newInput.append(Input[i])
    return newInput     


Input = [[1,3],[2,6],[8,10],[15,18]]
newInput=overlapIntervals(Input)
print(newInput)
