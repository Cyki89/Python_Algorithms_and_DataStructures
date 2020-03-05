
def create_powerset(inputset):
    powerset = []
    inputset_size = len(inputset)
    powerset_size = 2**inputset_size
    for i in range(powerset_size):
        subset = []
        for j in range(inputset_size):
            if (i & 2**j):
                subset.append(inputset[j])
        powerset.append(subset)
    return powerset
    

print(create_powerset([1,2,3,4]))



