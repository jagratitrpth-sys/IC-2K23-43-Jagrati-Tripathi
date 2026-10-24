# Lab 5: Greedy Best-First Search

## Problem Statement
Implement the Best-First Search algorithm to find a path from a start node to a goal node. The algorithm must utilize a heuristic function $h(n)$ to decide which node to explore next.

## Approach & Theoretical Concepts
Greedy Best-First Search is an **Informed Search** algorithm. Unlike BFS (which uses a standard Queue) or DFS (which uses a Stack), Best-First Search uses a **Priority Queue**. 

At every step, it evaluates all available nodes in the queue and selects the one with the lowest heuristic value $h(n)$—meaning it looks like it is the closest to the goal.

### Characteristics
* **Evaluation Function:** $f(n) = h(n)$
* **Data Structure:** Priority Queue (Min-Heap)
* **Drawback:** It is "greedy." It only looks at the immediate heuristic estimate and ignores the actual cost taken to reach the node. This means it can easily get trapped in dead ends or find sub-optimal paths compared to algorithms like A*.

**Time Complexity:** $O(b^d)$ in the worst case (where $b$ is the branching factor and $d$ is the maximum depth).
**Space Complexity:** $O(b^d)$ as it stores all generated nodes in memory.

## Expected Output
```text
Starting Best-First Search from 'S' to 'G'...

Visited: S (h=10)
Visited: B (h=6)
Visited: F (h=2)
Visited: G (h=0)

Goal 'G' reached!

Traversal Order: S -> B -> F -> G