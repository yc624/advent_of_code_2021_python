import numpy
from functools import reduce

def isFull(board):
    if len(board) == 5:
        return True
    else:
        return False


def addRowToBoards(boards, row):    
    if (isFull(boards[-1])):
        boards.append([])
    boards[-1].append(row)

def hasCheckBoardWon(checkBoard):
    # check all rows
    for row in checkBoard:
        if (reduce(lambda a,b: a and b, row, True) == True):
            return True 
    transposedCheckBoard = numpy.transpose(checkBoard)
    for row in transposedCheckBoard:
        if (reduce(lambda a,b: a and b, row, True) == True):
            return True 
    # check all columns
    return False 

def hasWon(board, called):
    # return true if won
    # false otherwise
    checkBoard = []
    for i in range(5):
        checkBoard.append([False] * 5)
    
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if (num in called):
                checkBoard[i][j] = True

    return hasCheckBoardWon(checkBoard)

def getWinningBoard(boards, called):
    for b in boards:
        if (hasWon(b, called)): 
            return b
    return None

def removeWinningBoard(boards, called):
    newBoards = []
    for i,b in enumerate(boards):
        if (not hasWon(b, called)):
            newBoards.append(b)
    return newBoards

def sumUnmarkedNumber(board, called):
    sum = 0
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if (not num in called):
                sum += int(num)
    return sum

# boards = [[ [r0], [r1],[r2],[r3],[r4] ], ... ]
boards = [[]]
numbersCalled = []

# populating the board
with open("input.txt", "r") as f:
    for i, line in enumerate(f):
        if i == 0:
            numbersCalled = line.split(",")
        elif i % 6 == 1:
            continue
        else: 
            addRowToBoards(boards, list(filter(lambda n: not n=="" , line[:-1].split(" "))))



# loop until there is a winning board 
numNumberCalled = 1
called = []

winningBoard = None

while (winningBoard == None):
    called = numbersCalled[0:numNumberCalled]
    numNumberCalled += 1 
    winningBoard = getWinningBoard(boards, called)
    

# calculate score
lastNumber = int(called[-1])
sum = sumUnmarkedNumber(winningBoard, called)

remainingBoards = boards.copy()
called = []
numNumberCalled = 1
lastBoard = None
print("what's going on?")
while (len(remainingBoards) > 0): 
    print(numNumberCalled)
    called = numbersCalled[0:numNumberCalled]
    print(called)
    numNumberCalled += 1 
    lastBoard=remainingBoards[0]
    remainingBoards = removeWinningBoard(remainingBoards, called)

# print(remainingBoards)
print(called)
# calculate score
lastNumber = int(called[-1])
print(lastNumber)

sum = sumUnmarkedNumber(lastBoard, called)

print(lastNumber * sum)

