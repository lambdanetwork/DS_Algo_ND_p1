## how to run
```
   python3 solution.py
```

## Analysis
- Time complexity is **O(n)** for the longest size of linked_list
1. For the union, we add the value to answer_dict
   - just walk through llist1 and llist2, and if the value already exist in answer_dict, ignore it to avoid duplicate
   - if the value is not exist in answer_dict, append to answer_llist

2. For intersection the fastest solution that I can think of is to use dictionary
   - when we walk through the linkedlist1, we store the value in linkedlist1_dict.
   - then we walk through the linkedlist2, if the value is find in linkedlist1_dict