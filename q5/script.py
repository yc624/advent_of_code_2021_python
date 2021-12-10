with open("input.txt", "r") as file:
    inputs = [ x.split(" -> ") for x in file.read().splitlines()]

for i,[pair1, pair2] in enumerate(inputs):

    pair1 = pair1.split(",")
    pair2 = pair2.split(",")

    inputs[i] = {
        "p1": {"x": int(pair1[0]), "y": int(pair1[1])},
        "p2": {"x": int(pair2[0]), "y": int(pair2[1])},
    }

# print (inputs)

maxX = 0
maxY = 0

for line in inputs:
    if (line["p1"]["x"] > maxX): 
        maxX = line["p1"]["x"]
    elif (line["p2"]["x"] > maxX):
        maxX = line["p2"]["x"]
    
    if (line["p1"]["y"] > maxY):
        maxY = line["p1"]["y"]
    elif (line["p2"]["y"] > maxY): 
        maxY = line["p2"]["y"]

print(maxX, maxY)

answer = []
n = max(maxX, maxY)+1
print (n)
for i in range(n): 
    answer.append([0] * n)

def getRange(a, b):
    if (a > b):
        return range(b, a+1)
    return range(a, b+1)

def min(a, b):
    if (a < b):
        return a
    return b

for line in inputs:
    # print(line)
    if (line["p1"]["x"] == line["p2"]["x"]):
        # print("vertical")
        x = line["p1"]["x"]
        for y in getRange(line["p1"]["y"], line["p2"]["y"]):
            # print(x, y)
            answer[y][x] += 1
            # print(answer[y][x])

    elif (line["p1"]["y"] == line["p2"]["y"]):
        # print("horizontal")
        y = line["p1"]["y"]
        for x in getRange(line["p1"]["x"], line["p2"]["x"]):
            # print(x, y)
            answer[y][x] += 1
            # print(answer[y][x])      
    else:
        # print("not horizontal or vertical")
        xRange = getRange(line["p1"]["x"], line["p2"]["x"])
        yRange = getRange(line["p1"]["y"], line["p2"]["y"])

        if (not abs(line["p1"]["x"] - line["p2"]["x"]) == abs(line["p1"]["y"] - line["p2"]["y"])):
            print("NOT 45 degree")

        x = line["p1"]["x"]
        y = line["p1"]["y"]
        for i in xRange:
            answer[y][x] += 1
            y += int ((line["p2"]["y"] - line["p1"]["y"]) / abs(line["p1"]["y"] - line["p2"]["y"]))
            x += int ((line["p2"]["x"] - line["p1"]["x"]) / abs(line["p1"]["x"] - line["p2"]["x"]))


count = 0

for row in answer:
    for num in row:
        if num >= 2:
            count += 1

# print (answer)

print (count)