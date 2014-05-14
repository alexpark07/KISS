### Finds system address

```
$gdb print system
0xb7e53260
```

### Finds /bin/sh string in memory

```
gdb$ find &system, +999999, "/bin/sh"
0xb7f7bb98
warning: Unable to access 16000 bytes of target memory at 0xb7fc5f20, halting search.
1 pattern found.
```

### Disables ASLR 

``sudo sysctl -w kernel.randomize_va_space=2``


### Finds system@plt and /bin/sh's offset in libc for ROPing

```
objdump -d libc > di
grep "system>:" di
00041260 <__libc_system>:
strings -tx /lib/i386-linux-gnu/libc.so.6 | grep /bin/sh
 169b98 /bin/sh
```
