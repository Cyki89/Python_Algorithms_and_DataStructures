'''
def subset_generator(inputset):
    for i in range(2**len(inputset)):
        subset = []
        for j in range(len(inputset)):
            if (i & 2**j):
                subset.append(inputset[j])
        yield subset
'''            

def subset_generator(inputset):
    for i in range(2**len(inputset)):
        yield [inputset[j] for j in range(len(inputset)) if (i & 2**j)]


for subset in subset_generator([1,2,3,4]):
    print(subset)
