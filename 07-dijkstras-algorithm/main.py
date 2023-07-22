print("""This is an exploration of Dijkstra's Algorithm
It will find the shortest path between two endpoints
It moves up, down, left and right only, and cannot move diagonally on the grid      
""")

# grid_size = input("How big would you like the grid to be? ")
# start = input("Where in the grid do you want to start? ")
# finish = input("Where in the grid do you want to finish? ")

start=10
finish=0 # should be 4 steps

grid = {}
grid_size = 4

for i in range(grid_size):
    for j in range(grid_size):
        grid[grid_size * i + j] = (i, j)

print(grid)

unvisited_nodes = set([i for i in range(grid_size * grid_size)])

print(unvisited_nodes)



#  0  1  2  3
#  4  5  6  7
#  8  9 10 11
# 12 13 14 15

