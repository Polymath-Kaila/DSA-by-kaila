class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self): # this is just for printing the outputs
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if self.length ==0:
            self.tail = None
        return temp.value

my_linked_list = LinkedList(2)
# 2 items
print(my_linked_list.pop_first())

# 1 item
print(my_linked_list.pop_first())

# 0 item
print(my_linked_list.pop_first())

"""
Same concept follow through

"""