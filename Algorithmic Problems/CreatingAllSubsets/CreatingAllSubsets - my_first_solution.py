'''
class CreatingSubsets:

    def __init__(self,input_set):
        self.all_subsets=[[]]
        max_lenght=len(input_set)
        i=0
        while i<max_lenght:
           subset=[]
           k=1; j=i
           while j<max_lenght:
              subset.append(input_set[j])
              self.all_subsets.append(subset.copy())
              j+=1
              if j==max_lenght:
                 subset=[input_set[i]]
                 k+=1; j=i+k
           i+=1                                           

    def __str__(self):
        return str(self.all_subsets)


print(CreatingSubsets([4, 5, 6, 7]))
'''


class AllSubsets:

    def creatingSubsets(self,input_set):
        self.all_subsets = [[]]

        for i in range(len(input_set)):
           subset=[]
           k = 1; j = i
           while j<len(input_set):
              subset.append(input_set[j])
              self.all_subsets.append(subset.copy())
              j += 1
              if j == len(input_set):
                 subset = [input_set[i]]
                 k += 1; j = i+k
        return str(self.all_subsets)


print(AllSubsets().creatingSubsets([4, 5, 6, 7]))
