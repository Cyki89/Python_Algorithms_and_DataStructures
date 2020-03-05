## Recursive solution
'''
from math import ceil

def LCA(tree, p, q):
    
    p_index = tree.index(p); p_path = [p_index]
    q_index = tree.index(q); q_path = [q_index]
    r_index = helper(p_index, q_index, p_path, q_path)

    return tree[r_index]

 
   
def helper(p, q, p_path, q_path):
    
  try:
    return (set(p_path) & set(q_path)).pop()
  except:  
    if p > q:
         q_index = q
         p_index = ceil(p/2)-1
         p_path.append(p_index)        
    else:
         p_index = p 
         q_index = ceil(q/2)-1
         q_path.append (q_index)     
    return helper(p_index, q_index, p_path, q_path)

   
tree = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 1

print(LCA(tree, p, q))
'''


## Iterative solution
'''
from math import ceil

def LCA(tree, p, q):
    
    p_index = tree.index(p); p_path = [p_index]
    q_index = tree.index(q); q_path = [q_index]

    while True:
        try:
            return tree[(set(p_path) & set(q_path)).pop()]
        except:
            if p_index > q_index:
                p_index = ceil(p_index/2)-1
                p_path.append(p_index)
            else:
                q_index = ceil(q_index/2)-1
                q_path.append(q_index) 
  
  
tree = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 6

print(LCA(tree, p, q))
'''
