#!/usr/bin/python
import sys
import file4

def getNeighbors(row, col):
    neighbors = []
    neighbors.append((row+1, col))
    neighbors.append((row-1, col))
    neighbors.append((row, col+1))
    neighbors.append((row, col-1))
    return neighbors

def direction(firstRow, firstCol, secondRow, secondCol):
    if firstRow - 1 == secondRow:
        return "W"
    if firstRow + 1 == secondRow:
        return "S"
    if firstCol - 1 == secondCol:
        return "A"
    if firstCol + 1 == secondCol:
        return "D"

board = file4.getBoard()

path = " "
start = "o"
end = "-"

pathIndexes = []

for index, value in enumerate(board):
    for subIndex, subValue in enumerate(value):
        if path == subValue:
            pathIndexes.append((index, subIndex))
    if start in value:
        subindex = value.index(start)
        startIndex = (index, subindex)
    if end in value:
        subindex = value.index(end)
        endIndex = (index, subindex)

def directionLoop(startIndex, endIndex, pathIndexes, directionString):
    if (endIndex == startIndex):
        return directionString
    else:
        neighbors = getNeighbors(*startIndex)
        nextStepSet = set(neighbors).intersection(pathIndexes)
        nextStep = list(nextStepSet)[0]
        newPath = [x for x in pathIndexes if x != nextStep]
        newStartIndex = nextStep
        newDirString = directionString + direction(startIndex[0], startIndex[1], nextStep[0], nextStep[1])
        return directionLoop(newStartIndex, endIndex, newPath, newDirString)

pathIndexes.append(endIndex)
print directionLoop(startIndex, endIndex, pathIndexes, "")