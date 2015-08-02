#include <stdio.h>

void name(const char *str)
{
    char bof[64] = { 0x00, };
    strcpy(bof, str);
    printf("Your name is %s\n", bof);
}

int main(int argc, char **argv)
{
    FILE *fp;
    char buf[256] = { 0x00, };

    if( argc != 2 ) {
        printf("Usage: %s [your name please]\n", argv[0]);
        return -1;
    }

    fp = fopen(argv[1], "r");
    if (!fp) { 
        fprintf(stdout, "failed to open file: %s\n", argv[1]);
        return 0;
    }


    fread(buf, 1, 255, fp);
    fclose(fp);

    name(buf);

    return 0;
}
