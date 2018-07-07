#!/usr/bin/python
import signal
import sys

TIMEOUT = 2

def board():
    board = [["X","X","X","X"," ","X","X"],
             ["X","X","X","X"," ","X","X"],
             ["X","X","X","X"," ","X","X"],
             ["X"," "," "," "," ","X","X"],
             ["X"," ","X","X","X","X","X"],
             ["o"," ","X","X","X","X","X"]]
    print '\n'.join(' '.join(map(str, x)) for x in board)

def interrupted(signum, frame):
    "called when read times out"
    print 'Try again!'
    sys.exit()
signal.signal(signal.SIGALRM, interrupted)

def input():
    try:
        print 'You have 2 seconds to solve.'
        print 'Move using WASD, get from o to -'
        board()
        print 'Type answer: '
        foo = raw_input()
        return foo
    except:
        return

signal.alarm(TIMEOUT)
s = input()

signal.alarm(0)
if s != None:
    if s == "DWWDDDWWW":
        print 'Correct!'
    else:
        print 'Wrong!'