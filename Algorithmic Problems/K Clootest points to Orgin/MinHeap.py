class MinHeap():
    
    ''' special methods '''
    def __init__(self, args=[]):
        self.heap = []
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
            minimum = self.heap.pop()
            self.__bubbleDown(0)
        elif len(self.heap) == 1:
            minimum = self.heap.pop()
        else:
            minimum = False
        return minimum
    
    ''' private methods '''   
    def __swap(self, i, j): 
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def __floatUp(self, index): # checking from down to up heap validity
        if index == 0: # ending floatingUP in index 0(root)
            return
        parent = (index-1)//2
        if self.heap[index] < self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
            
    def __bubbleDown(self, index): # checking from up to down heap validity
        left_child = 2*index + 1
        right_child = 2*index + 2
        smallest = index
        if len(self.heap) > left_child and self.heap[smallest] > self.heap[left_child]:
            smallest = left_child
        if len(self.heap) > right_child and self.heap[smallest] > self.heap[right_child]:
            smallest = right_child
        if index != smallest:
            self.__swap(index, smallest)
            self.__bubbleDown(smallest)


M=MinHeap([0,-1,-2,-3,-9])
print(M)
M.pop()
print(M)
M.push(5)
print(M.peak()) 
print(M)      
         


