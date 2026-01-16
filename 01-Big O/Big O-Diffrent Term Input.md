# This is a scenario where we have two different inputs.  

```python
def print_two_array(arr1, arr2):
    for x in arr1:
        print(x)

    for y in arr2:
        print(y)

```

let:  
+ size of `arr1` = n
+ size of `arr2` = m

Total work:  

`n + m`

so correct time complexity is:  
`O(n + m)`
Because the inputs are independent.  

