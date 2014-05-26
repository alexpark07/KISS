#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void vuln()
{
    int j = 0xcafebabe;
    char buf[128] = { 0x00, };
    int i = 0xdeadbeef;
    fgets(buf, 128*2, stdin);

    printf("buf: %s\n", buf);
    printf("i: 0x%x / j: 0x%x\n", i, j);

}

int main(int argc, char **argv)
{


    printf("Input your message: ");
    fflush(stdout);

    vuln();

    return 0xff;
}
