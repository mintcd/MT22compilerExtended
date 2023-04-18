def chaitin(graph, num_colors):
    colors = {}  # Dictionary to store assigned colors for each vertex
    available_colors = set(range(num_colors))  # Set to store available colors at each step

    # Helper function to get the neighboring colors of a vertex
    def get_neighboring_colors(vertex):
        neighboring_colors = set()
        for neighbor in graph[vertex]:
            if neighbor in colors:
                neighboring_colors.add(colors[neighbor])
        return neighboring_colors

    # Find simplifyable vertices (vertices with fewer than num_colors outgoing edges)
    simplifyable_vertices = [vertex for vertex in graph if len(graph[vertex]) < num_colors]

    # Initialize available colors and assigned colors
    for vertex in graph:
        colors[vertex] = None

    # Loop through each simplifyable vertex in the graph
    for vertex in simplifyable_vertices:
        neighboring_colors = get_neighboring_colors(vertex)
        # Find the first available color not used by any neighboring vertices
        for color in available_colors:
            if color not in neighboring_colors:
                colors[vertex] = color
                break

        # If no color can be assigned, mark the vertex as "troublesome"
        if colors[vertex] is None:
            colors[vertex] = "troublesome"

    # Loop through the remaining vertices in the graph
    for vertex in graph:
        if vertex not in simplifyable_vertices:
            neighboring_colors = get_neighboring_colors(vertex)
            # Find the first available color not used by any neighboring vertices
            for color in available_colors:
                if color not in neighboring_colors:
                    colors[vertex] = color
                    break

    return colors

# Example graph represented as a dictionary
graph = {
    'a': {'c', 'b', 'd'},
    'b': {'a', 'f', 'c', 'd', 'e'},
    'c': {'a', 'b', 'd', 'e'},
    'd': {'c', 'a', 'b'},
    'e': {'c', 'b', 'f'},
    'f': {'b', 'e'},
    'g': {}
}

num_colors = 3  # Specify the number of colors

# Call the Chaitin's algorithm function
result = chaitin(graph, num_colors)

print(result)