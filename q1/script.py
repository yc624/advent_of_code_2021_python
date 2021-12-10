
def countIncreases(inputs):
    count = 0
    for index, depth in enumerate(inputs):
        # print(index, depth)
        if (index != 0 and inputs[index-1] < depth):
            count += 1
    return count

def getSumList(inputs):
    sumList = []
    for index, depth in enumerate(inputs):
        # get sum
        sum = 0
        if (index >= 2): 
            sum = inputs[index-2] + inputs[index-1] + depth 
            sumList.append(sum)
    return sumList

with open("input.txt", "r") as file:
    inputs = [ int(x) for x in file.read().splitlines()]
    
print(len(inputs))

sumList = getSumList(inputs)
print(len(sumList))
print(countIncreases(sumList))
