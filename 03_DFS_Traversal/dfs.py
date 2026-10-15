def dfs_recursive(graph, node, visited=None, dfs_order=None):
    """
    Performs Depth-First Search on a graph recursively.
    Returns a list of nodes in the order they were visited.
    """
    # Initialize data structures on the first call
    if visited is None:
        visited = set()
    if dfs_order is None:
        dfs_order = []
        
    # Mark the current node as visited and add it to our traversal path
    if node not in visited:
        visited.add(node)
        dfs_order.append(node)
        
        # Recursively visit all unvisited neighbors (going as deep as possible)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_recursive(graph, neighbor, visited, dfs_order)
                
    return dfs_order

# --- Execution ---
if __name__ == "__main__":
    # Define the same sample graph as BFS to compare traversal orders
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B', 'H'],
        'F': ['C'],
        'G': ['C'],
        'H': ['E']
    }

    start = 'A'
    print(f"Starting Recursive DFS traversal from node '{start}'...\n")
    traversal_path = dfs_recursive(graph, start)
    print("DFS Traversal Order:", " -> ".join(traversal_path))