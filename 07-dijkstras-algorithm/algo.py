from main import grid_size

unvisited_nodes = set([i for i in range(grid_size * grid_size)])

print(unvisited_nodes)

node_distances = { i: float("inf") for i in range(grid_size * grid_size)}

print(node_distances)
