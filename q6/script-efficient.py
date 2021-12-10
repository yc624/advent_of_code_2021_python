# read input into a list of numbers
with open("input.txt", "r") as f:
    fishes = [int(e) for e in f.readline()[:-1].split(",")]

fish_dict = {}
for fish in fishes:
    if (not fish in fish_dict) :
        fish_dict[fish] = 0
    fish_dict[fish] += 1

fish_population_dict = {}

def fish_population(day, start_day):
    if (day in fish_population_dict and start_day in fish_population_dict[day]):
        return fish_population_dict[day][start_day]

    fish_pop = 0
    if (day == 0):
        fish_pop = 1
    else:
        if (start_day == 0):
            fish_pop = fish_population(day-1, 6) + fish_population(day-1, 8)
        else:
            fish_pop = fish_population(day-1, start_day-1)

    if (not day in fish_population_dict):
        fish_population_dict[day] = {}
    fish_population_dict[day][start_day] = fish_pop

    return fish_pop

fish_count = 0
for key, value in fish_dict.items():
    fish_count += fish_population(256, key) * value 

print (fish_count)