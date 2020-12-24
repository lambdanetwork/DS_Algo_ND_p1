## how to run
```
   python3 solution.py
```

## Analysis
- Time complexity is **O(m * n)**  - search for m user within n group
- Space Complexity is **O(m + n)** - length of list user + lenght of list group

1. We have to walk to each user with m length, 
2. and if we cannot find user in this group, we have to walk the sub_groups with n length to run step 1 above