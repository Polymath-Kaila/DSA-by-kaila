# Linked Lists
## Why Linked Lists Exist ?
Arrays are powerful, but they have fudamental limitations:  
+ Fixed size (expensive resizing)
+ Insertions and deletions are costly
+ Elements must be stored contiguously in memory

- So linked lists were developed to solve these structural problems, not to replace arrays, but to complement them.  

---
## What is a Linked List ?
A **linked List** is a linear structure where elements are stored in `nodes` and each node contains:  
1. **Data**
2. A **pointer** refrence to the node

Unlike arrays:   
+ Elements are stored contiguously
+ Each element knows where the next one is

---

## Node building Block
Its defined by nodes.  

A node looks like:  
┌────────┬──────────┐
│  Data  │  Next →  │
└────────┴──────────┘

### Actual node code
```python
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

my_linked_list = LinkedList(1)
my_linked_list = LinkedList(2)
my_linked_list = LinkedList(3)

print(my_linked_list)

```