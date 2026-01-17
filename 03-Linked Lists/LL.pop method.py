class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail =  new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        previous = self.head
        
        while (temp.next):
            previous = temp
            temp = temp.next
        self.tail = previous
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

my_linked_list = LinkedList(2)

my_linked_list.pop()
my_linked_list.print_list()

"""
This pop is a bit tricky right.
We need to a temporary pointer called temp and a pre for tracking the previous node
We have three cases here, one is for no node, 2 is we have a single node and 3 we have multiple nodes
So this is what we do for no node we just check length and return none because we have nothing to work ok
For the case where we have nodes already, we need to have two vars one (temp)for traversing through nodes checking for next whether its none,
The second var is (pre) for tracking the previous item to which after pop its where our tail will point ok
The third case iw whwn we have a single node an we want to pop the node out, here we simple asign head and tail to none since they are pointing at the same node no traversion

"""