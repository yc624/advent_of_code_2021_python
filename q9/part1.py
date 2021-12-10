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

risk = 0
for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        if (am_I_the_lowest_point(inputs, i, j)):
            risk += 1 + inputs[i][j]

print(risk)
