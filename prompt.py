#! /usr/bin/python3
import lisp

print('Welcome to Bymers Lisp.')
print('press C-C or (quit) to exit.\n\n')
while True:
    str = input('>')
    pos, obj = lisp.parse(str)
    print(lisp.eval(obj))
