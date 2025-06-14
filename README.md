# Inverting a Binary Tree

This means swapping the left and right children of every node in the tree. This is a classic problem and very common in job interviews.

# Theory

Given a binary tree, invert it by recursively swapping the left and right child of each node.

Ex:

```bash
Before:               After:
    1                   1
   / \                 / \
  2   3      -->      3   2
 / \ / \             / \ / \
4  5 6  7           7  6 5  4
```

## How to invert?

**Possible strategies**:

1. Recursive (DFS - Depth First Search)  
    For each node:  
        - invert the left subtree  
        - invert the right subtree  
        - swap the pointers  

2. Iterative (using queue - BFS - Breadth First Search)  
    - use a queue (or stack)  
    - visit each node and swap its children  
    - add the children to the queue to continue the process  

## Complexity

- **Time:** O(n) where `n` is the number of nodes  
- **Space:**  
    - Recursive: O(h) where `h` is the height of the tree (due to the stack)  
    - Iterative: O(n) in the worst case if
