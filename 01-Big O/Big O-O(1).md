# Constant Time Complexity - O(1)

An Algorithm runs in `constant time` if its execution time does not change as the input size grows.  

This is denoted as:  
`O(1)`

No matter how large the iput is, the algorithm always performs the same nuber of operations.  

It means the work done is indepent of input size.  

Example:  
```python
def get_first_element(arr):
    return arr[o]
```
Why this is O(1)?  
+ Accessing an element by index takes a fixed amount of time
+ Whether the array has 10 elements or 10 million, only ` one operation` is performed.  

If an algorithm performs a fixed number of steps:  
T(n) = 5

We drop constants, leaving:  
O(1)

---

## More Common O(1) Operations
+ Accessing an array element by index
+ Assigning a variable
+ Arithmetic operations (+, -, *, /)
+ Hash table lookup (average case)
+ Checking a boolean condition

Inshort steps taken to perform an operation are the same regardless of input size.  