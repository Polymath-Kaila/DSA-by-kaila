## Singly LinkedLists
Dont get scared this is not another concept.  
Its just the default linked lists we are working on this entire section whose folder is called LinkedList.  

## Key Properties Sigly Linked Lists
1. **One directional Traversal**

We can move:  
+ forward(`next`)
+ no backword

So once we move past a node, we cannot return unless we start over from the head.  

---

2. **No random access**
+ no indexes
+ no direct jumps

To reach the k-th element, we must traverse the first k-1 nodes.  
so Access = O(n)

---

3. **Dynamic size**
Nodes are:  
+ allocated individually
+ not contiguously in memory

The list can grow or shrink without resizing.  

---

## Basic Operations and Thier Costs

| Operation        | Time Complexity | Why                 |
| ---------------- | --------------- | ------------------- |
| Traverse         | (O(n))          | Visit each node     |
| Search           | (O(n))          | Sequential          |
| Insert at head   | (O(1))          | Pointer update      |
| Append (no tail) | (O(n))          | Must find last node |
| Delete at head   | (O(1))          | Pointer update      |
