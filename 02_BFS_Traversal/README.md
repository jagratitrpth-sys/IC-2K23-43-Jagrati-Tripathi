# Lab 2: Breadth-First Search (BFS) Graph Traversal

## Problem Statement
Implement the Breadth-First Search (BFS) algorithm to traverse a graph data structure. The program must start at a given root node and explore all neighboring nodes at the present depth prior to moving on to the nodes at the next depth level.

## Approach & Algorithm
This implementation models the graph as an **Adjacency List** using a Python dictionary. 

The core of BFS relies on a **Queue** (First-In-First-Out) data structure:
1. Initialize a queue and add the starting node.
2. Mark the starting node as visited using a `set`.
3. Loop until the queue is empty:
   - Dequeue a node and add it to our final traversal path.
   - Find all its unvisited neighbors.
   - Mark them as visited and enqueue them.

**Time Complexity:** $O(V + E)$ where $V$ is the number of vertices and $E$ is the number of edges.
**Space Complexity:** $O(V)$ to store the queue and the visited set.

## Expected Output
```text
Starting BFS traversal from node 'A'...

BFS Traversal Order: A -> B -> C -> D -> E -> F -> G -> H