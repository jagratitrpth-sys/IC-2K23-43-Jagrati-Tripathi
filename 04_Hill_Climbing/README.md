# Lab 4: Hill Climbing Algorithm

## Problem Statement
Implement the Hill Climbing search algorithm to find the peak (maximum value) of an objective function $f(x)$ starting from an arbitrary initial state.

## Approach & Theoretical Concepts
Hill Climbing is an **Informed Local Search** algorithm that uses an evaluation heuristic function to drive decisions.

<Image src="image_agent_tag_8338726620585358960" alt="State space surface graph displaying local maximum, global maximum, shoulder, and flat local maximum" caption="Hill Climbing State Space Landscape" />

### Key Characteristics & Drawbacks
1. **Local Maxima:** The algorithm can get stuck on a peak that is higher than its immediate neighbors but lower than the global maximum.
2. **Plateaus / Flat Region:** A flat area where neighboring states have the exact same value, giving the algorithm no direction to climb.
3. **Ridge:** An elevated region where the orientation forces the search into an apparent peak from single-step moves.

**Time Complexity:** Variable, dependent on step size and search space height.
**Space Complexity:** $O(1)$ constant space, as only the current state and candidate neighbors are kept in memory.

## Expected Output
```text
Starting Hill Search from x = -2.5000...

Initial State: x = -2.5000 | f(x) = -17.2500

Step 01: Moved to x = -2.4000 | f(x) = -15.9600
Step 02: Moved to x = -2.3000 | f(x) = -14.6900
...
Step 64: Moved to x = 3.9000 | f(x) = 24.9900
Step 65: Moved to x = 4.0000 | f(x) = 25.0000
Terminated at step 66: Local/Global Maximum reached!

Optimal Solution Found: x = 4.0000 with Peak Value f(x) = 25.0000