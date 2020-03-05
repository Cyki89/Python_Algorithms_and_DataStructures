def creatingAllSubsets(input_set):
    all_subsets=[]
    creatingSubsets(all_subsets, [], input_set, 0)
    return all_subsets
    
def creatingSubsets(all_subsets, subset, input_set, i):
    if i == len(input_set):
        all_subsets.append(subset)
    else:
        creatingSubsets(all_subsets, subset.copy(), input_set, i+1)
        subset.append(input_set[i])
        creatingSubsets(all_subsets, subset, input_set, i+1)


print(creatingAllSubsets([1,2,3,4]))
