
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
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

my_linked_list = LinkedList(2)
my_linked_list.prepend(3)

my_linked_list.print_list()

"""
  Explanation
  This is a bit easy right. 
  We have 2 cases, one when we have no node, 2 when we have nodes 
  Remember the node we want to prepend has a next, tail and head, but for this case we use its next and the head of the alredy existing node 
  For case 1, we check if no node, thats head and tail are pointing to None, the we point them to the new node and we are done
  For case 2, we take the new nodes next and point it to the head of the existing node, then we point the head of the existing node to the new node and thats it
  Take your time to synthesize the explanation

"""