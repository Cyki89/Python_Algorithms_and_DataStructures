## Basic approach
'''
def BS_tuple(intervals, newInterval):
    
    x = newInterval[0]
    l = 0; r = len(intervals)-1
    
    while l <= r:
        
        s = (l+r)//2
        
        if x == intervals[s][0]:
            return s    
        elif x > intervals[s][0]:
            l = s + 1
        else:
            r = s - 1
    
    while s > 0 and x > intervals[s][0]:
        s -= 1
    
    return s


def insertInterval(intervals, newInterval):
    
    pos = BS_tuple(intervals, newInterval)
    intervals.insert(pos,newInterval)
    merge = []
    
    for i in range(len(intervals)):
        
        if not merge or merge[-1][1] < intervals[i][0]:
            merge.append(intervals[i]) 
        else:
            merge[-1][1] = max(merge[-1][1], intervals[i][1])
    
    return merge
           

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [11,12]

print(insertInterval(intervals, newInterval))
'''

## Efficent approach (without inserting interwal)
'''
def BS_tuple(intervals, newInterval):
    
    x = newInterval[0]
    l = 0; r = len(intervals)-1
    
    while l <= r:
      
        s = (l+r)//2
        
        if x == intervals[s][0]:
            return s    
        
        elif x > intervals[s][0]:
            l = s + 1
            
        else:
            r = s - 1
    
    while s > 0 and x > intervals[s][0]:
        s -= 1
    
    return s


def insertInterval(intervals, newInterval):
    
    pos = BS_tuple(intervals, newInterval)
    merge = intervals[:pos] if pos > 0 else []

    if not merge or merge[-1][1] < newInterval[0]:
        merge.append(newInterval)           

    else:
        merge[-1][1] = max(merge[-1][1], newInterval[1])    

    i = pos

    while i < len(intervals):

        if merge[-1][1] < intervals[i][0]:
            break

        else:
            merge[-1][1] = max(merge[-1][1], intervals[i][1])              

        i += 1
        
    merge += intervals[i:]
    
    return merge
          

intervals = [[1,2],[4,5],[6,7],[8,10],[12,16]]
newInterval = [1,4]

print(insertInterval(intervals, newInterval))
'''


## Optimal approach II (with merge newInterval in place)

def insertInterval(intervals, newInterval):
    
    merge = []
    i = 0
    
    while i < len(intervals) and intervals[i][1] < newInterval[0]: # before overlaping
            merge.append(intervals[i]) 
            i += 1
    
    while i < len(intervals):  # merge state 
        
        if  intervals[i][0] > newInterval[1]: # after merge 
            merge.append(newInterval)
            merge += intervals[i:]
            break
        
        else:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
        
        i +=1
    
    if  intervals[-1][0] <= newInterval[1]: # if still merging 
            merge.append(newInterval)
    
    return merge
          

intervals = [[1,2],[4,5],[6,7],[8,10],[12,16]]
newInterval = [11,12]

print(insertInterval(intervals, newInterval))
