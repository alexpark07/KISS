#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void PrintArray(int arrData[], int length)
{
        int i;
        
        for(i=0; i<length; i++) {
                printf("%d ", arrData[i]);
        }
        printf("\n");
}

void InsertionSort(int arrData[], int length)
{
        int value = 0;
        int i, j;

        for(i=1; i<length; i++) {
                // if don't need to sort then just skip that.
                if(arrData[i-1] <= arrData[i]) {
                        printf("skipped: arrData[%d]: %d <= arrData[%d]: %d\n", i-1, arrData[i-1], i, arrData[i]);
                        continue;
                }

                value = arrData[i];
                printf("value: %d = arrData[%d]\n", value, i);

                for(j=0; j<i; j++) {
                        if(arrData[j] > value) {
                                /*
                                 * No sorted
                                 * +---+---+---+---+---+---+
                                 * | 3 | 4 | 6 | 2 | 8 | 1 |
                                 * +---+---+---+---+---+---+
                                 *
                                 * first move ( j > i )
                                 *               +-- i (value)
                                 *               V
                                 * +---+---+---+---+---+---+
                                 * | 3 | 4 | 6 | 2 | 8 | 1 |
                                 * +---+---+---+---+---+---+
                                 *   ^
                                 *   +-- j
                                 *
                                 * memmove(j+1, j, i-j); 
                                 *       +-- j+1 (destination)
                                 *       V
                                 * +---+---+---+---+---+---+
                                 * | 3 | 3 | 4 | 6 | 8 | 1 |
                                 * +---+---+---+---+---+---+
                                 *   ^
                                 *   +-- j (source)
                                 *
                                 * move small number to right place [j]
                                 *
                                 * +---+---+---+---+---+---+
                                 * | 2 | 3 | 4 | 6 | 8 | 1 |
                                 * +---+---+---+---+---+---+
                                 *   ^
                                 *   +-- j (value)
                                 *
                                 */
                                memmove(&arrData[j+1], &arrData[j], sizeof(arrData[0])*(i-j));
                                arrData[j] = value;
                                break;
                        }
                }

                PrintArray(arrData, length);
        }
}

int main(int argc, char **argv)
{
        int arrData[] = { 3, 4, 6, 2, 8, 1 };
        int length = sizeof(arrData) / sizeof(arrData[0]);

        printf("No sorted at all\n");
        PrintArray(arrData, length);
        InsertionSort(arrData, length);
}       
