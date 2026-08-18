from collections import deque

def water_jug_bfs(capacity_a, capacity_b, target):
    """
    Solves the Water Jug problem using Breadth-First Search.
    Returns the sequence of steps to reach the target amount.
    """
    # Queue stores tuples of (jug_a_current, jug_b_current, path_taken_so_far)
    queue = deque([(0, 0, [])])
    
    # Keep track of visited states to prevent infinite loops
    visited = set()
    visited.add((0, 0))

    while queue:
        a, b, path = queue.popleft()
        
        # Check if we've reached the goal state in either jug
        if a == target or b == target:
            path.append((a, b)) # Add the final state to the path
            return path
            
        # Define all possible next states (rules)
        next_states = set([
            (capacity_a, b), # Rule 1: Fill Jug A
            (a, capacity_b), # Rule 2: Fill Jug B
            (0, b),          # Rule 3: Empty Jug A
            (a, 0),          # Rule 4: Empty Jug B
            # Rule 5: Pour B into A until A is full or B is empty
            (min(a + b, capacity_a), max(0, a + b - capacity_a)), 
            # Rule 6: Pour A into B until B is full or A is empty
            (max(0, a + b - capacity_b), min(a + b, capacity_b))  
        ])
        
        for state in next_states:
            if state not in visited:
                visited.add(state)
                # Append the new state to the queue along with the updated path
                queue.append((state[0], state[1], path + [(a, b)]))
                
    return None # Return None if no solution is possible

# --- Execution ---
if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target_amount = 2

    print(f"Solving Water Jug: Jug1={jug1_capacity}L, Jug2={jug2_capacity}L, Target={target_amount}L\n")
    solution = water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)

    if solution:
        print("Solution found in", len(solution) - 1, "steps:")
        for step, state in enumerate(solution):
            print(f"Step {step}: Jug A = {state[0]}L | Jug B = {state[1]}L")
    else:
        print("No solution exists for the given capacities and target.")