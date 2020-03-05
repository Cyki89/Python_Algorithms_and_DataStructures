class node:
    def __init__(self, value = None):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None


class BST():
    def __init__(self, *args):
        self.root = None
        for arg in args:
            self.insert(arg)
    
    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, curr_node):
        
        if value < curr_node.value: 
            if curr_node.left_child != None:
                self._insert(value, curr_node.left_child)
            else:
                curr_node.left_child = node(value)
                curr_node.left_child.parent = curr_node
        elif value > curr_node.value: 
            if curr_node.right_child != None:
                self._insert(value, curr_node.right_child)
            else:
                curr_node.right_child = node(value)
                curr_node.right_child.parent = curr_node
        else:
            print("value already inserted")
        
    def print_tree(self):
        if self.root != None:
           self._print_tree(self.root) 
        else:
            print("Tree is empty")
           
    def _print_tree(self, curr_node):
        if curr_node != None:
            self._print_tree(curr_node.left_child)
            print(curr_node.value)
            self._print_tree(curr_node.right_child)
    
    def height(self):
        if self.root == None:
           return 0
        else:
            return self._height(self.root, 0)
    
    def _height(self, curr_node, h):
        if curr_node == None:
            return h
        return max(self._height(curr_node.left_child, h+1), self._height(curr_node.right_child, h+1))

    def search(self,value):
        if self.root == None:
           return False 
        else:
            return self._search(self.root,value)

    def _search(self, curr_node, value):
        if value == curr_node.value:
            return True
        elif value < curr_node.value and curr_node.left_child != None:
            return self._search(curr_node.left_child, value) 
        elif value > curr_node.value and curr_node.right_child != None:
            return self._search(curr_node.right_child, value) 
        return False

    def find(self, value):
        if self.root == None:
           return None 
        else:
            return self._find(self.root,value)
    
    def _find(self, curr_node, value):
        if value == curr_node.value:
            return curr_node
        elif value < curr_node.value and curr_node.left_child != None:
            return self._find(curr_node.left_child, value) 
        elif value > curr_node.value and curr_node.right_child != None:
            return self._find(curr_node.right_child, value) 
        return None
    
    def delete_value(self, value):
        self.delete_node(self.find(value))

    def delete_node(self, node):
        def min_value_node(node):
            curr_node = node
            while curr_node.left_child != None:
                curr_node = node.left_child                  
            return curr_node

        def num_of_child(node):
            num_of_child = 0
            if node.left_child != None:
                num_of_child += 1
            if node.right_child != None:
                num_of_child += 1
            return num_of_child

        node_children = num_of_child(node)
        
        node_parent = node.parent
        
        if node_children == 0:
           if node_parent:
               if node_parent.left_child == node:
                   node_parent.left_child = None
               else:
                   node_parent.right_child = None
           else:
               self.root = None

        if node_children == 1:            
            if node.left_child != None:
               child = node.left_child
            else:
               child = node.right_child
            if node_parent:
                if node_parent.left_child == node:
                   node_parent.left_child = child
                else:
                   node_parent.right_child = child
            else:
                self.root = child 
            child.parent = node_parent
            
        if node_children == 2:
            successor = min_value_node(node.right_child)
            node.value = successor.value
            
            self.delete_node(successor)
        
    
my_tree = BST(10,2,5,8,11,3)
my_tree.print_tree()
print('-----------')
my_tree.delete_value(10)
my_tree.delete_value(2)
my_tree.print_tree()
print('-----------')
