class MaxHeap():
    
    ''' special methods '''
    def __init__(self, args=[]):
        self.heap = []
        for arg in args:            
            self.heap.append((arg, arg[0]**2+arg[1]**2))
            self.__floatUp(len(self.heap)-1)
    
    def __str__(self):
        if len(self.heap) > 0:          
            return str([p[0] for p in self.heap])
        else:
            return str(False)  
     
    ''' public methods '''
    def push(self, arg, magnitude): # add element to heap
        self.heap.append((arg, magnitude))
        self.__floatUp(len(self.heap)-1)
        
    def peak(self): # return top element
        if len(self.heap) > 0:
            return self.heap[0][1]
        else:
            return False
        
    def pop(self): # remove element from Heap (top) 
        if len(self.heap) > 1:
            self.__swap(0, len(self.heap)-1)
            maximum = self.heap.pop()[1]
            self.__bubbleDown(0)
        elif len(self.heap) == 1:
            maximum = self.heap.pop()[1]
        else:
            maximum = False
        return maximum
    
    ''' private methods '''   
    def __swap(self, i, j): 
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def __floatUp(self, index): # checking from down to up heap validity
        if index == 0: # ending floatingUP 0 (root)
            return
        parent = (index-1)//2
        if self.heap[index][1] > self.heap[parent][1]:
            self.__swap(index, parent)
            self.__floatUp(parent)
            
    def __bubbleDown(self, index): # checking from up to down heap validity
        left_child = 2*index + 1
        right_child = 2*index + 2
        largest = index
        if len(self.heap) > left_child and self.heap[largest][1] < self.heap[left_child][1]:
            largest = left_child
        if len(self.heap) > right_child and self.heap[largest][1] < self.heap[right_child][1]:
            largest = right_child
        if index != largest:
            self.__swap(index, largest)
            self.__bubbleDown(largest)


        


