# Lab 1: The Water Jug Problem

## Problem Statement
You are given two jugs with capacities `x` and `y` liters. There is an infinite amount of water supply. You need to measure exactly `z` liters of water. You can perform the following operations:
1. Fill a jug completely.
2. Empty a jug entirely.
3. Pour water from one jug to another until the receiving jug is full, or the pouring jug is empty.

## Approach & Algorithm
This implementation uses **Breadth-First Search (BFS)**. 
BFS explores the state space graph level by level. We use a queue to keep track of the current water levels `(Jug A, Jug B)` and the path taken to get there. We also use a `visited` set to ensure we don't process the same state twice, avoiding infinite loops.

BFS guarantees that we find the solution requiring the minimum number of pouring steps.

## Expected Output
```text
Solving Water Jug: Jug1=4L, Jug2=3L, Target=2L

Solution found in 6 steps:
Step 0: Jug A = 0L | Jug B = 0L
Step 1: Jug A = 0L | Jug B = 3L
Step 2: Jug A = 3L | Jug B = 0L
Step 3: Jug A = 3L | Jug B = 3L
Step 4: Jug A = 4L | Jug B = 2L
Step 5: Jug A = 0L | Jug B = 2L