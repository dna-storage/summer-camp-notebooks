from bitarray import bitarray
from copy import copy
import heapq
from math import log10, log2, ceil, sqrt

from dnastorage.codec.base_conversion import convertIntToBytes, convertToAnyBase


from random import randint
try:
    from random import randbytes
except:
    def randbytes(b):
        return bytes([ randint(0,255) for _ in range(b) ])

def reverse(s):
    l = [_ for _ in s]
    l.reverse()
    return "".join(l)
    
# helper function to know how many bytes are needed for a given integer
def num_bytes(a):
    if a<=1:
        return 1    
    return ceil(log2(abs(a+1))/log2(256))

def num_bits(a):
    return num_bytes(a)*8

def show_bits(a, join_char=" "):
    ba = bitarray()
    if type(a) == int:
        a = convertIntToBytes(a,num_bytes(a))
        a.reverse()
        ba.frombytes(bytes(a))
    elif type(a) == list:
        res = []
        for j in a:
            r = convertIntToBytes(j,num_bytes(j))
            r.reverse()
            res += r
        ba.frombytes(bytes(a))
    elif type(a) == str:
        a = bytes(a,'utf-8')
        ba.frombytes(a)            
    
    print ("{}".format(join_char.join(["{}".format(_) for _ in ba.tolist()])))

    
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
