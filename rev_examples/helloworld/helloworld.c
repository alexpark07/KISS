#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
    int i;
    char c;
    char buf[128] = {0x00, };
    unsigned int j;
    char *p;

    i = -1;
    j = 31337;
    c = '\x64';
    p = buf;
    strncpy(p, "Hello World", 11);
    printf("char *p:%s\n", p);
    printf("char buf:%s\n", buf);
    printf("signed int: %d\n", i);
    printf("unsigned int: %d\n", j);

    return 0xff;
}
