import random

def objective_function(x):
    """
    Objective function to maximize: f(x) = -(x - 4)^2 + 25
    Maximum occurs at x = 4, where f(4) = 25.
    """
    return -(x - 4)**2 + 25

def get_neighbors(current_state, step_size=0.1):
    """Generates small left and right step neighbors of the current state."""
    return [current_state - step_size, current_state + step_size]

def hill_climbing(start_state, max_iterations=100, step_size=0.1):
    """
    Steepest-Ascent Hill Climbing Algorithm.
    """
    current_state = start_state
    current_score = objective_function(current_state)
    
    print(f"Initial State: x = {current_state:.4f} | f(x) = {current_score:.4f}\n")
    
    for step in range(1, max_iterations + 1):
        neighbors = get_neighbors(current_state, step_size)
        best_neighbor = None
        best_neighbor_score = float('-inf')
        
        # Evaluate all neighbors to find the steepest ascent
        for neighbor in neighbors:
            score = objective_function(neighbor)
            if score > best_neighbor_score:
                best_neighbor_score = score
                best_neighbor = neighbor
                
        # If the best neighbor does not improve the current state, we've hit a peak
        if best_neighbor_score <= current_score:
            print(f"Terminated at step {step}: Local/Global Maximum reached!")
            break
            
        # Move to the best neighbor
        current_state = best_neighbor
        current_score = best_neighbor_score
        print(f"Step {step:02d}: Moved to x = {current_state:.4f} | f(x) = {current_score:.4f}")
        
    return current_state, current_score

# --- Execution ---
if __name__ == "__main__":
    # Choose an arbitrary starting point
    initial_x = random.uniform(-10.0, 10.0)
    print(f"Starting Hill Search from x = {initial_x:.4f}...\n")
    
    final_x, max_val = hill_climbing(initial_x)
    print(f"\nOptimal Solution Found: x = {final_x:.4f} with Peak Value f(x) = {max_val:.4f}")