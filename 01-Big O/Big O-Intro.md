# Big O Concepts:
+ `O(1)`: Constant Time
    + Does not depent on the size of the data set
    + Example Accessing an array element by its index
+ `O(log n)`: Logarithmic Time
    + Splits the data in each step (`divide and conquer`)
    + Example Binary search
+ `O(n)`: Linear Time
    + Directly proportional to the data set size.  
    + Example: Looping through an array.
+ `O(n log n)`: Linearithmic Time
    + Splits and sorts or searches data
    + Example : Merge sort, quick sort
    
+ `O(n2)`: Polynomial Time
    + Nested loops for each power of n
    + Example: Bubble sort (O(n2))

---
### `Omega(Ω)` -Best Case
- `What it means` : Omega describes the best case scenario for an algorith.  
- `In simple terms`: It tells us fastedt an algorithm can run in the best circumstance.

---

### `Theta(Θ)` - Average Case
- `In simple terms` it tells us what to generally expect interms of time complexity.

---

### `Big O (O)` - Worst Case
- `What it means:` Big O descibes the worst-case scenario for an algorithm.
- `In simple terms:` It tells us the slowest an algorithm can run in the worst circustances.  

---

### Other concepts:
+ `Drop Non-Dominant Terms`
    + In O(n2 + n), focus on O(n2
) as it will dominate for large n.

+ `Drop Constants`
    + `O(2n)` simplify to `O(n)`