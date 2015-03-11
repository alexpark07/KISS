```c
#include <stdio.h>

void func(int a, int b, int c, int d, int e, int f, int g, int h, int i)
{
    printf("%d\n", i);
}

int main(void)
{
    func(1,2,3,4,5,6,7,8,9);
}
```

``rdi`` => 1st
``rsi`` => 2nd
``rdx`` => 3rd
``rcx`` => 4th
``r8``  => 5th
``r9``  => 6th

start from 7th will save on stack

```
(gdb) i r
rax            0x400568 4195688
rbx            0x0      0
rcx            0x4      4
rdx            0x3      3
rsi            0x2      2
rdi            0x1      1
rbp            0x7fffffffe070   0x7fffffffe070
rsp            0x7fffffffe050   0x7fffffffe050
r8             0x5      5
r9             0x6      6
r10            0x7fffffffdf00   140737488346880
r11            0x7ffff7a37dd0   140737348074960
r12            0x400440 4195392
r13            0x7fffffffe150   140737488347472
r14            0x0      0
r15            0x0      0
rip            0x400596 0x400596 <main+46>
eflags         0x212    [ AF IF ]
cs             0x33     51
ss             0x2b     43
ds             0x0      0
es             0x0      0
fs             0x0      0
gs             0x0      0
(gdb) x/16wx $sp
0x7fffffffe050: 0x00000007      0x00000000      0x00000008      0x00000000
0x7fffffffe060: 0x00000009      0x00000000      0x00000000      0x00000000
```
