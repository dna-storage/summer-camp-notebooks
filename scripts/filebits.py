from bitarray import bitarray
from copy import copy
import heapq
from math import log10, log2, ceil, sqrt

from random import randint
try:
    from random import randbytes
except:
    def randbytes(b):
        return bytes([ randint(0,255) for _ in range(b) ])


def display_bits(filename,block):
    with open(filename,"rb") as f:
        i = 0
        while (True):
            b = f.read(block)
            i += 1
            if len(b) > 0:
                ba = bitarray()
                ba.frombytes(b)
                print ("{}: {}".format(i," ".join(["{}".format(_) for _ in ba.tolist()])))
            else:
                break

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print ("usage:  python filebits.py [filename] [bytes per line]")
        sys.exit(0)
    
    try:
        display_bits(sys.argv[1],int(sys.argv[2]))
    except Exception as e:
        print (e)
