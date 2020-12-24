## how to run
```
   python3 solution.py
```

## Analysis
1. For the union, we add the value to answer_dict
   - just walk through llist1 and llist2, and if the value already exist in answer_dict, ignore it to avoid duplicate
   - if the value is not exist in answer_dict, append to answer_llist
   - Time complexity is **O(m + n)**, for looping of m length llist1 and llist2 of n length
   - Space complexity is **O(m + n)**, 
      * dictionary of m size is used to map llist1, 
      * answer_llist has n size

2. For intersection the fastest solution that I can think of is to use dictionary
   - when we walk through the linkedlist1, we store the value in linkedlist1_dict.
   - then we walk through the linkedlist2, check only if value is found in list1, then append to answer_llist
   - Time complexity is **O(m + n)**, for looping of m length llist1 and llist2 of n length
   - Space complexity is **O(m + n)**, 
      * dictionary of m size is used to map llist1, 
      * answer_llist has n size
