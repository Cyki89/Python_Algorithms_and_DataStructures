def creatingAllSubsets(input_set):
    all_subsets=[]
    creatingSubsets(all_subsets, [], input_set, 0)
    return all_subsets
    
def creatingSubsets(all_subsets, subset, input_set, start):
    all_subsets.append(subset.copy())
    for i in range(start,len(input_set)):
        subset.append(input_set[i])
        creatingSubsets(all_subsets, subset, input_set, i+1)
        subset.pop()
       


print(creatingAllSubsets([1,2,3]))
