def generateFrequencies(inputs): 
    frequencies = []

    for position in range(len(inputs[0])):
        frequencies.append({})

    for position in range(len(inputs[0])):
        for number in inputs:
            f = frequencies[position]
            if (not number[position] in f):
                f[number[position]] = 0
            else:
                f[number[position]] += 1
    return frequencies

# read the inputs [['0', '1', ...],...]

with open("input.txt", "r") as file:
    inputs = file.read().splitlines()

# iterate the input list. calculate the frequency distribution of each bit
# [{'0':321, '1': 123}, ...]

frequencies = generateFrequencies(inputs)

# gamma 
gamma = ""
episilon = ""

for f in frequencies:
    if (f['0'] > f['1']):
        gamma += "0"
        episilon += "1"
    elif (f['0'] < f['1']):
        gamma += "1"
        episilon += "0"


print (int(gamma,2) * int(episilon,2))

def filterList(inputs, filter, position):
    ret = []
    for number in inputs:
        if (number[position] == filter):
            ret.append(number)
    return ret

oxygenList = inputs.copy()
position = 0
while (len(oxygenList) > 1):
    print (len(oxygenList))
    f = generateFrequencies(oxygenList)[position]
    print (f)
    newList = filterList(oxygenList, ('1' if (f['1'] >= f['0']) else '0'), position)
    oxygenList = newList
    position += 1

print (oxygenList[0])

carbonList = inputs.copy()
position = 0

while (len(carbonList) > 1):
    print (len(carbonList))
    f = generateFrequencies(carbonList)[position]
    print (f)
    newList = filterList(carbonList, ('0' if (f['1'] >= f['0']) else '1'), position)
    carbonList = newList
    position += 1

print (carbonList[0])

print (int(oxygenList[0],2) * int(carbonList[0], 2))
