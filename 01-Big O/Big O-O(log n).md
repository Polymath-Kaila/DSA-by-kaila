# Logarithmic Time Complexity - O(log n)
An Algorith runs in `logarithmic time` if the number of operations grows `very slowly` as the input size increases.  

Its denoted as:  
    `O(log n)`

---

An `O(log n)` algorithm `reduces the problem size by constant factor` at every step - most commonly by `half`.  

Instead of checking every element, it eliminates large portions of the data once.  

---
This scenario of seaching a word in a dictionary:  
+ We do not start from page 1 
+ We open the middle
+ Then the middle of the remaining half
+ And we repeat

---

## Example
We have to find a number in a list of 8 numbers:  
```text

1 2 3 4 5 6 7 8 
step1 we split into half:
[1 2 3 4] | [5 6 7 8]
step2 we split the first half:  
[1 2] | [3,4]
step3 we split the first  half:  
[1] | [2]

```
So we did 3 splits:  
The question to ask is how many half splits do we need to carry out for 8 numbers?  

so now:  
#### Mathematical expression:  
2 to power x = 8:  
for our case we got x as the three steps we carried:  

#### Generally
`n = 2 to power k.`  
solving for k:   
`k = log base 2 n.`    

thus:  
`O(log n)`

---

#### Why Base of Log doesn't Matter in Big O
    log2​n, log10​n, loge​n.  

All differ by a constant factor, which is dropped in Big O notation.  

Where O(log n) Commonly Appears
+ Binary search
+ Balanced binary search trees (AVL, Red-Black)
+ Heap operations (insert, delete)
+ Divide-and-conquer algorithms

---
#### Key sentence
Logarithmic time complexity occurs when an algorithm reduces the problem size by a constant factor at each step, resulting in very slow growth of running time as input size increases.

## Scenario we want to split 1 million number
so:  log base 2 of 1,000,000 equals to 6 steps only