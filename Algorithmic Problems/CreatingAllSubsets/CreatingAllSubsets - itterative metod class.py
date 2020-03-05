'''
def creatingAllSubsets(input_set):
    all_subsets=[[]]
    for i in input_set:
        for j in range(len(all_subsets)):
            subset=all_subsets[j].copy()
            subset.append(i)
            all_subsets.append(subset)
    return all_subsets         


print(creatingAllSubsets([1,2,3,4]))
'''

''''
class CreatingAllSubsets:

    def __init__(self, input_set):
        self.all_subsets=[[]]
        for i in input_set:
            for j in range(len(self.all_subsets)):
                subset=self.all_subsets[j].copy()
                subset.append(i)
                self.all_subsets.append(subset)

    def __str__(self):
        return str(self.all_subsets)
    
print(CreatingAllSubsets([1,2,3,4]))
'''


class AllSubsets:


    def creatingAllSubsets(input_set):
        all_subsets=[[]]
        for i in input_set:
            for j in range(len(all_subsets)):
                subset=all_subsets[j].copy()
                subset.append(i)
                all_subsets.append(subset)
        return all_subsets
    
print(AllSubsets.creatingAllSubsets([1,2,3,4]))


'''
class AllSubsets:

    def creatingAllSubsets(self, input_set):
        self.all_subsets=[[]]
        for i in input_set:
            for j in range(len(self.all_subsets)):
                subset=self.all_subsets[j].copy()
                subset.append(i)
                self.all_subsets.append(subset)
        return self.all_subsets


print(AllSubsets().creatingAllSubsets([1,2,3,4]))
'''
