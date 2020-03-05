class node:
    
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
    
        
def validate_bst(root, min_value = float('-inf'), max_value = float('-inf')):
    
    if root == None:
        return True
    
    if root.value < min_value or root.value > max_value:
        return False
    
    return (validate_bst(root.left_child, min_value, root.value) and 
            validate_bst(root.right_child, root.value, max_value))
    
    
root = node(5)
leftChild = node(2)
rightChild = node(10)
rightRightChild = node(11)
leftRightChild = node(4)
root.left_child=leftChild
root.right_child=rightChild
rightChild.right_child=rightRightChild
rightChild.left_child=leftRightChild
print(validate_bst(root, min_value = float('-inf'), max_value = float('inf')))
