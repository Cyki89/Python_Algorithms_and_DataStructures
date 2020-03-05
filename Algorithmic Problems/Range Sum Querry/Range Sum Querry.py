# Immutable solution
'''
class NumArray():
    def __init__(self, nums):
        n = len(nums) +1
        self.nums = [0 for i in range(n)]
        for i in range(1,n):
            self.nums[i] += self.nums[i-1] + nums[i-1]    
    
    def sumRange(self, start, end):
        return self.nums[end+1] - self.nums[start]
       

nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))
'''



# Mutable solution (with update function)
'''
class SegmentTree():
   
    def __init__(self, nums):
        n = self.segTree_size(nums)
        self.segTree = [None for i in range(n)]
        self.lazyTree = [0 for i in range(n)]
        self.createSegTree(nums, 0, len(nums)-1, 0) ## len(nums)-1
    
    def segTree_size(self, nums):
        n = 1 
        while n < len(nums):
            n = n*2
        return 2*n-1
    
    def createSegTree (self, nums, low, high, pos):
        if low == high:
            self.segTree[pos] = nums[low]
            return
        mid = (low+high)//2
        self.createSegTree (nums, low, mid, 2*pos+1) ## left child 
        self.createSegTree (nums, mid+1, high, 2*pos+2) ## right child 
        self.segTree[pos] = self.segTree[2*pos+1] + self.segTree[2*pos+2] ## sum of caculated left and right child
    
    def sumRange(self, qlow, qhigh):
        return self._sumRange(qlow, qhigh, 0, len(nums)-1, 0)
    
    def _sumRange(self, qlow, qhigh, low, high, pos):
        if low >= qlow and high <= qhigh: ## total overlap
            return self.segTree[pos]
        elif low > qhigh or high < qlow: ## no overlap 
            return 0
        mid = (low+high)//2
        return self._sumRange(qlow, qhigh, low, mid, 2*pos+1) + \
               self._sumRange(qlow, qhigh, mid+1, high, 2*pos+2)  
    
    def update(self, index, value):
        diff = value - nums[index]
        nums[index] = value
        self._update(index, diff, 0, len(nums)-1, 0)
    
    def _update(self, index, diff, low, high, pos):
        if index < low or index > high: ## index out of range
            return
        else: ## indexx in range
            self.segTree[pos] += diff 
            if  low == high: ## end of range
                return 
            mid = (low+high)//2
            self._update(index, diff, low, mid, 2*pos+1)
            self._update(index, diff, mid+1, high, 2*pos+2)
    
    def lazyUpdate(self, qlow, qhigh, diff):
        for i in range(qlow, qhigh+1):
            nums[i] += diff
        self._lazyUpdate(qlow, qhigh, diff, 0, len(nums)-1, 0)
    
    def _lazyUpdate(self, qlow, qhigh, diff, low, high, pos):
        if low > high: 
            return
        if self.lazyTree[pos]!= 0: 
            self.segTree[pos] += self.lazyTree[pos] * (1+high-low)
            if low != high: ## update children lazyTree values
                self.lazyTree[2*pos+1] += self.lazyTree[pos]    
                self.lazyTree[2*pos+2] += self.lazyTree[pos]  
            self.lazyTree[pos] = 0
        if low > qhigh or high < qlow: ## no overlap
            return
        if qlow <= low and qhigh >= high:
            self.segTree[pos] += diff * (1+high-low)
            if low != high: ## update children lazyTree values
                self.lazyTree[2*pos+1] += diff     
                self.lazyTree[2*pos+2] += diff 
            return
        mid = (low+high)//2 ## partialy overlap 
        self._lazyUpdate(qlow, qhigh, diff, low, mid, 2*pos+1)
        self._lazyUpdate(qlow, qhigh, diff, mid+1, high, 2*pos+2) 
        self.segTree[pos] = self.segTree[2*pos+1] + self.segTree[2*pos+2]
    
    def lazySumRange(self, qlow, qhigh):
        return self._lazySumRange(qlow, qhigh, 0, len(nums)-1, 0)
    
    def _lazySumRange(self, qlow, qhigh, low, high, pos):
        if low > high:
            return 0
        if self.lazyTree[pos]!= 0: 
            self.segTree[pos] += self.lazyTree[pos] * (1+high-low)
            if low != high: ## update children lazyTree values
                self.lazyTree[2*pos+1] += self.lazyTree[pos]    
                self.lazyTree[2*pos+2] += self.lazyTree[pos]  
            self.lazyTree[pos] = 0
        if qlow <= low and qhigh >= high: ## total overlap
            return self.segTree[pos]
        if low > qhigh or high < qlow: ## no overlap 
            return 0
        mid = (low+high)//2
        return self._lazySumRange(qlow, qhigh, low, mid, 2*pos+1) + \
               self._lazySumRange(qlow, qhigh, mid+1, high, 2*pos+2)
        
    def printTree(self):
        print('lazyTree:\n', self.lazyTree)
        print('segTree:\n', self.segTree)
       

nums = [1,2,3,4]
obj = SegmentTree(nums)
obj.printTree()
obj.lazyUpdate(0, 2, 1)
print(obj.lazySumRange(0, 0))
obj.printTree()
#obj.update(0,2)
#print(obj.sumRange(0, 0))
#print(obj.sumRange(0, 4))
#print(obj.sumRange(2, 5))
#print(obj.sumRange(0, 5))
#obj.printTree()

'''



# 2d Immutable solution catches row
'''

class NumMatrix():
    def __init__(self, matrix):
        self.matrix = [[0 for c in range(len(matrix[0])+1)] for r in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.matrix[r][c+1] = self.matrix[r][c] + matrix[r][c]        
                
    def sumRegion(self, r1, c1, r2, c2):
        result = 0
        for r in range(r1,r2+1):
            result += self.matrix[r][c2+1] - self.matrix[r][c1]
        return result

        
matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
          ]

obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))

'''

# 2d Smart solution 
class NumMatrix():
    def __init__(self, matrix):
        self.matrix = [[0 for c in range(len(matrix[0])+1)] for r in range(len(matrix)+1)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.matrix[r+1][c+1] = matrix[r][c] + self.matrix[r][c+1] + self.matrix[r+1][c] - self.matrix[r][c]        
                
    def sumRegion(self, r1, c1, r2, c2):
        return self.matrix[r2+1][c2+1] - self.matrix[r1][c2+1] - self.matrix[r2+1][c1] + self.matrix[r1][c1]

        
matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
          ]

obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))

'''
