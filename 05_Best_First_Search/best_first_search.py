import heapq

def best_first_search(graph, heuristics, start, goal):
    """
    Performs Greedy Best-First Search using a priority queue.
    """
    # Priority queue stores tuples of (heuristic_value, node_name)
    priority_queue = [(heuristics[start], start)]
    visited = set()
    traversal_path = []

    print(f"Starting Best-First Search from '{start}' to '{goal}'...\n")

    while priority_queue:
        # Pop the node with the lowest heuristic value (closest to goal)
        current_h, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
            
        visited.add(current_node)
        traversal_path.append(current_node)
        
        print(f"Visited: {current_node} (h={current_h})")

        # Check if we have reached the goal
        if current_node == goal:
            print(f"\nGoal '{goal}' reached!")
            return traversal_path

        # Add unvisited neighbors to the priority queue
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))

    print("\nGoal could not be reached.")
    return traversal_path

# --- Execution ---
if __name__ == "__main__":
    # Define a graph using an adjacency list
    graph = {
        'S': ['A', 'B', 'C'],
        'A': ['S', 'D', 'E'],
        'B': ['S', 'F'],
        'C': ['S', 'H'],
        'D': ['A'],
        'E': ['A', 'G'],
        'F': ['B', 'G'],
        'H': ['C', 'G'],
        'G': ['E', 'F', 'H']
    }

    # Define the heuristic values h(n) for each node to the goal 'G'
    heuristics = {
        'S': 10,
        'A': 8,
        'B': 6,
        'C': 7,
        'D': 9,
        'E': 4,
        'F': 2,
        'H': 4,
        'G': 0  # Heuristic for the goal is always 0
    }

    start_node = 'S'
    goal_node = 'G'
    
    path = best_first_search(graph, heuristics, start_node, goal_node)
    print("\nTraversal Order:", " -> ".join(path))