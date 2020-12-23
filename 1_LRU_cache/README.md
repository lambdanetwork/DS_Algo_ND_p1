## how to run
```
   python3 solution.py
```

## Analysis
1. Time complexity is **O(1)** 
2. To achieve constant complexity, we need to store it in dictionary.
   - accessing value in dictionary is O(1)
3. However key in dictionary is unordered, perhaps if python has Map() which has ordered key
4. To quickly move to first element and last element, we will use double LinkedList
   - remove method:
      * we will get the pointer to Node in dictionary, accessing it is O(1)
      * detach this Node from double linkedlist
      * remove this pointer from Dictionary

   - set method:
      * create the Node and set the Node to head of double LList
      * store the pointer to this node to Dictionary.
      * if capacity is reached, remove the tail from doubleLList, and the Node from dictionary

   - get method:
      * get value from dictionary O(1)
      * remove this node from DoubleLList and set it back to head 
