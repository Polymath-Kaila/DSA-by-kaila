
# Linear algorith O(n)
# We use a for a loop 

```python
def print_n(n):
    for i in range(n):
        print(j)
print_n(10) 
# 0 1 2 3 4 5 6 7 8 9

```
So the for loop run 10 times.  
If we have another for loop for checking say j, it will run still 10 times for the same range.  

```python
def print_n(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
print_n(10)
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
```
so: n + n = 2n , drop constant = n:  
This O(n), this is proportional in that an increase in input reuslt in increase in time complexity.  
This produces a straight line graph.  

### Explain why linear algoriths scale better than quadratic algorithms.  

A linear algorithm's growth rate is proportional to the input size, why quadratic algorithm's grow much faster by a factor of four with the input increase.  

### Intuitively
A linear Algorithm processes each element `once`.  
A quadratic algorith compares every element with every other element creating nested work.  

- So as the input grows large, this extra repeated work in quadratic algorithm becomes extreamely expnsive.  

### Example

| Input Size (n) | Linear (O(n)) | Quadratic (O(n^2))    |
| -------------- | ------------- | --------------------- |
| 1,000          | 1,000 ops     | 1,000,000 ops         |
| 10,000         | 10,000 ops    | 100,000,000 ops       |
| 1,000,000      | 1,000,000 ops | 1,000,000,000,000 ops |

note `ops` is operations.  

### Conclusively
Linear algorithms scale better because their running time grows proportionally with input size, while quadratic algorithms grow with the square of the input, causing performance to degrade rapidly as data increases.