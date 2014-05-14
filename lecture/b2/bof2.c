#include <stdio.h>

void name(const char *str)
{
    char bof[64] = { 0x00, };
    strcpy(bof, str);
    printf("Your name is %s\n", bof);
}

int main(int argc, char **argv)
{
    if( argc != 2 ) {
        printf("Usage: %s [your name please]\n", argv[0]);
        return -1;
    }

    name(argv[1]);

    return 0;
}
