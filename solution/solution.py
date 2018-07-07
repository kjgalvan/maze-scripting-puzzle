#!/usr/bin/python

def neighbors(row, col):
    neighbors = []
    neighbors.append([row+1, col])
    neighbors.append([row-1, col])
    neighbors.append([row, col+1])
    neighbors.append([row, col-1])
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

board = [["X","X","X","X","-","X","X"],
         ["X","X","X","X"," ","X","X"],
         ["X","X","X","X"," ","X","X"],
         ["X"," "," "," "," ","X","X"],
         ["X"," ","X","X","X","X","X"],
         ["o"," ","X","X","X","X","X"]]

path = " "
start = "o"
end = "-"

pathIndexes = []

for index, value in enumerate(board):
    if path in value:
        subindex = value.index(path)
        pathIndexes.append([index, subindex])
    if start in value:
        subindex = value.index(start)
        startIndex = [index, subindex]
    if end in value:
        subindex = value.index(end)
        endIndex = [index, subindex]

neighbors = neighbors(*startIndex)

neighborsTuple = tuple(tuple(x) for x in neighbors)
pathTuple = tuple(tuple(x) for x in pathIndexes)

nextStepSet = set(neighborsTuple).intersection(pathTuple)
nextStep = list(list(nextStepSet)[0])
print nextStep
print (direction(startIndex[0], startIndex[1], nextStep[0], nextStep[1]))