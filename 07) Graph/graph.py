#if user chooses Graph (illustration)

elif structure == "Graph":
    graph = {}
    for elements in parsed:
        graph[elements] = []
    for i in range(len(parsed) - 1):
        current_node = parsed[i]
    next_node = parsed[i + 1]
    graph[current_node].append(next_node)
    print(f"Demonstation of graph (adjecent):")
    for node, edges in graph.items():
        print(f"Node [{node}] connects to -> Neighbours {edges}")
