# read input into a list of numbers
with open("input.txt", "r") as f:
    fishes = [int(e) for e in f.readline()[:-1].split(",")]

# simulate for 80 days

for day in range(256):
    print (day, len(fishes))
    current_fish_count = len(fishes) 
    for i in range(current_fish_count):
        new_fish = fishes[i] - 1
        if (new_fish < 0):
            new_fish = 6
            fishes.append(8)
        
        fishes[i] = new_fish

# print len(input)

print (len(fishes))