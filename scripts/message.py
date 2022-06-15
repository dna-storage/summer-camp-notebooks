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


def encode(num, ascolor=False, colors=['red', 'blue', 'green', 'orange']):
    #assert num >= 0 and num <= 63
    if ascolor:
        if type(num) == str:
            return [ colors[(ENC[num]//16)%4], colors[(ENC[num]//4)%4], colors[ENC[num]%4] ]
        else:
            return [ colors[(num//16)%4], colors[(num//4)%4], colors[num%4] ]        
    else:
        if type(num) == str:
            return [ (ENC[num]//16)%4, (ENC[num]//4)%4, ENC[num]%4 ]
        else:
            return [ (num//16)%4, (num//4)%4, num%4 ]        
                
ENC = {}

for i in range(ord('0'),ord('9')+1):
    ENC[ chr(i) ] = i - ord('0') 


for i in range(ord('A'),ord('Z')+1):
    ENC[ chr(i) ] = i - ord('A') + 16

i = 42
for c in [' ', ',', '.', '?', '-']:    
    ENC[c] = i
    i = i+1

ENC['\n'] = 63
    
message_original = \
'''\
Q. In other words, instead of a magnetic tape as a memory core of a computer, you will have
genes-
A. You will have substances allied to genes. Whether you call them genes or not
is a matter of phraseology, but substances of the same sort.
Now, that will involve a lot of new fundamental research. How to get in and out
of these genetic memories - how to put them to use - involves much research which has
scarcely started yet.
- Dr. Norbert Wiener, U.S. News and World Report, 1964.\
'''

message = \
'''\
Q. In other words, instead of a magnetic tape as a memory of a computer, you will have
genes-
A. You will have substances allied to genes. How to get in and out
of these genetic memories involves much research which has
scarcely started yet.
- Dr. Wiener, US News, 1964.\
'''

m = [ m.upper() for m in message ]

index = 0
size = 10
total = 0

while len(m) > 0:
    s = m[0:size]
    if len(s) < size:
        s += ' '*(size-len(s))

    codes = []
    for c in s:
        codes += encode(c)

    codes = encode(index//10) + encode(index%10) + codes
        
    print (index, "".join(s))
    #print (len(codes), codes)
    #print( ", ".join(["{}".format(c) for c in codes]))

    
    total += len(codes)
    index += 1
    m = m[size:]

print (total, "beads needed")
