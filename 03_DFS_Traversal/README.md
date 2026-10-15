# Lab 3: Depth-First Search (DFS) Graph Traversal

## Problem Statement
Implement the Depth-First Search (DFS) algorithm. The program must start at a root node and explore as far as possible along each branch before backtracking. 

## Approach & Algorithm
This implementation models the graph as an **Adjacency List** using a Python dictionary and uses **Recursion** to traverse it.

The core of DFS relies on a **Stack** (Last-In-First-Out). By using recursion, we let the computer's built-in call stack manage this for us:
1. Visit the current node and mark it as visited.
2. Iterate through its neighbors.
3. If a neighbor is unvisited, recursively call the DFS function on that neighbor.
4. When a node has no unvisited neighbors left, the function returns (backtracks) to the previous node.

**Time Complexity:** $O(V + E)$ where $V$ is the number of vertices and $E$ is the number of edges.
**Space Complexity:** $O(V)$ in the worst case (a completely linear graph) due to the recursive call stack depth.

## Expected Output
```text
Starting Recursive DFS traversal from node 'A'...

DFS Traversal Order: A -> B -> D -> E -> H -> C -> F -> G