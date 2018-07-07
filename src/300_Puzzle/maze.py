#!/usr/bin/python
import random
import importlib

fileIndex = random.randint(1,15)
filePath = "file" + `fileIndex`
file = importlib.import_module(filePath)

def input():
    try:
        print 'You have 1 second to solve.'
        print 'Move using WASD, get from o to -'
        file.printBoard()
        print 'Type answer, upper-case, (ex: WWAADS): '
        foo = raw_input()
        return foo
    except:
        return

s = input()

if s != None:
    if s == file.getAnswer():
        print 'Correct! flag{kiddie-scripter}'
    else:
        print 'Wrong!'