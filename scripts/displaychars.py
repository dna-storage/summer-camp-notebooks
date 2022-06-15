from bitarray import bitarray
from copy import copy
import heapq
from math import log10, log2, ceil, sqrt

import re

from random import randint
try:
    from random import randbytes
except:
    def randbytes(b):
        return bytes([ randint(0,255) for _ in range(b) ])


def display_chars(filename,block):
    with open(filename,"r") as f:
        i = 0
        while (True):
            s = f.read(block)
            i += 1
            if len(s) > 0:
                #print ("{}: {}".format(i,(re.subn('\n','\\n',s)[0],)))
                print ("{}: {}".format(i,repr(s)))
            else:
                break

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print ("usage:  python displaychars.py [filename] [chars per line]")
        sys.exit(0)
    
    try:
        display_chars(sys.argv[1],int(sys.argv[2]))
    except Exception as e:
        print (e)
