#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
    int i;

    scanf ("%d", &i);

    switch (i) {
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            printf("You inputed number is between 0 and 5 am I right?\n");
            break;
        case 10:
            printf("You inputed number 10\n");
            break;
        default:
            printf("You inputed number %d\n", i);
            break;
    }

    return 0;
}
