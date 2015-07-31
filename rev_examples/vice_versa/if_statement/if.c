#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
    int i;

    scanf ("%d", &i);

    if (i == 0) {
        printf("You inputed number 0\n");
    } else if (i == 1) {
        printf("You inputed number 1\n");
    } else {
        printf("You inputed number %d\n", i);
    }

    return 0;
}
