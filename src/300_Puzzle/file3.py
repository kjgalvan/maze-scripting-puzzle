#!/bin/usr/python

board = [["X","X"," "," "," "," ","-"],
         ["X","X"," ","X","X","X","X"],
         ["X"," "," ","X","X","X","X"],
         ["X"," ","X","o","X","X","X"],
         ["X"," "," "," ","X","X","X"],
         ["X","X","X","X","X","X","X"]]

def getBoard():
    return board

def printBoard():
    print '\n'.join(' '.join(map(str, x)) for x in board)

def getAnswer():
    return "SAAWWDWWDDDD"