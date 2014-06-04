from itertools import izip, cycle
import re

def xor_crypt_string(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
    
print re.escape(xor_crypt_string(data, key))
