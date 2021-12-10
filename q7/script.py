import sys
import os

print (os.getcwd())

def get_weighted_sum(position_dict):
    sum = 0
    for k, v in position_dict.items():
        sum += k * v
    return sum 

# read input into a list of numbers
with open(os.path.join(os.getcwd(),"q7/input.txt"), "r") as f:
    positions = [int(e) for e in f.readline().split(",")]

print(positions)

positions.sort()
position_count = len(positions)

print(positions)

position_dict = {}
for position in positions:
    if (not position in position_dict) :
        position_dict[position] = 0
    position_dict[position] += 1

print(position_dict)

# get weighted average 
weighted_average = get_weighted_sum(position_dict) / position_count

print (weighted_average)

unique_positions = list(position_dict.keys())
unique_positions.sort()

middle_i = None

for i, position in enumerate(unique_positions):
    if (position > weighted_average):
        middle_i = i
        break

print (middle_i, unique_positions[middle_i])


# recursively look for min 
def find_min_fuel_position(unique_positions, position_dict, m_pos):
    print("m_pos = ", m_pos)
    m = get_fuel_cost(position_dict, m_pos)

    l_pos = m_pos-1
    l = get_fuel_cost(position_dict, l_pos)
    while (l == m):
        l_pos -= 1
        l = get_fuel_cost(position_dict, l_pos)

    r_pos = m_pos+1
    r = get_fuel_cost(position_dict, r_pos)
    while (r == m):
        r_pos += 1
        r = get_fuel_cost(position_dict, r_pos)

    print (l, m, r)
    if (l > m and r > m): 
        return m 
    if (l > m and m > r):
        return find_min_fuel_position(unique_positions, position_dict, r_pos)
    if (r > m and m > l):
        return find_min_fuel_position(unique_positions, position_dict, l_pos)
    

def get_fuel_cost(position_dict, target_position):
    cost = 0
    for k,v in position_dict.items():
        cost += (1 + abs(k - target_position)) * abs(k - target_position) / 2 * v
    return cost 



print("3", get_fuel_cost(position_dict, 3))
print("4", get_fuel_cost(position_dict, 4))
print("5", get_fuel_cost(position_dict, 5))
print("6", get_fuel_cost(position_dict, 6))
print("7", get_fuel_cost(position_dict, 7))
print("8", get_fuel_cost(position_dict, 8))
print("9", get_fuel_cost(position_dict, 9))
print("10", get_fuel_cost(position_dict, 10))

print(unique_positions)

print (find_min_fuel_position(unique_positions, position_dict, int(weighted_average)))


