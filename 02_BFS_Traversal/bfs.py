from collections import deque

def bfs(graph, start_node):
    """
    Performs Breadth-First Search on a graph.
    Returns a list of nodes in the order they were visited.
    """
    # Keep track of visited nodes to prevent cycles
    visited = set()
    # Queue for level-by-level traversal
    queue = deque([start_node])
    
    # Store the final traversal order
    bfs_order = []
    
    # Mark the start node as visited immediately
    visited.add(start_node)

    while queue:
        # Pop the oldest node from the front of the queue
        current_node = queue.popleft()
        bfs_order.append(current_node)

        # Iterate over all adjacent neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) # Add to the back of the queue

    return bfs_order

# --- Execution ---
if __name__ == "__main__":
    # Define a sample graph using an adjacency list
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
    print(f"Starting BFS traversal from node '{start}'...\n")
    traversal_path = bfs(graph, start)
    print("BFS Traversal Order:", " -> ".join(traversal_path))