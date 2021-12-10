import os

with open(os.path.join(os.getcwd(),"q9/input.txt"), "r") as f:
    inputs = [[ int(e) for e in list(l[:-1])] for l in f.readlines()]

def am_I_the_lowest_point(graph, i, j):
    my_value = graph[i][j]
    if (i - 1 >= 0):
        up = graph[i-1][j]
        if (my_value >= up):
            return False
    if (i + 1 < len(graph)):
        down = graph[i+1][j]
        if (my_value >= down):
            return False
    if (j - 1 >= 0):
        left = graph[i][j-1]
        if (my_value >= left):
            return False
    if (j + 1 < len(graph[i])):
        right = graph[i][j+1]
        if (my_value >= right):
            return False
    return True 

def has_visited(visited, i, j):
    if (i in visited and j in visited[i] and visited[i][j] == True):
        return True
    return False 


def should_be_added_to_queue(graph, visited, i, j):
    if (graph[i][j] == 9):
        return False
    if (has_visited(visited, i, j)):
        return False
    return True 

def get_basin_size(graph, low_i, low_j):
    print("get basin for ", low_i, low_j)
    queue = [[low_i,low_j]]
    visited = {}
    size = 0

    while (len(queue) > 0):
        print ("queue", queue)
        [i, j] = queue.pop(0)

        if(not has_visited(visited, i, j)):
            size += 1
            visiting_point_val = graph[i][j]
            if (not i in visited):
                visited[i] = {}
            visited[i][j] = True
        
            # up
            new_i = i-1
            new_j = j
            if (new_i >= 0): # has up point
                if (should_be_added_to_queue(graph, visited, new_i, new_j)):
                    queue.append([new_i, new_j])

            # down 
            new_i = i+1
            new_j = j
            if (new_i < len(graph)): # has down point
                if (should_be_added_to_queue(graph, visited, new_i, new_j)):
                    queue.append([new_i, new_j])

            # left
            new_i = i
            new_j = j-1
            if (new_j >= 0): # has left point
                if (should_be_added_to_queue(graph, visited, new_i, new_j)):
                    queue.append([new_i, new_j])
            # right
            new_i = i
            new_j = j+1
            if (new_j < len(graph[new_i])): # has right point
                if (should_be_added_to_queue(graph, visited, new_i, new_j)):
                    queue.append([new_i, new_j])
    print(size)
    return size

basins = []

for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        if (am_I_the_lowest_point(inputs, i, j)):
            basins.append({
                "low_point": [i,j],
                "size": None
            })
            
# calculate basin sizes 
for basin in basins:
    basin["size"] = get_basin_size(inputs, basin["low_point"][0], basin["low_point"][1])

basins.sort(key=lambda b:b["size"])

print (basins)

multiply = basins[-1]["size"] * basins[-2]["size"] * basins[-3]["size"]

print (multiply)