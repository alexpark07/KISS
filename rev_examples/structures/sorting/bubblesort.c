/*
 * code from http://blog.eairship.kr/35
 */

#include <stdio.h>
#include <stdlib.h>

void BubbleSort(int DataArray[], int length)
{
        int i=0, j=0, temp=0;

        for(i=0; i<length-1; i++) {
                for(j=i+1; j<length; j++) {
                        if(DataArray[i] > DataArray[j]) {
                                temp = DataArray[i];
                                DataArray[i] = DataArray[j];
                                DataArray[j] = temp;
                        }
                }
        }

        printf("Completed\n");
}


int main(int argc, char **argv)
{
        int *DataArray;
        int i=0;
        int length;

        printf("What size of int demension: ");
        scanf("%d", &length);
        DataArray = (int *)malloc(sizeof(int)*length);
        printf("\n");
        printf("Input number %d times for bubble sorting: ", length);

        for(i=0; i<length; i++) {
                scanf("%d", &DataArray[i]);
        }

        BubbleSort(DataArray, length);

        for(i=0; i<length; i++)
                printf("%d ", DataArray[i]);

        printf("\n");

        return 0;
}
