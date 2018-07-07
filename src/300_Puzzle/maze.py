#!/usr/bin/python
import signal
import sys
import random
import importlib

fileIndex = random.randint(1,15)
filePath = "file" + `fileIndex`
file = importlib.import_module(filePath)

TIMEOUT = 1

def interrupted(signum, frame):
    "called when read times out"
    print 'Try again!'
    sys.exit()
signal.signal(signal.SIGALRM, interrupted)

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

signal.alarm(TIMEOUT)
s = input()

signal.alarm(0)
if s != None:
    if s == file.getAnswer():
        print 'Correct! flag{kiddie-scripter}'
    else:
        print 'Wrong!'