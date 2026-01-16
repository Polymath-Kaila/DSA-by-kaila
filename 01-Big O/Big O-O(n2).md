# Quadratic Algorithm
This algorithm has quadratic time complexity since the number of operations grows proportionally to the square of the input size.  

Denoted as : O(n2)
Quadratic time complexity most commonly appears when an algorithm uses nested loops where:  
+ The outer loop runs `n` times
+ The inner loop also runs `n` times for each outer iteration.  

---

## We Use a nested for loop

```python
def print_num(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_num()

```
Total execution of `print(i,j)` = `n2`.  
so for n = 3;  

The operation looks like:  

```scss
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
```
That is:  `3 * 3 = 9` operations

---

### Why are Quadratic algorithms Slow at Scale
- Quadratic algorithms perform `repeated work.`
For Large inputs:   
 - Doubling the input size results in four times the work
 - This rapid growth makes them unsuitable for large datasets

---

### Common Real-World Examples

Quadratic time appears in algorithms that:

+ Compare every item with every other item
+ Use brute-force pairwise comparisons

Examples:

1. Bubble Sort
2. Selection Sort
3. Checking all pairs in a list