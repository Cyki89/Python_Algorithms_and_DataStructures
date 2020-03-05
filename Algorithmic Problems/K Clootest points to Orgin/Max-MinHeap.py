class Heap():
    
    ''' special methods '''
    def __init__(self, args=[], max=True):
        self.heap = []
        self.max = max
        for arg in args:
            self.heap.append(arg)
            self.__floatUp(len(self.heap)-1)
    
    def __str__(self):
        if len(self.heap) > 0:
            return str(self.heap)
        else:
            return str(False)   
     
    ''' public methods '''
    def push(self, arg): # add element to heap
        self.heap.append(arg)
        self.__floatUp(len(self.heap)-1)
        
    def peak(self): # return top element
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return False
        
    def pop(self): # remove element from Heap (top) 
        if len(self.heap) > 1:
            self.__swap(0, len(self.heap)-1)
            top = self.heap.pop()
            self.__bubbleDown(0)
        elif len(self.heap) == 1:
            top = self.heap.pop()
        else:
            top = False
        return top
    
    ''' private methods '''   
    def __swap(self, i, j): 
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def __floatUp(self, index): # checking from down to up heap validity
        if index == 0: # ending floatingUP in index 0 (root)
            return
        parent = (index-1)//2
        if self.max == True and self.heap[index] > self.heap[parent] or \
           self.max == False and self.heap[index] < self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
            
    def __bubbleDown(self, index): # checking from up to down heap validity
        left_child = 2*index + 1
        right_child = 2*index + 2
        parent = index
        if len(self.heap) > left_child and \
           (self.max == True and self.heap[parent] < self.heap[left_child] or \
            self.max == False and self.heap[parent] > self.heap[left_child]):
                parent = left_child

        if len(self.heap) > right_child and \
           (self.max == True and self.heap[parent] < self.heap[right_child] or \
            self.max == False and self.heap[parent] > self.heap[right_child]):
                parent = right_child

        if index != parent:
            self.__swap(index, parent)
            self.__bubbleDown(parent)


M=Heap([1,2,3,4,5,6], True)
print(M.peak()) 
print(M)
M.pop()
print(M)
M.push(5)
print(M) 
##print(M.peak()) 
     
##M.push(4)
##print(M)
##M.push(3)
##M.pop()
##M.pop()
##print(M.peak()) 
##print(M)          


