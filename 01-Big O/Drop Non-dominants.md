## Simplification

Take this loop:  

```python
def print_num(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)

print_num(3)

```
The first nested loops have a quadratic time complexity: `O(N2)`.  
The separed look `k` has a linear time complexity : `O(n)`.  

So we write:  `O(n2 + n)`

- When analyzing time complexity, we keep only the term that grows the fastest as input size increases and drop all smaller terms.
- This is because, for large inputs, the largest term dominates the toatal running time.  

For our case:  
+ `n2` grows much faster than n.  
+ `n` becomes insignificant as n increases

So we drop the non-dominant terms thats `n`.  

We end up with:  
`O(n2)`