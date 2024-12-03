from collections import deque

def BFS(graph, start):
    # Initialize all vertices
    bfs_data = {}
    for vertex in graph:
        bfs_data[vertex] = {
            "color": "WHITE",
            "distance": float('inf'),
            "predecessor": None
        }
    
    # Initialize the starting vertex
    bfs_data[start]["color"] = "GRAY"
    bfs_data[start]["distance"] = 0
    bfs_data[start]["predecessor"] = None
    
    # Create a queue and enqueue the starting vertex
    queue = deque([start])
    
    while queue:
        u = queue.popleft()  # Dequeue a vertex
        for v in graph[u]:   # Explore neighbors
            if bfs_data[v]["color"] == "WHITE":
                bfs_data[v]["color"] = "GRAY"
                bfs_data[v]["distance"] = bfs_data[u]["distance"] + 1
                bfs_data[v]["predecessor"] = u
                queue.append(v)
        bfs_data[u]["color"] = "BLACK"  # Mark u as fully explored
    
    return bfs_data
