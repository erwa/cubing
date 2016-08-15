#!/usr/bin/env python
# Program for training mapping letter to sticker location.

import random
import sys

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWX')

print 'Press <Enter> to begin generating random letters from ' + str(alphabet)
print 'Press <Enter> after each random letter to generate another one.'
print 'Press <Ctrl> + D to exit.'
raw_input()

while True:
    try:
        index = random.randint(0, 23)
        print alphabet[index]
        raw_input()
    except EOFError:
        sys.exit()
