"""
In this section we are now doing the append method of a linked list
We will first create a Node instance and a linked list classses
Then we are going to do the append method and we will clearly see the Big O of the operation
This section requires object oriented programming skill and control flow 

We have 2 scenarios of appending:
   1. when there is no node and head and tail are both pointing to "None"
   2. when we have nodes already in existence. for this case we do not touch the head, 
      we only append a node at the end and make the next of the last item to point to the last node, then now move the tail to point the last node we are appending 
"""

# declare a class for creating the Node

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

    def append(self,value): # scenario no node exists
        new_node = Node(value)
        if self.length ==0:
       # if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: # scenario 2 where nodes exist
            self.tail.next = new_node # we move the next pointer to the new node
            self.tail = new_node # we also move the tail to the new node which is now the last node
            self.length+=1 # we increament the length of the nodes

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()


"""
That is how we create an append method to our list we can clearly see the following:
   1. Append requires some steps like starting from head, traversing node by node and stopping at last node next==None
   2. Traversal touches evry node once so there are n nodes:  
       T(n) = n => O(n)
   3. In as much as head, tail move with a single step regardless n so to say O(1),
   4. Appending to a singly linked list is O(n) because the list must be traversed to find the last node before the insertion. 

"""
