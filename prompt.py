#! /usr/bin/python3
import lisp

print('Welcome to Bymers Lisp.')
print('press C-C or (quit) to exit.\n\n')
while True:
    str = input('>')
    #Oops.
    if (len(str) == 0):
    	continue
    elif (str == "quit"):
    	break
    pos, obj = lisp.parse(str)
    print(pos, lisp.eval(obj))
