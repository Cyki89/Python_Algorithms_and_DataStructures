class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self, *args):
        self.head = node()
        for arg in args:
            self.append(arg)

    def __str__(self):
        elements = []
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            elements.append(curr_node.data)
        return str(elements)
        
    def append(self, data):
        new_node = node(data)
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def size(self):
        count = 0
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            count += 1
        return count 
    
    def get (self, index):
        if index >= self.size():
            print('Wrong index')
            return None
        curr_index = 0
        curr_node = self.head
        while curr_index != index:
           curr_node = curr_node.next         
           curr_index += 1
        return curr_node.next.data

    def erease (self, index):
        if index >= self.size():
            print('Wrong index')
            return None
        curr_index = 0
        last_node = self.head
        next_node = self.head.next
        while curr_index != index:
           last_node = next_node
           next_node = next_node.next           
           curr_index += 1
        last_node.next = next_node.next

        
'''
my_list = LinkedList(5,6,7)
print(my_list)
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list.size())
print(my_list)
print(my_list.get(0))
print(my_list.get(1))
my_list.erease(0)
print(my_list)
my_list.append(2)
my_list.append(3)
print(my_list)
print(my_list.get(0))
print(my_list.get(1))
'''
