import heapq

def a_star_search(graph, heuristics, start, goal):
    """
    Performs A* Search to find the shortest path from start to goal.
    f(n) = g(n) + h(n)
    """
    # Priority queue stores tuples of (f_score, current_node)
    priority_queue = [(heuristics[start], start)]
    
    # Dictionary to keep track of the shortest actual path cost g(n) from start to a node
    g_scores = {node: float('inf') for node in graph}
    g_scores[start] = 0
    
    # Dictionary to keep track of the path (child -> parent)
    came_from = {}
    
    visited = set()

    print(f"Starting A* Search from '{start}' to '{goal}'...\n")

    while priority_queue:
        # Pop the node with the lowest f(n) value
        current_f, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
            
        visited.add(current_node)
        print(f"Evaluating: {current_node} (f={current_f:.1f}, g={g_scores[current_node]:.1f}, h={heuristics[current_node]:.1f})")

        # If we reached the goal, reconstruct the path
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            
            print(f"\nGoal '{goal}' reached! Optimal cost: {g_scores[goal]}")
            return path

        # Evaluate neighbors
        for neighbor, edge_cost in graph[current_node].items():
            if neighbor in visited:
                continue
                
            # Calculate tentative g_score for the neighbor
            tentative_g_score = g_scores[current_node] + edge_cost
            
            # If this path to neighbor is better than any previous one
            if tentative_g_score < g_scores[neighbor]:
                came_from[neighbor] = current_node
                g_scores[neighbor] = tentative_g_score
                
                # f(n) = g(n) + h(n)
                f_score = tentative_g_score + heuristics[neighbor]
                heapq.heappush(priority_queue, (f_score, neighbor))

    print("\nGoal could not be reached.")
    return None

# --- Execution ---
if __name__ == "__main__":
    # Graph represented as an adjacency list with edge costs: graph[node][neighbor] = cost
    graph = {
        'S': {'A': 1, 'B': 4},
        'A': {'B': 2, 'C': 5, 'G': 12},
        'B': {'C': 2},
        'C': {'G': 3},
        'G': {}
    }

    # Heuristic values h(n) (straight-line distance to G)
    heuristics = {
        'S': 7,
        'A': 6,
        'B': 4,
        'C': 2,
        'G': 0
    }

    start_node = 'S'
    goal_node = 'G'
    
    optimal_path = a_star_search(graph, heuristics, start_node, goal_node)
    
    if optimal_path:
        print("\nOptimal Path:", " -> ".join(optimal_path))