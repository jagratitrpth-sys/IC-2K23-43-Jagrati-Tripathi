# Lab 6: A* (A-Star) Search Algorithm

## Problem Statement
Implement the A* Search algorithm to find the optimal path from a start node to a goal node in a weighted graph.

## Approach & Theoretical Concepts
A* is a **Best-First Search** algorithm that finds the shortest path by combining two pieces of information:
1. $g(n)$: The exact cost of the path from the starting node to any node $n$.
2. $h(n)$: The heuristic estimated cost from node $n$ to the goal.

The algorithm selects the path that minimizes the total estimated cost:
**$f(n) = g(n) + h(n)$**

### Key Characteristics
* **Completeness:** Yes, it will always find a solution if one exists.
* **Optimality:** Yes, it is guaranteed to find the shortest path, provided the heuristic $h(n)$ is **admissible** (it never overestimates the true cost to reach the goal).
* **Data Structure:** Priority Queue (Min-Heap) sorted by $f(n)$.

**Time Complexity:** $O(b^d)$, where $b$ is the branching factor and $d$ is the depth of the solution.
**Space Complexity:** $O(b^d)$, as it keeps all generated nodes in memory.

## Expected Output
```text
Starting A* Search from 'S' to 'G'...

Evaluating: S (f=7.0, g=0.0, h=7.0)
Evaluating: A (f=7.0, g=1.0, h=6.0)
Evaluating: B (f=7.0, g=3.0, h=4.0)
Evaluating: C (f=7.0, g=5.0, h=2.0)
Evaluating: G (f=8.0, g=8.0, h=0.0)

Goal 'G' reached! Optimal cost: 8

Optimal Path: S -> A -> B -> C -> G