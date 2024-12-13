def DFS(graph):
    # Initialize all vertices
    dfs_data = {}
    time = 0
    
    for vertex in graph:
        dfs_data[vertex] = {
            "color": "WHITE",  # Initially, all vertices are white (unvisited)
            "pi": None,        # Predecessor is None
            "d": None,         # Discovery time
            "f": None          # Finish time
        }

    # DFS visit function
    def DFS_VISIT(u):
        nonlocal time
        time += 1
        dfs_data[u]["d"] = time  # Set discovery time for u
        dfs_data[u]["color"] = "GRAY"  # Mark u as discovered (gray)

        # Explore each neighbor v of u
        for v in graph[u]:
            if dfs_data[v]["color"] == "WHITE":  # If v is unvisited
                dfs_data[v]["pi"] = u  # Set u as the predecessor of v
                DFS_VISIT(v)  # Visit the neighbor v

        dfs_data[u]["color"] = "BLACK"  # Mark u as fully explored (black)
        time += 1
        dfs_data[u]["f"] = time  # Set finish time for u

    # Perform DFS for each vertex in the graph
    for u in graph:
        if dfs_data[u]["color"] == "WHITE":
            DFS_VISIT(u)

    return dfs_data

# Example: Graph represented as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

# Run DFS on the graph
result = DFS(graph)

# Output the DFS result
for vertex, data in result.items():
    print(f"Vertex {vertex}: "
          f"Color = {data['color']}, "
          f"Discovery time = {data['d']}, "
          f"Finish time = {data['f']}, "
          f"Predecessor = {data['pi']}")
