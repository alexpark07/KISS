#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
    int i;
    char c;
    char buf[128];
    unsigned int j;
    char *p;

    i = -1;
    j = 31337;
    c = '\x64';
    p = buf;
    strncpy(p, "Hello World", 11);
    printf("%s\n", p);


    return 0xff;
}
