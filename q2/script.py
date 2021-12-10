# parse the input  => [[instruction, value],...]
with open("input.txt", "r") as file:
    inputs = [line.split(" ") for line in file.read().splitlines()]

print(inputs)
# iterate the list => accumulate horizontal and depth 

horizontal = 0
depth = 0
aim = 0

for [instruction, value] in inputs:
    value = int(value)
    if (instruction == "forward"):
        horizontal += value
        depth += aim * value 
    elif (instruction == "up"):
        aim -= value
    elif (instruction == "down"):
        aim += value

print (horizontal * depth)