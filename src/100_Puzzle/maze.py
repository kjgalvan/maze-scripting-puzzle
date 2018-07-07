#!/usr/bin/python

def board():
    board = [["X","X","X","X","-","X","X"],
             ["X","X","X","X"," ","X","X"],
             ["X","X","X","X"," ","X","X"],
             ["X"," "," "," "," ","X","X"],
             ["X"," ","X","X","X","X","X"],
             ["o"," ","X","X","X","X","X"]]
    print '\n'.join(' '.join(map(str, x)) for x in board)

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

s = input()

if s != None:
    if s == "DWWDDDWWW":
        print 'Correct! flag{ctrlshiftc-ctrlshiftv}'
    else:
        print 'Wrong!'